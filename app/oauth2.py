from jose import JWTError, jwt, ExpiredSignatureError
import logging
from datetime import datetime, timedelta, timezone
from . import schemas, models, database
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings

# SECRET_KEY 
# Algorithm 
# Expiration time 

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

# OAuth2PasswordBearer tells FastAPI where clients should send the username/password
# to receive a token. Here, "login" is the token endpoint.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data: dict): 
    """
    Create a signed JWT access token.

    1. Copy the input data.
    2. Add an expiration timestamp.
    3. Encode the payload using the secret key and algorithm.
    4. Return the JWT string.
    """
    to_encode = data.copy() 
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) 
    to_encode.update({"exp": expire}) 
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  
    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    """
    Verify the provided JWT token.

    1. Decode the JWT using SECRET_KEY and ALGORITHM.
    2. Extract the "user_id" from the payload.
    3. Validate that user_id exists; otherwise raise authentication error.
    4. Handle expired or invalid token cases.
    5. Return token data object containing the user ID.
    """
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) 
        id = payload.get("user_id") 

        # Token is valid but missing required data
        if id is None: 
            raise credentials_exception 
        token_data = schemas.TokenData(id=id)
    
    # Handle expired token error
    except ExpiredSignatureError:
        logging.error(f"JWT token expired: {token}")
        raise credentials_exception
        
    # Catch other JWT-related errors
    except JWTError as e:
        logging.error(f"JWT decoding error: {e}")
        raise credentials_exception
    
    return token_data


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)): 
    """
    Retrieve the currently authenticated user.

    1. Extract the Bearer token from the Authorization header.
    2. Verify and decode the token.
    3. Look up the user in the database using the token's user_id.
    4. Return the matching User model instance.
    """
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="could not validate credentials", 
                                          headers={"WWW-Authenticate": "Bearer"}) 
    
    token = verify_access_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user