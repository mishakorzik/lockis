# Lockis

Easily encrypt your sensitive data with double aes256+hmac and with ttl.

```
# import the module
import lockis

# generate secret key (128 bytes)
key = lockis.gkey()

# initilize secret key
key = lockis.lockis(key)

# encrypt message
key.encrypt()

# decrypt message with ttl 10 seconds
key.decrypt(data, ttl=10)
```

You can also specify ttl, this will help protect against replay attacks.

```python
>>> import lockis
>>> key = lockis.gkey()
>>> key = lockis.lockis(key)
>>> key.encrypt(b"hello everyone, its a test message!")
b'EAAAAABnhh92pdLhypQcEsvwh4YUMuwzNg8RiQE2pJLnkT9Ru8tUSXvN6XGi3eeO1q-OiLD_E66pCpymr8Jw_BtrXB6Q1i9SeHe3l-NiCvGRZD2WOEmzjjH7MnyO7Haiw-hHdvs8SFZJgpssxR_tLAEvRaDcV9scC7Gfd2kwmdsok8wrRNvlpkE='
>>> key.decrypt(b'EAAAAABnhh92pdLhypQcEsvwh4YUMuwzNg8RiQE2pJLnkT9Ru8tUSXvN6XGi3eeO1q-OiLD_E66pCpymr8Jw_BtrXB6Q1i9SeHe3l-NiCvGRZD2WOEmzjjH7MnyO7Haiw-hHdvs8SFZJgpssxR_tLAEvRaDcV9scC7Gfd2kwmdsok8wrRNvlpkE=', ttl=60)
hello everyone, its a test message!
```

---

how to show the current version of installed lockis

```python
lockis.version()
```
