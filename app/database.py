from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base # A base class for creating ORM models (tables).
from sqlalchemy.orm import sessionmaker 

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:2058@localhost/fastapi"   # dialect+driver://username:password@host:port/database_name

# Create a database connection engine.
engine = create_engine(SQLALCHEMY_DATABASE_URL) 

# Create a db session factory 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

# Create Base Class for ORM models
Base = declarative_base()

def get_db(): 
    db = SessionLocal() 
    try: 
        yield db     #  yields the database session db to the caller
    finally: 
        db.close()   # ensure the db session is closed even though error occurs
