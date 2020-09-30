Enyo is a lightweight multistage partition based encryption algorithm

# Description
    
It consists of two main modules:

- `enyoencryption`: Enyo Encryption algorithm module
- `enyodecryption`: Enyo Decryption algorithm module

# Usage
    
## To encrypt:
```python
from enyo.enyoencryption import EnyoEncryption
# Third parameter is optional partition (by default 2)
test = EnyoEncryption("test","secretkey")
# To print the encrypted text
print(test.encrypted)
```

## To decrypt:
```python
from enyo.enyodecryption import EnyoDecryption
# Third parameter is optional partition (by default 2)
test = EnyoDecryption("SaSQpN","secretkey")
# To print the decrypted text
print(test.decrypted)
```

# Installation
 
## Normal installation

```bash
pip install enyo
```

## Development installation

```bash
git clone https://github.com/apratimshukla6/enyo.git
cd enyo
pip install --editable .
```