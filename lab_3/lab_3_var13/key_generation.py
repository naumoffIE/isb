import base64
from os import urandom

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


class KeyGenerator:
    def __init__(self, sym_key_length: int, priv_key_path: str, pub_key_path: str, encrypted_key_path: str):
        self.sym_key_length = sym_key_length
        self.priv_key_path = priv_key_path
        self.pub_key_path = pub_key_path
        self.encrypted_key_path = encrypted_key_path

    def generate_3des_key(self) -> bytes:
        """Generate a 3DES key of the specified byte length (8, 16, or 24)."""
        if self.sym_key_length not in (8, 16, 24):
            raise ValueError("Invalid 3DES key length. Must be 8, 16, or 24 bytes.")
        return urandom(self.sym_key_length)

    def generate(self) -> None:
        """Generate RSA key pair and encrypt 3DES key with the public key."""
        print("Generating RSA and 3DES keys...")

        sym_key = self.generate_3des_key()

        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()

        with open(self.priv_key_path, "wb") as f:
            f.write(private_key.private_bytes(
                serialization.Encoding.PEM,
                serialization.PrivateFormat.PKCS8,
                serialization.NoEncryption()
            ))

        with open(self.pub_key_path, "wb") as f:
            f.write(public_key.public_bytes(
                serialization.Encoding.PEM,
                serialization.PublicFormat.SubjectPublicKeyInfo
            ))

        encrypted_key = public_key.encrypt(
            sym_key,
            padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )

        # Save as base64 to a .txt file
        with open(self.encrypted_key_path, "w") as f:
            f.write(base64.b64encode(encrypted_key).decode())

        print("Keys have been generated and saved successfully.")
