from algosdk.v2client.algod import AlgodClient
from algosdk.util import microalgos_to_algos

from utils import algod_token, algod_address


def check_balance(address) -> int:
  algod_client = AlgodClient(algod_token, algod_address)
  account_info = algod_client.account_info(address)
  amount = account_info.get('amount')
  
  print(account_info)
  print(f"Account balance: {amount} microAlgos or {microalgos_to_algos(amount)} Algos")
  return amount
