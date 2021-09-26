from enyo.enyoencryption import EnyoEncryption

# Third parameter is an optional integer for partition (by default 2), the fourth parameter is optional Boolean for transposition (default False)
test = EnyoEncryption("test", "secretkey", partition=2, transposition=True)

# To print the encrypted text
print(test.encrypted)
