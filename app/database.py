from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base # A base class for creating ORM models (tables).
from sqlalchemy.orm import sessionmaker 
from .config import settings 


# dialect+driver://username:password@host:port/database_name
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"   

# Create a database connection engine.
engine = create_engine(SQLALCHEMY_DATABASE_URL) 

# Create a db session factory 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

# Create Base Class for ORM models
Base = declarative_base()

def get_db(): 
    """
    Dependency that provides a database session
    """
    db = SessionLocal() 
    try: 
        yield db     #  yields the database session db to the caller
    finally: 
        db.close()   # ensure the db session is closed even though error occurs




# --- Old psycopg2 connection code (no longer needed after switching to SQLAlchemy) ---
# import psycopg2
# from psycopg2.extras import RealDictCursor  

## Keep trying until database connection is made
# while True:
#     try: 
        # conn = psycopg2.connect(host=settings.database_hostname, database=settings.database_username, user=settings.database_username, password=settings.database_password, 
#                                 cursor_factory=RealDictCursor) # returns query results as real Python dictionaries instead of the default tuples.
#         cursor = conn.cursor() 
#         print("Database connection was successful!")
#         break
#     except Exception as error: 
#         print("Connecting to database failed") 
#         print("Error: ", error)
#         time.sleep(2)


