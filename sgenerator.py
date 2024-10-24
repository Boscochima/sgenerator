import random
from web3 import Web3

# Connect to an Ethereum node using Infura (or any other provider)
INFURA_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

def generate_random_address():
    """
    Generate a random Ethereum address by generating a random private key
    and deriving the public address.
    """
    private_key = hex(random.getrandbits(256))[2:].zfill(64)
    account = web3.eth.account.from_key(private_key)
    return account.address

def check_balance(address):
    """
    Check the ETH balance of a given Ethereum address.
    """
    balance_wei = web3.eth.get_balance(address)
    balance_eth = web3.fromWei(balance_wei, 'ether')
    return balance_eth

def find_wallet_with_balance():
    """
    Generate random Ethereum addresses and check for balance.
    """
    attempts = 0
    while True:
        attempts += 1
        random_address = generate_random_address()
        balance = check_balance(random_address)

        print(f"Attempt {attempts}: Address {random_address}, Balance {balance} ETH")

        # If the balance is greater than 0, return the address
        if balance > 0:
            print(f"Wallet with balance found!\nAddress: {random_address}\nBalance: {balance} ETH")
            break

if __name__ == "__main__":
    find_wallet_with_balance()
