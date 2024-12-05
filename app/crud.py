from sqlalchemy.orm import Session
from app.models import Profile
from sqlalchemy.sql.expression import func


def get_random_profiles(db: Session, limit: int = 10):
    return db.query(Profile).order_by(func.random()).limit(limit).all()
