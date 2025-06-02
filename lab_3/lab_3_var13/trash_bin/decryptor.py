from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

import base64
from utility_functions import unpad
from work_with_files import read_file


class Decryptor:
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

    def decrypt(self, input_file: str, output_file: str) -> None:
        """Decrypt the file using 3DES and save the plaintext."""
        print("Decrypting symmetric key...")
        key = self._load_symmetric_key()

        print("Decrypting data with 3DES...")
        ciphertext = read_file(input_file)

        cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), backend=default_backend())
        decryptor = cipher.decryptor()
        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        plaintext = unpad(padded_plaintext)

        with open(output_file, "wb") as f:
            f.write(plaintext)

        print("Data has been decrypted successfully.")
