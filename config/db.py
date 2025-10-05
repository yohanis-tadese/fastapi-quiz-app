from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError

# Configure database url
DATABASE_URL = "postgresql://postgres:dev_jhon@localhost:5432/py_quize_fastapi"

# Create database engine
# define how to connect to the database
engine = create_engine(DATABASE_URL)

# test database connection
try:
    # Try to connect to the database
    with engine.connect() as connection:
        print("Database connection successful")
except OperationalError as e:
    # handle connection error
    print(f"Database connection error: {e}")

# Create a configured "Session" class
# define how to talk sqlalchemy with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
# define how to create models (tables) in the database
Base = declarative_base()

# define get_db function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
