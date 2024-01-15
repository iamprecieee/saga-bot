from web3 import Web3
import time
import os
from dotenv import load_dotenv


load_dotenv()

dragonstone_rpc_url = 'https://dragonstone-2705349341270000-1.jsonrpc.testnet-sp1.sagarpc.io' # Update to your network's rpc url
web3 = Web3(Web3.HTTPProvider(dragonstone_rpc_url))

# Check if the connection is successful
if not web3.is_connected():
    print("Failed to connect to Dragonstone Saga network")
    exit()

# Sender and receiver details
sender_address = os.getenv("ADDRESS_MAIN")

receiver_addresses = [os.getenv("ADDRESS_1"),
                    os.getenv("ADDRESS_2"),
                    os.getenv("ADDRESS_3"),
                    os.getenv("ADDRESS_4")
                    ]

private_key = os.getenv("PRIVATE_KEY")
amount = web3.to_wei(0.01, 'ether') # Amount to send in ETH
gas = 21000 # Standard gas limit for ETH transfer
gas_price = web3.eth.gas_price # Get current gas price
chain_id = 2705349341270000 # Update to your network's chain ID

def send_transaction(receiver_address):
    nonce = web3.eth.get_transaction_count(sender_address, 'pending')  # Get the dynamic nonce
    tx = {
        'nonce': nonce,
        'to': receiver_address,
        'value': amount,
        'gas': gas,
        'gasPrice': gas_price,
        'chainId': chain_id
    }
    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f'Transaction sent to {receiver_address} with hash: {web3.to_hex(tx_hash)}')
        
if __name__ == "__main__":
    while True:
        for receiver_address in receiver_addresses:
            try:
                send_transaction(receiver_address)
                # print(f"Transaction sent to {receiver_address}. Waiting 10 seconds before sending the next one.")
                time.sleep(10)  # Wait 10 seconds before the next transaction
            except ValueError as e:
                # print("Nonce issue encountered, retrying transaction...")
                time.sleep(10)  # Wait a bit before retrying