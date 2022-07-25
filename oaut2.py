from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import models
from database import get_db

import token2

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Cloud not valibale credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    token_data = token2.verify_token(token, credentials_exception)
    return db.query(models.User).filter(models.User.email == token_data.email).first()