from typing import List, Optional
from pydantic import BaseModel


class PostBase(BaseModel):
    brand: str
    model: str
    year_of_release: int
    car_body: str
    generation: str
    engine: str
    actuator: str
    transmission: str
    color: str
    mileage: int
    price: int

class Post(PostBase):
    class Config():
        orm_mode=True


class User(BaseModel):
    name: str
    email: str
    phone:str
    password: str

class ShowUser(BaseModel):
    name:str
    email:str
    phone: str
    posts: List[Post] = []
    class Config():
        orm_mode=True


class ShowPost(BaseModel):
    id: int
    brand: str
    model: str
    year_of_release: int
    car_body: str
    generation: str
    engine: str
    actuator: str
    transmission: str
    color: str
    mileage: int
    price: int
    creator: ShowUser
    class Config():
        orm_mode=True



class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None