from typing import Dict

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Address(BaseModel):
    street: str
    city: str


class User(BaseModel):
    name: str = None
    age: int = None
    relations: Dict[str, Address] = None


@app.get("/")
async def root() -> User:
    return {"name": "John", "age": 25, "relations": {"friend": {"street": "123 Main St", "city": "Springfield"},
                                                     "family": {"street": "456 Elm St", "city": "Springfield"}}}

