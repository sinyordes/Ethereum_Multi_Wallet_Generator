# Ethereum Wallet Generator

This simple Python program allows you to generate Ethereum wallets. You can obtain the address, public key, and private key for each wallet.

## Dependencies

- `eth_keys`
- `eth_utils`

To install the required dependencies, you can use the following command:

```bash 
pip install eth-keys eth-utils
```

## Usage

1. Download the `eth_wallet.py` file and save it to your execution environment.
2. Open a terminal or command prompt and navigate to the directory where your execution environment is located.
3. Run the following command to start the program:

```bash
python eth_wallet.py
```


4. The program will generate 10 Ethereum wallets and print the results to the console.
5. A file named `wallets.json` will be created in the same directory. This file contains the information of the generated wallets.

## Notes

- Each time the program is executed, new wallets will be generated, and the existing `wallets.json` file will be overwritten.
- The generated wallet information is only printed to the console and should be stored securely.
- This program is for development purposes only. For real-world use, private keys should be securely stored and handled.

