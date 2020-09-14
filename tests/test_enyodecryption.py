from enyo.enyoencryption import EnyoDecryption

# Third parameter is optional partition (by default 2)
test = EnyoDecryption("SQpaSN","secretkey")
# To print the decrypted text
print(test.decrypted)