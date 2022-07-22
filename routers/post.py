from fastapi import APIRouter, Depends, status, HTTPException
import models, schemas, oaut2
from sqlalchemy.orm import Session
from typing import List
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
def create(request: schemas.Post, db: Session = Depends(get_db),current_user:schemas.User = Depends(oaut2.get_current_user)):
    return post.create(request,db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db), current_user:schemas.User = Depends(oaut2.get_current_user)):
    return post.destroy(id,db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Post, db: Session = Depends(get_db),current_user:schemas.User = Depends(oaut2.get_current_user)):
    return post.update(id, request, db)