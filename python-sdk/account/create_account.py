from algosdk import account, mnemonic


def generate_algorand_keypair():
  private_key, address = account.generate_account()
  print(f'My address: {address}')
  print(f'My private key: {private_key}')
  print(f'My passphrase: {mnemonic.from_private_key(private_key)}')

  f = open('acc.txt', 'a')
  f.write('\n')
  f.write(f'{mnemonic.from_private_key(private_key)}')
  f.close()
