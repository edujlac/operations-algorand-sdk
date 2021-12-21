from algosdk.future.transaction import AssetTransferTxn
from algosdk.util import algos_to_microalgos
from algosdk.v2client.algod import AlgodClient

from utils import algod_token, algod_address, wait_for_confirmation


def transferring_asset(sender, receiver, asset_id, amount):
  """
  Authorized by: The account that holds the asset to be transferred.
  Assets can be transferred between accounts that have opted-in to receiving the asset. 
  These are analogous to standard payment transactions but for Algorand Standard Assets.
  """
  algod_client = AlgodClient(algod_token, algod_address)
  params = algod_client.suggested_params()
  params.fee = 1000
  params.flat_fee = True

  txn = AssetTransferTxn(
    sender=sender['pk'],
    sp=params,
    receiver=receiver['pk'],
    amt=algos_to_microalgos(amount),
    index=asset_id
  )

  stxn = txn.sign(sender['sk'])
  txid = algod_client.send_transaction(stxn)
  print(txid)

  wait_for_confirmation(algod_client, txid)
