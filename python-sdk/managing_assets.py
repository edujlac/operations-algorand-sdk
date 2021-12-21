from asa.receive import receiving_asset
from asa.transfer import transferring_asset
from utils import accounts

receiving_asset(accounts[0], 10458941)
transferring_asset(accounts[1], accounts[0], 10458941, 5)
