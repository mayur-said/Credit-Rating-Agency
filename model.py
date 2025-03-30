from pydantic import BaseModel, Field
from enum import Enum
from typing import Annotated

class LoanType(Enum):
    FIXED = "fixed"
    ADJUSTABLE = "adjustable"

class PropertType(Enum):
    SINGLE_FAMILY = "single_family"
    CONDO = "condo"

class Mortgage(BaseModel):
    credit_score: Annotated[int, Field(ge=300, le=850)]
    loan_amount: float
    property_value: float
    annual_income: float
    debt_amount: float
    loan_type: LoanType
    property_type: PropertType



