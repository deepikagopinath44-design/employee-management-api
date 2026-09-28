from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from auth import create_access_token
from database import get_db
from models import UserModel
from schemas import UserCreate, UserResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

@router.post(
    "/register",
    status_code=201,
    response_model=UserResponse
)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = db.query(UserModel).filter(
        UserModel.email == user.email
    ).first()

    if existing_user:
       raise HTTPException(
           status_code=400,
           detail="email already registered"
       )

    existing_username = db.query(UserModel).filter(
        UserModel.username == user.username
    ).first()

    if existing_username:
        raise HTTPException(
            status_code=400,
            detail= "Username already registered"
        )

    hashed_password = pwd_context.hash(user.password)

    new_user = UserModel(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login")
def login_user(
    from_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

   existing_user = db.query(UserModel).filter(
      UserModel.email == from_data.username
   ).first()

   if existing_user is None:
         raise HTTPException(
           status_code=401,
           detail="Invalid email or password"
      )

   if not pwd_context.verify(from_data.password, existing_user.password):
       raise HTTPException(
           status_code=401,
           detail="Invalid email or password"
       )
   access_token = create_access_token(
        {"sub": existing_user.email}
    ) 

   
   return {
       "access_token": access_token,
       "token_type": "bearer"
   }