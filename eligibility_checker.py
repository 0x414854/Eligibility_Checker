import json
import os

"""
This script checks the eligibility of a wallet address against a list stored in a 
JSON file. 
It verifies if the provided address exists in the list and returns the corresponding 
allocation amount if eligible.
"""

def check_eligibility(wallet_address, json_file_path):
    json_file_path = os.path.abspath(json_file_path)

    with open(json_file_path, 'r') as file:
        addresses_data = json.load(file)
    
    for item in addresses_data:
        if item['address'] == wallet_address:
            return True, item['amount']
    
    return False, None

if __name__ == "__main__":
    json_file_path = './wallets.json'
    wallet_to_check = input("Enter your Wallet address (inj1...7yrcpx) : ")
    
    is_eligible, allocation_amount = check_eligibility(wallet_to_check, json_file_path)
    
    if is_eligible:
        print(f"The person with address {wallet_to_check} is eligible with an allocation of {allocation_amount} unois ({allocation_amount/ 1000000} $NOIS).")
    else:
        print(f"The person with address {wallet_to_check} is not eligible.")
