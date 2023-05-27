import json
from eth_keys import keys
from os import urandom
import os

if os.path.exists("wallets.json"):
    os.remove("wallets.json")

wallets = []

for _ in range(1000):
    private_key_bytes = urandom(32)
    private_key = keys.PrivateKey(private_key_bytes)

    address = private_key.public_key.to_checksum_address()
    public_key = private_key.public_key.to_hex()
    private_key = private_key.to_hex()

    print("Address: ", address)
    print("Public Key: ", public_key)
    print("Private Key: ", private_key)

    wallet = {
        "address": address,
        "public_key": public_key,
        "private_key": private_key
    }
    wallets.append(wallet)

with open("wallets.json", "w") as file:
    json.dump(wallets, file, indent=4)

print("Wallets have been generated and saved to wallets.json")
