import hashlib
import os


class SHA256PasswordHasher:
    salt = os.urandom(16)
    iterations = 100000
    key_length = 32
    hash_function = hashlib.sha256
    def __init__(self):
        pass

    def encode(self, password):
        assert password is not None
        password = password.encode("utf-8")
        hashed_password = hashlib.pbkdf2_hmac(
            "sha256", # Use the name of the hash function as the digest module
            password,
            self.salt,
            self.iterations,
            self.key_length
        )

        return hashed_password

    def verify(self, password, enCryptPassword):
        assert password is not None and enCryptPassword is not None

        user_password = password.encode("utf-8")
        stored_password = enCryptPassword

        salt, hashed_password = stored_password.split("$")
        salt_bytes = bytes.fromhex(salt)
        hashed_password_bytes = bytes.fromhex(hashed_password)

        password_attempt = hashlib.pbkdf2_hmac(
            self.hash_function.__name__,
            user_password,
            salt_bytes,
            self.iterations,
            self.key_length
        )

        # if password_attempt == hashed_password_bytes:
        #     print("Password is correct!")
        # else:
        #     print("Password is incorrect.")
        return password_attempt == hashed_password_bytes

    def safe_summary(self, encoded):
        return {
            'algorithm': 'sha256',
            'hash': encoded,
        }
