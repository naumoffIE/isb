from constants import *


def write_to_file(filename: str, content: str) -> None:
    """
    Writes the contents to a file
    :param filename: file name
    :param content: content to record
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


def read_file(filename: str) -> str:
    """
    Reads data from a file
    :param: filename: file name
    :return: file contents
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def repeat_key(text: str, key: str) -> str:
    """
    Repeats the key to the length of the text
    """
    return (key * (len(text) // len(key) + 1))[:len(text)]


def belazo_encrypt(plaintext: str, key: str) -> str:
    """
    Encrypts the message using the Belazo cipher with the Trithemia table
    :param: plaintext: source text
    :param: key: keyword
    :return: ciphertext
    """
    plaintext = plaintext.lower()
    key = repeat_key(plaintext, key.lower())
    encrypted = []

    for i in range(len(plaintext)):
        if plaintext[i] in ALPHABET_INDEX:
            pi = ALPHABET_INDEX[plaintext[i]]
            ki = ALPHABET_INDEX[key[i]]
            encrypted_char = RUSSIAN_ALPHABET[(pi + ki) % ALPHABET_LEN]
            encrypted.append(encrypted_char)
        else:
            encrypted.append(plaintext[i])

    return ''.join(encrypted)


def belazo_decrypt(ciphertext: str, key: str) -> str:
    """
    Decrypts the message encrypted with the Belazo cipher
    :param: ciphertext: ciphertext
    :param: key: keyword
    :return: decrypted text

    """
    ciphertext = ciphertext.lower()
    key = repeat_key(ciphertext, key.lower())
    decrypted = []

    for i in range(len(ciphertext)):
        if ciphertext[i] in ALPHABET_INDEX:
            wi = ALPHABET_INDEX[ciphertext[i]]
            ki = ALPHABET_INDEX[key[i]]
            decrypted_char = RUSSIAN_ALPHABET[(wi - ki + ALPHABET_LEN) % ALPHABET_LEN]
            decrypted.append(decrypted_char)
        else:
            decrypted.append(ciphertext[i])

    return ''.join(decrypted)

