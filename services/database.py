# Database configuration file
from dotenv import load_dotenv
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env file
load_dotenv()

# Database connection settings
DATABASE_NAME = getenv("DATABASE_NAME")
DATABASE_USER = getenv("DATABASE_USER")
DATABASE_PASSWORD = getenv("DATABASE_PASSWORD")
DATABASE_HOST = getenv("DATABASE_HOST")
DATABASE_PORT = getenv("DATABASE_PORT")

# Construct the database URL
DATABASE_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

# For SQLite (if needed)
# DATABASE_URL = getenv("DATABASE_URL", "sqlite:///./mental_health.db")

# Create connection
def get_database_url():
    return DATABASE_URL

# Create the SQLAlchemy engine
engine = create_engine(get_database_url())

# Create a declarative base class
Base = declarative_base()

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
