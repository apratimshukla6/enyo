<div align="center">
  <br />
  <p>
    <a href="https://pypi.org/project/enyo/"><img src="https://i.imgur.com/ZARmmn0.png" width="500" alt="enyo" /></a>
  </p>
  <br />
  <p>
    <a href="https://pypi.org/project/enyo/"><img src="https://badge.fury.io/py/enyo.svg" alt="PyPi version" /></a>
    <a href="https://github.com/apratimshukla6/enyo/actions"><img src="https://github.com/apratimshukla6/enyo/actions/workflows/python-package.yml/badge.svg" alt="Python Package Test" /></a>
    <a href="https://pypi.org/project/enyo/"><img src="https://img.shields.io/pypi/format/enyo" alt="format" /></a>
    <a href="https://github.com/apratimshukla6/enyo/blob/master/LICENSE"><img src="https://img.shields.io/github/license/apratimshukla6/enyo?color=red" alt="LICENSE" /></a>
    <a href="https://pepy.tech/project/enyo"><img src="https://pepy.tech/badge/enyo" alt="Downloads" /></a>
    <a href="https://pepy.tech/project/enyo"><img src="https://pepy.tech/badge/enyo/week" alt="Downloads/week" /></a>
    <a href="https://github.com/apratimshukla6/enyo/issues"><img src="https://camo.githubusercontent.com/f5054ffcd4245c10d3ec85ef059e07aacf787b560f83ad4aec2236364437d097/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f6e747269627574696f6e732d77656c636f6d652d627269676874677265656e2e7376673f7374796c653d666c6174" alt="Contributions" /></a>
  </p>
</div>

## About

[Enyo](https://link.springer.com/chapter/10.1007/978-981-16-1089-9_32) is a lightweight multistage partition-based encryption algorithm. Enyo cipher demonstrates good resistance to a brute-force attack. It is well suited for small-scale applications where the computational power is a bottleneck.

- Combines the performance of primitive ciphers with enhanced security
- Custom encoding ensures URL safe encryption
- Transposition stage for additional security

## Modules

- `enyoencryption` - Enyo Encryption module
- `enyodecryption` - Enyo Decryption module

## Installation

**Python3 is required.**  

Open `terminal` and execute:
```shell
pip install enyo
```

## Development Installation
Open `terminal` and execute:
```shell
git clone https://github.com/apratimshukla6/enyo.git
cd enyo
pip install --editable .
```

## Example Usage

#### Encryption

```python
from enyo.enyoencryption import EnyoEncryption
# Third parameter is an optional integer for partition (by default 2), the fourth parameter is optional Boolean for transposition (default False)
test = EnyoEncryption("test", "secretkey", partition=2, transposition=True)

# To print the encrypted text
print(test.encrypted)
```
##### Output

```python
SaSQpN
```

#### Decryption

```python
from enyo.enyodecryption import EnyoDecryption
# Third parameter is an optional integer for partition (by default 2), the fourth parameter is optional Boolean for transposition (default False)
test = EnyoDecryption("SaSQpN", "secretkey", partition=2, transposition=True)

# To print the decrypted text
print(test.decrypted)
```

##### Output

```python
test
```

## Links

- [Research Paper](https://link.springer.com/chapter/10.1007/978-981-16-1089-9_32)
- [Demo](https://enyo.owaspvit.com)

## Contributing

Before creating an issue, please ensure that it hasn't already been reported/suggested.

The issue tracker is only for bug reports and enhancement suggestions. If you have a question, please ask it in the [Discord server](https://discord.gg/aMgWPApkyS) instead of opening an issue – you will get redirected there anyway.

If you wish to contribute to the Enyo codebase or documentation, feel free to fork the repository and submit a pull request.

## Help 

If you don't understand something in the documentation, you are experiencing problems, or you just need a gentle
nudge in the right direction, please don't hesitate to join our [Discord Server](https://discord.gg/aMgWPApkyS).
