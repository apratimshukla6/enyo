from enyo.enyodecryption import EnyoDecryption

# Third parameter is an optional integer for partition (by default 2), the fourth parameter is optional Boolean for transposition (default False)
test = EnyoDecryption("SaSQpN", "secretkey", partition=2, transposition=True)

# To print the decrypted text
print(test.decrypted)