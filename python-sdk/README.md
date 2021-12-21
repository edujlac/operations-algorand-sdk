
When ```generate_algorand_keypair()``` is invoked the mnemonic generated is saved in ```acc.txt``` so it can be invoked from ```utils```

### Structure of accounts
```
  {0: 
    {
      'pk': 'Public address', 
      'sk': 'Private key'
    }
  }
```

### Calling the first account
```
  from utils import accounts
  
  print(f'Address: {accounts[0]['pk']}')
  print(f'Private key: {accounts[0]['sk']}')
```