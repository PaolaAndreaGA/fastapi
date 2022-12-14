
# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel


# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path


app = FastAPI()

# Models


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


@app.get("/")
def home():
    return {"hello": "world"}

# request and response body


@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person


# validations query paramenters
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title="Person Name",
        description="This is the person name. it's between 1 and 50 characters"
    ),
    age: str = Query(
        ...,
        title="Person Age",
        description="This is the person age. it's required"
    )
):
    return {name: age}

# validations path parameters


@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person Id",
        description="This is the person Id. it's required"
    ),
):
    return {person_id: "It exists!"}
