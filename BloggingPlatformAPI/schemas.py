from pydantic import BaseModel, validator
from typing import List,Optional
from datetime import datetime

class PostCreate(BaseModel):
    title: str
    content: str
    category: Optional[str] = None
    tags: Optional[List[str]] = []

class PostOut(PostCreate):
    id: int
    createdAt: datetime
    updatedAt: datetime

    class Config:
        orm_mode=True

    @validator("tags", pre=True)
    def split_tags(cls, v):
        if isinstance(v, str):
            return v.split(",") if v else []
        return v