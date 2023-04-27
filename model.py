from pydantic import BaseModel, EmailStr, Field


class UserAuth(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, regex="^[a-zA-Z0-9]+$")


class UpdateContent(BaseModel):
    id: int
    title: str | None = None
    content: str | None = None


class User(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True


class Content(BaseModel):
    id: int
    user_id: int
    title: str
    content: str

    class Config:
        orm_mode = True
