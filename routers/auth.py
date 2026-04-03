## Libraries
from fastapi import APIRouter, Depends, HTTPException
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlmodel import Session, select

## Internal
from models.users import User
from config.database import get_session, engine

auth_router = APIRouter()
preurl = "auth"

@auth_router.post('/%s/login' % (preurl), tags=['auth'])
def login(data: User, session: Session = Depends(get_session)):
    statement = select(User).where(User.email == data.email)
    record = session.exec(statement).first()
    if not record:
        raise HTTPException(status_code=404, detail="Usuario no existe")             
    else:
        if data.password == record.password:
            token: str = create_token(data.dict())
            result = {
                "id": record.id,
                "token": token
            }
            return JSONResponse(status_code=200, content=jsonable_encoder(result))
        else:
            raise HTTPException(status_code=400, detail="Contraseña incorrecta")
            

@auth_router.post('/%s/user' % (preurl), tags=['auth'])
def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user