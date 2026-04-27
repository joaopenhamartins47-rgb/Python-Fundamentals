from typing import Annotated
from starlette import status
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED

from database import Sessionlocal
from models import Users
from passlib.context import CryptContext #to hash password
router = APIRouter()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class CreateUserRequest(BaseModel): #Create to validate the inputs in post methods
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    roll: str

def get_db():
    db = Sessionlocal()
    try:
        yield db #Entrega a sessao para o endpoint
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/auth", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency,
                      create_user: CreateUserRequest): #Nao funciona com ** e o parametro porque tenho um hash_password
    create_user_model = Users(
        email=create_user.email,
        username=create_user.username,
        first_name = create_user.first_name,
        last_name = create_user.last_name,
        role = create_user.roll,
        hashed_password = bcrypt_context.hash(create_user.password),
        is_active=True
    )

    db.add(create_user_model)
    db.commit()
