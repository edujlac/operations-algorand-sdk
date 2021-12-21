from account.create_account import generate_algorand_keypair
from account.make_transaction import make_transaction
from account.check_balance import check_balance
from utils import accounts


if check_balance(accounts[0]['pk']) > 0:
  make_transaction(accounts[0]['sk'], accounts[0]['pk'], accounts[1]['pk'], 1, "Sending 1 Algo")
else:
  print('Fund the account before making the transaction in https://dispenser.testnet.aws.algodev.network/')

# Checking account A balance
check_balance(accounts[0]['pk'])

# Checking account B balance
check_balance(accounts[1]['pk'])
