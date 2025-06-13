from sqlmodel import Field, SQLModel, create_engine, Session, List

class UserBase(SQLModel):
    limit_balance: int
    sex: str = list['1', '2']
    education_level: str = list['1', '2', '3', '4', '5', '6']
    marital_status: str = list['1', '2', '3']
    age: int
