from os import urandom

from cryptography.hazmat.primitives import padding as sym_padding

from constants import BLOCK_SIZE


def pad(data: bytes) -> bytes:
    """Apply PKCS7 padding for 3DES (block size 64 bits)."""
    padder = sym_padding.PKCS7(BLOCK_SIZE).padder()
    return padder.update(data) + padder.finalize()


def unpad(data: bytes) -> bytes:
    """Remove PKCS7 padding."""
    unpadder = sym_padding.PKCS7(BLOCK_SIZE).unpadder()
    return unpadder.update(data) + unpadder.finalize()


def read_file(path: str) -> bytes:
    """Read binary content of a file."""
    with open(path, "rb") as f:
        return f.read()
