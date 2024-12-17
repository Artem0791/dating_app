from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

SQLALCHEMY_DATABASE_URL = "postgresql://app_user:securepassword@postgres:5432/dating_app"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)



"""
How to up a docker postgres container

docker run --name postgres \
  -e POSTGRES_USER=app_user \
  -e POSTGRES_PASSWORD=securepassword \
  -e POSTGRES_DB=dating_app \
  -p 5432:5432 \
  -d postgres:15

"""