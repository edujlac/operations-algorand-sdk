from algosdk.mnemonic import to_public_key, to_private_key
from algosdk.v2client.algod import AlgodClient

algod_address = "http://localhost:4001"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
accounts = {}

if len(accounts) == 0:
  counter = 0
  with open('acc.txt', 'r') as f:
    for mnemonic in f.readlines():
      accounts[counter] = {}
      accounts[counter]['pk'] = to_public_key(mnemonic)
      accounts[counter]['sk'] = to_private_key(mnemonic)
      counter += 1

def wait_for_confirmation(client: AlgodClient, txid: str, timeout: int = 0):
  """
  Wait until the transaction is confirmed or rejected, or until 'timeout'
  number of rounds have passed.
  Args:
      txid (str): the transaction to wait for
      timeout (int): maximum number of rounds to wait    
  Returns:
        dict: pending transaction information, or throws an error if the transaction
            is not confirmed or rejected in the next timeout rounds
  """
  if timeout > 0:
    start_round = client.status()["last-round"] + 1
    current_round = start_round

    while current_round < start_round + timeout:
      try:
        pending_txn = client.pending_transaction_info(txid)
      except Exception:
        return

      if pending_txn.get("confirmed-round", 0) > 0:
        return pending_txn
      elif pending_txn["pool-error"]:  
        raise Exception(f'pool error: {pending_txn["pool-error"]}')

      client.status_after_block(current_round)                   
      current_round += 1

      raise Exception(f'pending tx not found in timeout rounds, timeout value = : {timeout}')
  else:
    last_round = client.status().get('last-round')
    txinfo = client.pending_transaction_info(txid)

    while not (txinfo.get('confirmed-round') and txinfo.get('confirmed-round') > 0):
        print("Waiting for confirmation")
        last_round += 1
        client.status_after_block(last_round)
        txinfo = client.pending_transaction_info(txid)

    print("Transaction {} confirmed in round {}.".format(txid, txinfo.get('confirmed-round')))
    
    return txinfo
