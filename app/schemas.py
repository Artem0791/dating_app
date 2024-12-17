from pydantic import BaseModel


class Profile(BaseModel):
    id: int
    name: str
    age: int
    bio: str

    class Config:
        from_attributes = True
