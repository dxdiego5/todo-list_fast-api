from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    disabled: bool = True


class UserDB(UserSchema):
    id: int


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
    disabled: bool


class UserList(BaseModel):
    users: list[UserPublic]

    class Config:
        orm_mode = True
