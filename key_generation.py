from typing import Any

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

from utility_functions import *


def generate_keys(config: dict[str, Any]) -> None:
    """Generate RSA key pair and encrypt 3DES key with the public key."""
    print("Generating RSA and 3DES keys...")

    sym_key: bytes = generate_3des_key(config["sym_key_length"])

    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    with open(config["private_key_path"], "wb") as f:
        f.write(private_key.private_bytes(
            serialization.Encoding.PEM,
            serialization.PrivateFormat.PKCS8,
            serialization.NoEncryption()
        ))

    with open(config["public_key_path"], "wb") as f:
        f.write(public_key.public_bytes(
            serialization.Encoding.PEM,
            serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    encrypted_sym_key: bytes = public_key.encrypt(
        sym_key,
        padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )

    with open(config["encrypted_sym_key_path"], "wb") as f:
        f.write(encrypted_sym_key)

    print("Keys have been generated and saved successfully.")
