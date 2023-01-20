from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException

from models import Gender, Role, User

app = FastAPI()

db: List[User] = [
    User(
        id='837688c4-afb8-41f6-890f-99130500a676',
        first_name="Nicholas",
        last_name="Chung",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id='837688c4-afb8-41f6-890f-99130500a679',
        first_name="Nicholas",
        last_name="Chung",
        gender=Gender.female,
        roles=[Role.admin, Role.user]
    )
]


@app.get("/")
async def root():
    return {"hello": "Mundo"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_users(user: User):
    db.append(user)
    return {id: user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        tempUser = user
        if user.id == user_id:
            db.remove(user)
            return tempUser.first_name
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} is not available."
        )
