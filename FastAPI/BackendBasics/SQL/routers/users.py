from typing import Annotated
from pydantic import BaseModel, Field
from starlette import status
from fastapi import APIRouter, Depends, HTTPException, Path
from models import Users
from database import Sessionlocal
from sqlalchemy.orm import Session
from .auth import get_current_user
from passlib.context import CryptContext

router = APIRouter(
    prefix='/Users',
    tags=['user']
)

class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)


def get_db():
    db = Sessionlocal()
    try:
        yield db #Entrega a sessao para o endpoint
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto') #gerar hash de senha, verificar senha, gerenciar algoritmos de criptografia de senha


@router.get("/data")
async def read_all_informations(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not encountered')
    return db.query(Users).filter(Users.id == user.get('id')).first()

@router.put("/change_pass")
async def change_pass(user: user_dependency, db: db_dependency, user_verification: UserVerification):
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not encountered')
    current_password = db.query(Users).filter(Users.id == user.get('id')).first()

    if not bcrypt_context.verify(user_verification.password, current_password.hashed_password):
        raise HTTPException(status_code=401, detail='Error on password change')
    current_password.hashed_password = bcrypt_context.hash(user_verification.new_password)
    db.add(current_password)
    db.commit()


