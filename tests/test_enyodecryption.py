from enyo.enyodecryption import EnyoDecryption

# Third parameter is optional partition (by default 2)
test = EnyoDecryption("SaSQpN","secretkey")
# To print the decrypted text
print(test.decrypted)