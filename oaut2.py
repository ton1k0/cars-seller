from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

import token2

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Cloud not valibale credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    return token2.verify_token(token, credentials_exception)