from enyo.enyodecryption import EnyoDecryption

# Third parameter is optional partition (by default 2), Fourth parameter is optional boolean transposition (default False)
test = EnyoDecryption("SaSQpN","secretkey",partition=2,transposition=True)
# To print the decrypted text
print(test.decrypted)