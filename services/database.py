# Database configuration file
from os import getenv

# Database connection settings
DATABASE_NAME = getenv("DATABASE_NAME", "calmcollectiv_db")
DATABASE_USER = getenv("DATABASE_USER", "jamesl1500")
DATABASE_PASSWORD = getenv("DATABASE_PASSWORD", "Cooley12%")
DATABASE_HOST = getenv("DATABASE_HOST", "localhost")
DATABASE_PORT = getenv("DATABASE_PORT", "3306")

# Construct the database URL
DATABASE_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

# For SQLite (if needed)
# DATABASE_URL = getenv("DATABASE_URL", "sqlite:///./mental_health.db")

# Example usage: