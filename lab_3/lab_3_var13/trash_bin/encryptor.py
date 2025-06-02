from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

import base64
from utility_functions import pad
from work_with_files import read_file


class Encryptor:
    def __init__(self, private_key_path: str, encrypted_key_path: str):
        self.private_key_path = private_key_path
        self.encrypted_key_path = encrypted_key_path

    def _load_symmetric_key(self) -> bytes:
        """Decrypt symmetric key from base64-encoded file."""
        with open(self.private_key_path, "rb") as f:
            private_key = serialization.load_pem_private_key(f.read(), password=None)

        with open(self.encrypted_key_path, "r") as f:
            encrypted_key_b64 = f.read()
            encrypted_key = base64.b64decode(encrypted_key_b64)

        return private_key.decrypt(
            encrypted_key,
            padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )

    def encrypt(self, input_file: str, output_file: str) -> None:
        """Encrypt the file using 3DES and save the result."""
        print("Decrypting symmetric key...")
        key = self._load_symmetric_key()

        print("Encrypting data with 3DES...")
        data = read_file(input_file)
        padded = pad(data)

        cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded) + encryptor.finalize()

        with open(output_file, "wb") as f:
            f.write(ciphertext)

        print("Data has been encrypted successfully.")
