from fastapi import Depends, HTTPException, status
import schemas, models, hashing
from sqlalchemy.orm import Session
from database import get_db


def create_user(request: schemas.User, db: Session = Depends(get_db)):
    email = db.query(models.User).filter(models.User.email == request.email).all()
    if not email:
        phone = db.query(models.User).filter(models.User.phone == request.phone).all()
        if not phone:
            new_user = models.User(name=request.name, email=request.email,
                                   password=hashing.Hash.bcrypt(request.password), phone=request.phone)
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return new_user
        else:
            raise HTTPException(status_code=status.HTTP_423_LOCKED,
                            detail={'detail': f'This phone is already used'})
    else:
        raise HTTPException(status_code=status.HTTP_423_LOCKED,
                            detail={'detail': f'This email is already used'})

def show(id:int,db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with the id {id} not found')
    return user