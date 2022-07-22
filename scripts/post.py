from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import models, schemas


def get_all(db: Session):
    posts = db.query(models.Post).all()
    return posts


def create(request: schemas.Post, db: Session):
    new_post = models.Post(brand=request.brand, model=request.model,
                           year_of_release=request.year_of_release,car_body=request.car_body,
                           generation=request.generation, engine=request.engine,
                           actuator=request.actuator, transmission=request.transmission,
                           color=request.color, mileage=request.mileage, price=request.price, user_id=1)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def destroy(id:int, db: Session):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with id {id} not found')
    post.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id:int, request:schemas.Post, db:Session):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    post.update(request.dict())
    db.commit()
    return 'updated'