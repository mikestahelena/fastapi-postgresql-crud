from pydantic import BaseModel
from typing import Optional
from datetime import date


class Customer(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    document: str
    birthdate: date

    class Config:
        orm_mode = True
