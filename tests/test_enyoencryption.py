from enyo.enyoencryption import EnyoEncryption

# Third parameter is optional partition (by default 2)
test = EnyoEncryption("test","secretkey")
# To print the encrypted text
print(test.encrypted)