from json import dumps
from base64 import b64decode
from algosdk.v2client.algod import AlgodClient
from algosdk.future.transaction import PaymentTxn
from algosdk.util import algos_to_microalgos

from utils import wait_for_confirmation, algod_token, algod_address


def make_transaction(private_key, from_add, to_add, amount, note):
  algod_client = AlgodClient(algod_token, algod_address)
  params = algod_client.suggested_params()
  params.flat_fee = True
  params.fee = algos_to_microalgos(0.001)
  amount = algos_to_microalgos(float(amount))
  note = note.encode()

  unsigned_txn = PaymentTxn(from_add, params, to_add, amount, None, note)

  signed_txn = unsigned_txn.sign(private_key)

  #submit transaction
  txid = algod_client.send_transaction(signed_txn)
  print(f"Successfully sent transaction with txID: {txid}")

  try:
    confirmed_txn = wait_for_confirmation(algod_client, txid)  
  except Exception as err:
    print(err)
    return

  print(f"Transaction information: {dumps(confirmed_txn, indent=4)}")
  print(f"Decoded note: {b64decode(confirmed_txn['txn']['txn']['note']).decode()}")
