from ninja import Schema
from datetime import datetime

class UserSchema(Schema):
    id: int
    username: str

class ArticleIn(Schema):
    author: int
    title: str
    content: str

class ArticleOut(Schema):
    id: int
    author: UserSchema
    created: datetime
    title: str
    content: str