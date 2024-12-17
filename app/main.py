from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import get_random_profiles
from app.schemas import Profile

app = FastAPI()


@app.get("/profiles/random", response_model=list[Profile])
def read_random_profiles(db: Session = Depends(get_db)):
    return get_random_profiles(db)
