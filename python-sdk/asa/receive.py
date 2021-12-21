from algosdk.future.transaction import AssetTransferTxn
from algosdk.v2client.algod import AlgodClient

from utils import algod_token, algod_address, wait_for_confirmation


def receiving_asset(receiver, asset_id):
  """
  Before an account can receive a specific asset it must opt-in to receive it. 
  An opt-in transaction places an asset holding of 0 into the account and 
  increases its minimum balance by 100,000 microAlgos. 
  An opt-in transaction is simply an asset transfer with an amount of 0, 
  both to and from the account opting in. 
  """
  algod_client = AlgodClient(algod_token, algod_address)
  params = algod_client.suggested_params()
  params.fee = 1000
  params.flat_fee = True

  account_info = algod_client.account_info(receiver)
  holding = None
  
  for scrutinized_asset in account_info['assets']:
    if (scrutinized_asset['asset-id'] == asset_id):
      holding = True
      break

  if not holding:
    # Use the AssetTransferTxn class to transfer assets and opt-in
    txn = AssetTransferTxn(
      sender=receiver,
      sp=params,
      receiver=receiver,
      amt=0,
      index=asset_id
    )
    
    stxn = txn.sign(receiver['sk'])
    txid = algod_client.send_transaction(stxn)
    print(txid)

    wait_for_confirmation(algod_client, txid) 
