from fastapi import FastAPI, HTTPException, Depends,Response
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
@app.post("/posts", response_model=schemas.PostOut, status_code=201)
def create_post(post:schemas.PostCreate, db:Session = Depends(get_db)):
    db_post = models.Post(
        title=post.title,
        content=post.content,
        category=post.category,
        tags=",".join(post.tags)
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@app.get("/posts", response_model=List[schemas.PostOut])
def get_posts(term: str = "", db: Session = Depends(get_db)):
    query = db.query(models.Post)
    if term:
        query = query.filter(
            (models.Post.title.contains(term) |
             models.Post.content.contains(term) |
             models.Post.category.contains(term))
        )
    
    return query.all()


@app.get("/posts/{post_id}", response_model = schemas.PostOut)
def get_post(post_id:int, db:Session=Depends(get_db)):
    post = db.query(models.Post).get(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.put("/posts/{post_id}", response_model=schemas.PostOut)
def update_post(post_id: int, post:schemas.PostCreate, db:Session=Depends(get_db)):

    db_post = db.query(models.Post).get(post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    for key,value in post.dict().items():
        if key=="tags":
            setattr(db_post, key,",".join(value))
        else:
            setattr(db_post,key,value)
    db.commit()
    db.refresh(db_post)
    return db_post

@app.delete("/posts/{post_id}", status_code=204)
def delete_post(post_id:int, db:Session=Depends(get_db)):
    db_post = db.query(models.Post).get(post_id)

    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(db_post)
    db.commit()
    return Response(status_code=204)
