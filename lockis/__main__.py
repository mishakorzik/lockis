from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.padding import PKCS7
import base64, struct, time, os

def gkey():
    return base64.urlsafe_b64encode(os.urandom(96))

class lockis:
    def __init__(self, key: bytes):
        key = base64.urlsafe_b64decode(key)

        self.encryption_key = key[:32]
        self.hmac_key = key[32:96]

        self.block_size = 128
        self.version = b'\x10'

    def encrypt(self, data: bytes) -> bytes:
        timestamp = struct.pack(">Q", int(time.time()))
        iv = os.urandom(16)

        padder = PKCS7(self.block_size).padder()
        padded_data = padder.update(data) + padder.finalize()

        cipher = Cipher(algorithms.AES(self.encryption_key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()

        message = self.version + timestamp + iv + ciphertext

        h = hmac.HMAC(self.hmac_key, hashes.SHA512())
        h.update(message)
        mac = h.finalize()
        return base64.urlsafe_b64encode(message + mac)

    def decrypt(self, token: bytes, ttl: int = None) -> bytes:
        decoded = base64.urlsafe_b64decode(token)
        if decoded[0:1] != self.version:
            raise ValueError("Unsupported version")

        timestamp = struct.unpack(">Q", decoded[1:9])[0]
        iv = decoded[9:25]
        ciphertext = decoded[25:-64]
        mac = decoded[-64:]

        h = hmac.HMAC(self.hmac_key, hashes.SHA512())
        h.update(decoded[:-64])
        h.verify(mac)

        if ttl is not None and time.time() - timestamp > ttl:
            raise ValueError("Token has expired")

        cipher = Cipher(algorithms.AES(self.encryption_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()

        unpadder = PKCS7(self.block_size).unpadder()
        return unpadder.update(padded_data) + unpadder.finalize()
