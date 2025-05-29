from typing import Any

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from encryptor import decrypt_sym_key
from utility_functions import *


def decrypt_file(config: dict[str, Any]) -> None:
    """Decrypt the ciphertext file using 3DES and save the plaintext."""
    print("Decrypting symmetric key...")
    sym_key = decrypt_sym_key(config["private_key_path"], config["encrypted_sym_key_path"])

    print("Decrypting data with 3DES...")
    with open(config["input_file"], "rb") as f:
        ciphertext: bytes = f.read()

    cipher = Cipher(algorithms.TripleDES(sym_key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    plaintext = unpad(padded_plaintext)

    with open(config["output_file"], "wb") as f:
        f.write(plaintext)

    print("Data has been decrypted successfully.")
