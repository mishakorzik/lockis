from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.padding import PKCS7
import base64, struct, time, os

def version():
    return "1.0.1"

def gkey():
    return base64.urlsafe_b64encode(os.urandom(128))

class lockis:
    def __init__(self, key: bytes):
        key = base64.urlsafe_b64decode(key)
        if len(key) != 128:
            raise ValueError("Invalid key length. Expected 128 bytes")

        self.encryption_key_1 = key[:32]
        self.encryption_key_2 = key[32:64]
        self.hmac_key = key[64:128]

        self.block_size = 128
        self.version = b'\x10'

    def encrypt(self, data) -> bytes:
        if isinstance(data, (bytes, str)):
            raise TypeError("Data must by bytes or str")
        if isinstance(data, str):
            data = data.encode('utf-8')

        timestamp = struct.pack(">Q", int(time.time()))
        while True:
            iv1 = os.urandom(16)
            iv2 = os.urandom(16)
            if iv1 != iv2:
                break

        padder = PKCS7(self.block_size).padder()
        padded_data = padder.update(data) + padder.finalize()

        cipher1 = Cipher(algorithms.AES(self.encryption_key_1), modes.CBC(iv1))
        encryptor1 = cipher1.encryptor()
        ciphertext1 = encryptor1.update(padded_data) + encryptor1.finalize()

        cipher2 = Cipher(algorithms.AES(self.encryption_key_2), modes.CBC(iv2))
        encryptor2 = cipher2.encryptor()
        ciphertext2 = encryptor2.update(ciphertext1) + encryptor2.finalize()

        message = self.version + timestamp + iv1 + iv2 + ciphertext2
        h = hmac.HMAC(self.hmac_key, hashes.SHA512())
        h.update(message)
        mac = h.finalize()

        return base64.urlsafe_b64encode(message + mac)

    def decrypt(self, token: bytes, ttl: int = None) -> bytes:
        try:
            decoded = base64.urlsafe_b64decode(token)
            if decoded[0:1] != self.version:
                raise ValueError("Unsupported version")

            timestamp = struct.unpack(">Q", decoded[1:9])[0]
            iv1 = decoded[9:25]
            iv2 = decoded[25:41]
            ciphertext2 = decoded[41:-64]
            mac = decoded[-64:]

            h = hmac.HMAC(self.hmac_key, hashes.SHA512())
            h.update(decoded[:-64])
            h.verify(mac)

            if ttl is not None and time.time() - timestamp > ttl:
                raise ValueError("Token has expired")

            cipher2 = Cipher(algorithms.AES(self.encryption_key_2), modes.CBC(iv2))
            decryptor2 = cipher2.decryptor()
            ciphertext1 = decryptor2.update(ciphertext2) + decryptor2.finalize()

            cipher1 = Cipher(algorithms.AES(self.encryption_key_1), modes.CBC(iv1))
            decryptor1 = cipher1.decryptor()
            padded_data = decryptor1.update(ciphertext1) + decryptor1.finalize()

            unpadder = PKCS7(self.block_size).unpadder()
            return unpadder.update(padded_data) + unpadder.finalize()
        except Exception:
            raise ValueError("Decryption failed")
