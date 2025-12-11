from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from . import models
from .routers import post, user, auth, votes


# alembic is setup so no need of create_all()
# models.Base.metadata.create_all(bind=engine)

app = FastAPI() 


# Create a list of allwoed origins
origins = ["*"]

# Middleware is a function that run before, after, or around main requests
# This runs before every request and determines which cross-origin requests are allowed.
app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,      # List of allowed origins. Empty = block all cross-origin requests
    allow_credentials=True,     # Allow credentials such as cookies/authorization headers
    allow_methods=["*"],        # Allow all HTTP request methods 
    allow_headers=["*"],        # Allow all headers
)

app.include_router(post.router)
app.include_router(user.router) 
app.include_router(auth.router)
app.include_router(votes.router) 

@app.get("/") 
def root(): 
    return {"message": "Hello World"} 
 

