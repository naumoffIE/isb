from typing import Any

from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from utility_functions import *


def decrypt_sym_key(private_key_path: str, encrypted_sym_key_path: str) -> bytes:
    """Decrypt the symmetric key using the RSA private key."""
    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    with open(encrypted_sym_key_path, "rb") as f:
        encrypted_key = f.read()

    return private_key.decrypt(
        encrypted_key,
        padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )


def encrypt_file(config: dict[str, Any]) -> None:
    """Encrypt the input file using 3DES and save the ciphertext."""
    print("Decrypting symmetric key...")
    sym_key = decrypt_sym_key(config["private_key_path"], config["encrypted_sym_key_path"])

    print("Encrypting data with 3DES...")
    with open(config["input_file"], "rb") as f:
        plaintext: bytes = f.read()

    padded = pad(plaintext)
    cipher = Cipher(algorithms.TripleDES(sym_key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded) + encryptor.finalize()

    with open(config["output_file"], "wb") as f:
        f.write(ciphertext)

    print("Data has been encrypted successfully.")
