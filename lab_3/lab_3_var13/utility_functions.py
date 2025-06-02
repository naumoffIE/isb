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


def ask_key_length() -> int:
    print("Choose 3DES key length:")
    print("1 - 64 bits")
    print("2 - 128 bits")
    print("3 - 192 bits")

    choice = input("Enter option (1/2/3): ").strip()
    if choice == "1":
        return 8
    elif choice == "2":
        return 16
    elif choice == "3":
        return 24
    else:
        print("Invalid choice, defaulting to 192-bit key.")
        return 24

