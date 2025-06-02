import base64

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

from work_with_files import read_file, write_text_file, read_text_file
from symmetric_encryption import SymmetricEncryptor


class AsymmetricKeyManager:
    def __init__(self, sym_key_length: int):
        self.sym_key_length = sym_key_length

    def generate_keys(self, priv_key_path: str, pub_key_path: str, encrypted_key_path: str):
        sym_key = SymmetricEncryptor.generate_3des_key(self.sym_key_length)

        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()

        with open(priv_key_path, "wb") as f:
            f.write(private_key.private_bytes(
                serialization.Encoding.PEM,
                serialization.PrivateFormat.PKCS8,
                serialization.NoEncryption()
            ))

        with open(pub_key_path, "wb") as f:
            f.write(public_key.public_bytes(
                serialization.Encoding.PEM,
                serialization.PublicFormat.SubjectPublicKeyInfo
            ))

        encrypted_key = public_key.encrypt(
            sym_key,
            padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )

        write_text_file(encrypted_key_path, base64.b64encode(encrypted_key).decode())

    @staticmethod
    def load_symmetric_key(priv_key_path: str, encrypted_key_path: str) -> bytes:
        private_key = serialization.load_pem_private_key(read_file(priv_key_path), password=None)
        encrypted_key = base64.b64decode(read_text_file(encrypted_key_path))
        return private_key.decrypt(
            encrypted_key,
            padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )
