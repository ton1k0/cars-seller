from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String)
    model = Column(String)
    year_of_release = Column(Integer)
    car_body = Column(String)
    generation = Column(String)
    engine = Column(String)
    actuator = Column(String)
    transmission = Column(String)
    color = Column(String)
    mileage = Column(Integer)
    price = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="posts")


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    password = Column(String)

    posts = relationship('Post', back_populates='creator')