from fastapi import FastAPI, HTTPException, Response
from fastapi import Depends, Cookie, Header
from fastapi.staticfiles import StaticFiles
from sqlalchemy import event
from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine
from database import Base, UserTable, ContentTable, engine
from model import *
from util import create_jwt, get_user_id_from_token, check_xsrf_tokens, password_context
import secrets


app = FastAPI()
api = FastAPI(title="api")
web = StaticFiles(directory="svelte/build", html=True)
app.mount("/api", api)
app.mount("/", web)


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


Base.metadata.create_all(engine)


class Tokens:
    def __init__(
        self,
        access_token: str | None = Cookie(default=None),
        xsrf_token: str | None = Cookie(default=None),
        x_xsrf_token: str | None = Header(default=None),
    ):
        self.access = access_token
        self.xsrf = xsrf_token
        self.x_xsrf = x_xsrf_token


@api.get("/")
def root():
    return "hello world"


@api.post("/signup/", response_model=User)
def user_signup(signup: UserAuth, response: Response):
    with Session(engine) as db:
        db_user = db.query(UserTable).filter_by(email=signup.email).first()
        if db_user is None:
            pass
        else:
            raise HTTPException(status_code=404, detail="error: user_signup")

        hashed_password = password_context.hash(signup.password)
        user = UserTable(email=signup.email, hashed_password=hashed_password)
        db.add(user)
        db.commit()
        db.refresh(user)

    encoded_jwt = create_jwt(user)
    response.set_cookie(key="access_token", value=encoded_jwt, httponly=True)
    response.set_cookie(key="xsrf_token", value=secrets.token_hex(16))
    return user


@api.post("/login/", response_model=User)
def user_login(login: UserAuth, response: Response):
    with Session(engine) as db:
        db_user = db.query(UserTable).filter_by(email=login.email).one()

    if not password_context.verify(login.password, db_user.hashed_password):
        raise HTTPException(status_code=404, detail="error: user_login")

    encoded_jwt = create_jwt(db_user)
    response.set_cookie(key="access_token", value=encoded_jwt, httponly=True)
    response.set_cookie(key="xsrf_token", value=secrets.token_hex(16))
    return db_user


@api.get("/user/", response_model=User)
def get_current_user(tokens: Tokens = Depends()):
    if not check_xsrf_tokens(tokens.xsrf, tokens.x_xsrf):
        raise HTTPException(status_code=404)

    with Session(engine) as db:
        user_id = get_user_id_from_token(tokens.access)
        db_user = db.query(UserTable).filter_by(id=user_id).one()
    return db_user


@api.get("/content/", response_model=list[Content])
def get_contents(tokens: Tokens = Depends()):
    if not check_xsrf_tokens(tokens.xsrf, tokens.x_xsrf):
        raise HTTPException(status_code=404)

    with Session(engine) as db:
        user_id = get_user_id_from_token(tokens.access)
        db_contents = db.query(ContentTable).filter_by(user_id=user_id).all()

    return db_contents


@api.post("/content/", response_model=Content)
def create_content(tokens: Tokens = Depends()):
    if not check_xsrf_tokens(tokens.xsrf, tokens.x_xsrf):
        raise HTTPException(status_code=404)

    with Session(engine) as db:
        user_id = get_user_id_from_token(tokens.access)
        db_user = db.query(UserTable).filter_by(id=user_id).one()
        content = ContentTable(user_id=user_id, title="無題", content="")
        db.add(content)
        db.commit()
        db.refresh(content)

    return content


@api.put("/content/", response_model=Content)
def update_content(update_content: UpdateContent, tokens: Tokens = Depends()):
    if not check_xsrf_tokens(tokens.xsrf, tokens.x_xsrf):
        raise HTTPException(status_code=404)

    with Session(engine) as db:
        user_id = get_user_id_from_token(tokens.access)
        db_user = db.query(UserTable).filter_by(id=user_id).one()
        db_content = db.query(ContentTable).filter_by(id=update_content.id).one()

        if not db_user.id == db_content.user_id:
            raise HTTPException(status_code=404)

        if update_content.title:
            db_content.title = update_content.title

        if update_content.content:
            db_content.content = update_content.content

        db.commit()
        db.refresh(db_content)

    return db_content


@api.delete("/content/{content_id}", response_model=Content)
def delete_content(content_id: int, tokens: Tokens = Depends()):
    if not check_xsrf_tokens(tokens.xsrf, tokens.x_xsrf):
        raise HTTPException(status_code=404)

    with Session(engine) as db:
        user_id = get_user_id_from_token(tokens.access)
        db_user = db.query(UserTable).filter_by(id=user_id).one()
        db_content = db.query(ContentTable).filter_by(id=content_id).one()

        if not db_user.id == db_content.user_id:
            raise HTTPException(status_code=404)

        db.delete(db_content)
        db.commit()

    return db_content
