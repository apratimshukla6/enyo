from enyo.enyoencryption import EnyoEncryption

# Third parameter is optional partition (by default 2), Fourth parameter is optional boolean transposition (default False)
test = EnyoEncryption("test","secretkey",partition=2,transposition=True)
# To print the encrypted text
print(test.encrypted)