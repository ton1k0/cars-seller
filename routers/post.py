from fastapi import APIRouter, Depends, status, HTTPException
import models, schemas, oaut2
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db
from scripts import post

router = APIRouter(
    prefix='/post',
    tags=['posts']
)


@router.get('/', status_code=201, response_model=List[schemas.ShowPost])
def all(db:Session = Depends(get_db)):
    return post.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Post, db: Session = Depends(get_db), current_user:schemas.User = Depends(oaut2.get_current_user)):
    return post.create(request,db, current_user)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db), current_user:schemas.User = Depends(oaut2.get_current_user)):
    return post.destroy(id,db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Post, db: Session = Depends(get_db),current_user:schemas.User = Depends(oaut2.get_current_user)):
    return post.update(id, request, db)


@router.get('/search')
def search(brand: str, model: str | None = None, generation: str| None = None,
           car_body: str | None = None, engine: str | None = None,
           actuator: str | None = None, transmission: str | None = None, price_from: int | None = None,
           price_to: int | None = None, year_of_release_from: int | None = None, year_of_release_to: int | None = None,
           mileage_from: int | None = None, mileage_to: int | None = None, db: Session = Depends(get_db)):
    return post.search(brand, model, generation,car_body,engine,actuator,transmission, price_from,price_to,
                       year_of_release_from,year_of_release_to,mileage_from,mileage_to,db)