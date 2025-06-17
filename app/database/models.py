from datetime import datetime
from enum import Enum

from sqlmodel import Field, SQLModel


class SexEnum(str, Enum):
    male = "male"
    female = "female"


class EducationLevelEnum(str, Enum):
    graduate_school = "graduate school"
    high_school = "high school"
    university = "university"
    others = "others"
    unknown = "unknown"


class MaritalStatusEnum(str, Enum):
    single = "single"
    married = "married"
    others = "others"
    unknown = "unknown"


class PredictionRequest(SQLModel, table=True):
    __tablename__ = "prediction_request"

    id: int = Field(default=None, primary_key=True, gt=100000)
    limit_balance: int | None = Field(default=None, nullable=True)
    sex: SexEnum | None = Field(default=None, nullable=True)
    education_level: EducationLevelEnum | None = Field(default=None, nullable=True)
    marital_status: MaritalStatusEnum | None = Field(default=None, nullable=True)
    age: int | None = Field(default=None, ge=15, le=110, nullable=True)
    created_at: datetime | None = Field(default_factory=datetime.now, nullable=True)
