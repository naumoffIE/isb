from os import urandom


def generate_3des_key(length_bits: int) -> bytes:
    if length_bits not in VALID_KEY_LENGTHS:
        raise ValueError(f"3DES key length must be one of {VALID_KEY_LENGTHS}")
    return urandom(length_bits // 8)


def pad(data: bytes) -> bytes:
    pad_len: int = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([pad_len] * pad_len)


def unpad(data: bytes) -> bytes:
    pad_len: int = data[-1]
    return data[:-pad_len]
