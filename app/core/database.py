from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from app.core.config import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

sessionlocal = sessionmaker(
    autocommit =False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = sessionlocal()

    try:
        yield db

    finally:
        db.close()