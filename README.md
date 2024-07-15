![Static Badge](https://img.shields.io/badge/python-%233776ab?logo=python&logoColor=white)

# Wallet Eligibility Checker

## **Description**
**This Python script checks the eligibility of a wallet address against a list stored in a JSON file.**
<br>It verifies if the provided address exists in the list and returns the corresponding allocation amount if eligible.
<br>This code was created to verify my eligibility for an airdrop from the crypto project [NOIS](https://x.com/NoisRNG/status/1745415267747008765).

## **Features**
- **Eligibility Check** : Verifies if a wallet address exists in the eligibility list.
- **JSON Data Storage** : Reads the list of eligible wallet addresses and their allocation amounts from a JSON file.
- **Allocation Amount** : Returns the allocation amount if the wallet address is eligible.

## **Prerequisites**
- **Python 3.x** installed on your machine

## **Installation Instructions**
Make sure you have [Python](https://www.python.org/downloads/) installed on your system before running the script.

1. Clone this repository to your machine.
   
   ```bash
   git clone https://github.com/0x414854/Eligibility_Checker.git

2. Navigate to the repository directory.

   ```bash
   cd Eligibility_Checker
  
3. Run the script!

   ```bash
   python3 eligibility_checker.py

## **Usage Examples**

1.  When prompted, enter your wallet address (format: **inj1...7yrcpx**).

2. The script will read the wallet addresses from the JSON file and check if your wallet address is eligible, printing the results.

## **Tree Directory**

Eligibility_Checker/
<br>├── eligibility_checker.py
<br>├── wallets.json
<br>└── README.md

## **License**
This project is licensed under the **MIT License**.

## **Author**
[**0x414854**](https://github.com/0x414854)
