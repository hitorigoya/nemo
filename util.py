from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi import HTTPException
from datetime import datetime, timedelta
from database import UserTable


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "59bceb84c6ed47eeb7b37fbaa67059c1c8daa0cac3ef0e47daf0543425fc1f4f"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24


def get_user_id_from_token(access_token):
    try:
        payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=404)

    return user_id


def create_jwt(user: UserTable):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": str(user.id), "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
