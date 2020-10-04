[![PyPI version](https://badge.fury.io/py/enyo.svg)](https://pypi.org/project/enyo/) [![Downloads](https://pepy.tech/badge/enyo)](https://pepy.tech/project/enyo) [![Downloads](https://pepy.tech/badge/enyo/week)](https://pepy.tech/project/enyo/week) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/apratimshukla6/enyo/issues)

Enyo is a lightweight multistage partition based encryption algorithm

# Description
    
It consists of two main modules:

- `enyoencryption`: Enyo Encryption algorithm module
- `enyodecryption`: Enyo Decryption algorithm module

# Usage
    
## To encrypt:
```python
from enyo.enyoencryption import EnyoEncryption
# Third parameter is optional partition (by default 2), Fourth parameter is optional boolean transposition (default False)
test = EnyoEncryption("test","secretkey",partition=2,transposition=True)
# To print the encrypted text
print(test.encrypted)
```

## To decrypt:
```python
from enyo.enyodecryption import EnyoDecryption
# Third parameter is optional partition (by default 2), Fourth parameter is optional boolean transposition (default False)
test = EnyoDecryption("SaSQpN","secretkey",partition=2,transposition=True)
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
