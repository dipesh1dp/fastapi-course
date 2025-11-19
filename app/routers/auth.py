from fastapi import APIRouter, Depends, status, HTTPException, Response  
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils, oauth2

router = APIRouter(tags=["Authentication"]) 

@router.post("/login", response_model=schemas.Token) 
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)): 
    """
    Login endpoint.

    Steps:
    1. FastAPI provides user_credentials (username & password) via OAuth2PasswordRequestForm.
    2. Use the database session to check if a user with the given email (username field) exists.
    3. If user does not exist → raise 404 error.
    4. If user exists, verify that the password is correct.
    5. If password is invalid → raise 404 error.
    6. If valid, create an access token containing the user's ID.
    7. Return the access token to the client (token type = bearer).
    """
    # Step 2: Fetch the user from the database
    user = db.query(models.User).filter(
        models.User.email == user_credentials.username).first() 

    # Step 3: Check if user exists
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Invalid Credentials") 
    # Step 4 & 5: Verify the password
    if not utils.verify(user_credentials.password, user.password): 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Invalid Credentials") 
    
    # Step 6 & 7: Create and return token
    access_token = oauth2.create_access_token(data={"user_id": user.id}) 
    return {"access_token": access_token, "token_type": "bearer"}
    
