from sqlalchemy import and_, or_, not_
from fastapi import HTTPException, status
from pydantic.class_validators import Optional
from sqlalchemy.orm import Session
import models, schemas



def get_all(db: Session):
    posts = db.query(models.Post).all()
    return posts


def create(request: schemas.Post, db: Session, current_user: schemas.User_id):
    new_post = models.Post(brand=request.brand, model=request.model,
                           year_of_release=request.year_of_release,car_body=request.car_body,
                           generation=request.generation, engine=request.engine,
                           actuator=request.actuator, transmission=request.transmission,
                           color=request.color, mileage=request.mileage, price=request.price, user_id = current_user.id)
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


def search(brand: str, model: str, generation: str,car_body: str,
           engine: str, actuator: str, transmission: str, price_from: int, price_to: int,
           year_of_release_from: int, year_of_release_to: int, mileage_from: int, mileage_to: int,
           db: Session, limit: int = 10, skip: int = 0):
    post = db.query(models.Post).filter(and_(brand == None or models.Post.brand == brand,
                                             model == None or models.Post.model.contains(model)),
                                             generation == None or models.Post.generation == generation,
                                             car_body == None or models.Post.car_body == car_body,
                                             engine == None or models.Post.engine == engine,
                                             actuator == None or models.Post.actuator == actuator,
                                             transmission == None or models.Post.transmission == transmission,
                                             price_from == None or models.Post.price >= price_from,
                                             price_to == None or models.Post.price <= price_to,
                                             year_of_release_from == None or models.Post.year_of_release >= year_of_release_from,
                                             year_of_release_to == None or models.Post.year_of_release <= year_of_release_to,
                                             mileage_from == None or models.Post.mileage >= mileage_from,
                                             mileage_to == None or models.Post.mileage <= mileage_to).all()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={'detail': f'Post with this filters is not found'})
    return post[skip : skip + limit]