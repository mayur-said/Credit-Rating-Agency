from model import Mortgage
from pydantic import ValidationError
from utils import process_error_response


def process_credit_rating_response(credit_rating: str) -> dict:
    return {"error": False, "message": {'credit_rating': credit_rating}}


def calculate_risk_score(mortgage: Mortgage) -> int:
    risk_score = 0
    
    # Loan-to-Value (LTV) Ratio
    ltv_ratio = mortgage.loan_amount / mortgage.property_value * 100
    if ltv_ratio > 90:
        risk_score += 2
    elif ltv_ratio > 80:
        risk_score += 1
    
    # Debt-to-Income (DTI) Ratio
    dti_ratio = mortgage.debt_amount / mortgage.annual_income * 100
    if dti_ratio > 50:
        risk_score += 2
    elif dti_ratio > 40:
        risk_score += 1
    
    # Credit Score
    if mortgage.credit_score >= 700:
        risk_score -= 1
    elif mortgage.credit_score < 650:
        risk_score += 1
    
    # Loan Type
    if mortgage.loan_type.value == 'fixed':
        risk_score -= 1
    
    if mortgage.loan_type.value == 'adjustable':
        risk_score += 1
    
    # Property Type
    if mortgage.property_type.value == 'condo':
        risk_score += 1
    
    return risk_score


def calculate_credit_rating(mortgage_payload_list: list) -> dict:
    try:
        total_risk_score = 0
        credit_scores = []
        for mortgage_payload in mortgage_payload_list:
            mortgage = Mortgage(**mortgage_payload)
            risk_score = calculate_risk_score(mortgage)
            credit_scores.append(mortgage.credit_score)
            total_risk_score += risk_score
        
        # adjust total_risk_score based on average credit scrore
        avg_credit_score = sum(credit_scores) / len(credit_scores)
        if avg_credit_score >= 700:
            total_risk_score -= 1
        if avg_credit_score < 650:
            total_risk_score += 1
        
        if total_risk_score <= 2:
            return process_credit_rating_response(credit_rating='AAA')
        if total_risk_score >= 3 and total_risk_score <= 5:
            return process_credit_rating_response(credit_rating='BBB')
        if total_risk_score > 5:
            return process_credit_rating_response(credit_rating='C')
        
    except ValidationError as e:
        errors = {error["loc"][0]: error["msg"] for error in e.errors()}
        return process_error_response(title="Invalid input", errors = errors)
    except Exception as e:
        return process_error_response(title="Unexecpected error", errors = e)