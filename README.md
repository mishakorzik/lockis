## Lockis

Easily encrypt your sensitive data with aes256+hmac and with ttl.

## Installing

```
pip install lockis
```

## Usage

Here are examples of using the lockis module

```
# generate secret key (96 bytes)
key = gkey()

# initilize secret key
key = lockis(key)

# encrypt message
key.encrypt()

# decrypt message
key.decrypt(data, ttl=10)
```

You can also specify ttl, this will help protect against replay attacks.

```python
>>> from lockis import gkey, lockis
>>> key = gkey()
>>> key = lockis(key)
>>> key.encrypt(b"hello everyone, its a test message!")
b'EAAAAABnhh92pdLhypQcEsvwh4YUMuwzNg8RiQE2pJLnkT9Ru8tUSXvN6XGi3eeO1q-OiLD_E66pCpymr8Jw_BtrXB6Q1i9SeHe3l-NiCvGRZD2WOEmzjjH7MnyO7Haiw-hHdvs8SFZJgpssxR_tLAEvRaDcV9scC7Gfd2kwmdsok8wrRNvlpkE='
>>> key.decrypt(b'EAAAAABnhh92pdLhypQcEsvwh4YUMuwzNg8RiQE2pJLnkT9Ru8tUSXvN6XGi3eeO1q-OiLD_E66pCpymr8Jw_BtrXB6Q1i9SeHe3l-NiCvGRZD2WOEmzjjH7MnyO7Haiw-hHdvs8SFZJgpssxR_tLAEvRaDcV9scC7Gfd2kwmdsok8wrRNvlpkE=', ttl=60)
hello everyone, its a test message!
```
