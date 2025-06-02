from os import urandom

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from utility_functions import pad, unpad
from work_with_files import read_file, write_file


class SymmetricEncryptor:
    def __init__(self, key: bytes):
        self.key = key

    @staticmethod
    def generate_3des_key(length: int = 24) -> bytes:
        if length not in (8, 16, 24):
            raise ValueError("Invalid 3DES key length. Must be 8, 16, or 24 bytes.")
        return urandom(length)

    def encrypt(self, input_file: str, output_file: str) -> None:
        data = read_file(input_file)
        padded = pad(data)

        cipher = Cipher(algorithms.TripleDES(self.key), modes.ECB(), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded) + encryptor.finalize()

        write_file(output_file, ciphertext)


class SymmetricDecryptor:
    def __init__(self, key: bytes):
        self.key = key

    def decrypt(self, input_file: str, output_file: str):
        ciphertext = read_file(input_file)

        cipher = Cipher(algorithms.TripleDES(self.key), modes.ECB(), backend=default_backend())
        decryptor = cipher.decryptor()
        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

        plaintext = unpad(padded_plaintext)

        with open(output_file, "wb") as f:
            f.write(plaintext)

        print("Data has been decrypted successfully.")
