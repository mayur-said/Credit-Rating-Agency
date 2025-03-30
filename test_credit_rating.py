import unittest
from credit_rating import calculate_credit_rating, calculate_risk_score
from model import Mortgage
from pydantic import ValidationError


class TestCreditRating(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.AAA_payload = {
            "mortgages": [
                {
                "credit_score": 750,
                "loan_amount": 200000,
                "property_value": 250000,
                "annual_income": 60000,
                "debt_amount": 20000,
                "loan_type": "fixed",
                "property_type": "single_family"
                },
                {
                "credit_score": 680,
                "loan_amount": 150000,
                "property_value": 175000,
                "annual_income": 45000,
                "debt_amount": 10000,
                "loan_type": "adjustable",
                "property_type": "condo"
                }
                ]}
        cls.BBB_payload = {
            "mortgages": [
                {
                "credit_score": 660,
                "loan_amount": 250000,
                "property_value": 300000,
                "annual_income": 50000,
                "debt_amount": 25000,
                "loan_type": "adjustable",
                "property_type": "single_family"
                },
                {
                "credit_score": 700,
                "loan_amount": 180000,
                "property_value": 200000,
                "annual_income": 60000,
                "debt_amount": 30000,
                "loan_type": "fixed",
                "property_type": "condo"
                }]}
        cls.C_payload = {
            "mortgages": [
                {
                "credit_score": 620,
                "loan_amount": 300000,
                "property_value": 330000,
                "annual_income": 45000,
                "debt_amount": 25000,
                "loan_type": "adjustable",
                "property_type": "condo"
                },
                {
                "credit_score": 640,
                "loan_amount": 200000,
                "property_value": 250000,
                "annual_income": 40000,
                "debt_amount": 20000,
                "loan_type": "adjustable",
                "property_type": "condo"
                }]}
        
        cls.invalid_payload_1 = {
            "mortgages": [
                {
                "credit_score": 1000,
                "loan_amount": 300000,
                "property_value": 330000,
                "annual_income": 45000,
                "debt_amount": 25000,
                "loan_type": "wrong_type",
                "property_type": "wrong_type"
                }]}
        
        cls.invalid_payload_2 = {
            "mortgages": [
                {
                "loan_amount": 200000,
                "property_value": 250000,
                "annual_income": 40000,
                "debt_amount": 20000,
                "loan_type": "adjustable",
                "property_type": "condo"
                }]}
        
        cls.mortgage_1 = Mortgage(**{ 
            "credit_score": 750, 
            "loan_amount": 200000, 
            "property_value": 250000, 
            "annual_income": 60000,
            "debt_amount": 20000, 
            "loan_type": "fixed", 
            "property_type": "single_family" 
            })
        
        cls.mortgage_2 = Mortgage(**{
            "credit_score": 620,
            "loan_amount": 300000,
            "property_value": 330000,
            "annual_income": 45000,
            "debt_amount": 25000,
            "loan_type": "adjustable",
            "property_type": "condo"
            })
        
        cls.mortgage_3 = Mortgage(**{
            "credit_score": 700,
            "loan_amount": 180000,
            "property_value": 200000,
            "annual_income": 60000,
            "debt_amount": 30000,
            "loan_type": "fixed",
            "property_type": "condo"
            })
               
    
    def test_credit_rating(self):
        AAA_result = calculate_credit_rating(self.AAA_payload['mortgages'])
        BBB_result = calculate_credit_rating(self.BBB_payload['mortgages'])
        C_result = calculate_credit_rating(self.C_payload['mortgages'])
        error_result_1 = calculate_credit_rating(self.invalid_payload_1['mortgages'])
        error_result_2 = calculate_credit_rating(self.invalid_payload_2['mortgages'])

        self.assertEqual(AAA_result['error'], False)
        self.assertEqual(BBB_result['error'], False)
        self.assertEqual(C_result['error'], False)
        self.assertEqual(error_result_1['error'], True)
        self.assertEqual(error_result_2['error'], True)
        self.assertEqual(AAA_result['message']['credit_rating'], 'AAA')
        self.assertEqual(BBB_result['message']['credit_rating'], 'BBB')
        self.assertEqual(C_result['message']['credit_rating'], 'C')
        self.assertEqual(error_result_1['message']['title'], "Invalid input")
        self.assertEqual(error_result_2['message']['title'], "Invalid input")

    
    def test_calculate_risk_score(self):
        self.assertEqual(calculate_risk_score(self.mortgage_1), -2)
        self.assertEqual(calculate_risk_score(self.mortgage_2), 7)
        self.assertEqual(calculate_risk_score(self.mortgage_3), 1)
    

if __name__ == '__main__':
    unittest.main()

