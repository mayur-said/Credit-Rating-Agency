import os
import argparse

from utils import read_json_file
from credit_rating import calculate_credit_rating
CWD = os.getcwd()

parser = argparse.ArgumentParser()
parser.add_argument(
    "--payload", 
    type=str, 
    choices=['payload', 'error_payload', 'missing_payload'],
    default="payload", 
    help="Name of input payload"
    )
args = parser.parse_args()


if __name__ == '__main__':
    payload_path = CWD + f'/{args.payload}.json'
    payload = read_json_file(payload_path)

    mortgages = payload.get('mortgages')
    if mortgages:
        result = calculate_credit_rating(mortgages)
        print(result)