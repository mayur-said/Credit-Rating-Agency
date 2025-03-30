# Python Developer - Credit Rating Agency - Residential Mortgage Securities (RMBS) Assignment

## Prerequisite
Python version: 3.11
## Installation
1. Obtain the URL to the GitHub repository and clone it
```bash
git clone git@github.com:mayur-said/Credit-Rating-Agency.git
cd Credit-Rating-Agency
```
2. Create and activate a virtual environment
```bash
python -m venv myenv
.\myenv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r .\requirements.txt
```

## Run the code
```bash
python main.py --payload payload
```
You can provide three different payload choices -payload, error_payload, and missing_payload- to run three different scenarios.

## Test the code
```bash
python .\test_credit_rating.py
```
The code tests for all possible edge cases and invalid inputs that I was able to identify within the given time constraints.

## Design Decisions
The code largely follows the required solution structure. I have taken the liberty to modify and enhance the output slightly. Instead of just returning a string, the code returns a Python dictionary as follows:
1. if the input is valid:
   ```json
   response = {"error": False, "message": {'credit_rating': 'AAA'}}
   ```
2. if the input is invalid or for some unexpected errors:
   ```json
   response = {"error": True, "message": {"title": title, "details": errors}}
   ```
   You can provide different payload choices to check different responses.
## Questions:
1. **Performance Optimization**: How would you optimize the solution for handling a large number of mortgages or a large dataset?  
    1. Designing a solution to handle a large dataset depends on the requirements and infrastructure of the project. I feel for a mid-size dataset, the given solution should be more than enough.  
    2. If the solution doesn't match the requirements or data load, I would first investigate and identify the bottleneck. Once the bottleneck is identified, we should optimize the solution accordingly.  

2. **Error Handling**: How would you improve error handling in case of invalid input or internal errors?  
    1. I have implemented one of the best solutions using Pydantic for handling invalid input. The code handles all the scenarios given in the assignment and gives back a detailed error response to the user.  
    2. For internal errors, the code returns the following response with a detailed error message:  
        ```json
        {"error": true, "message": {"title": "Unexpected error", "details": errors}}
        ```
