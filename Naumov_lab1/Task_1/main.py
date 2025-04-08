from constants import *

from utility_functions import belazo_encrypt, read_file, write_to_file


def main() -> None:
    try:
        plaintext = read_file(PATH_TO_ORIGINAL_TEXT)
        key = read_file(KEYWORD)

        print("\nOriginal text:\n")
        print(plaintext)

        encrypted = belazo_encrypt(plaintext, key)
        print("\nEncrypted text:\n")
        print(encrypted)

        write_to_file(PATH_TO_ENCRYPTED_TEXT, encrypted)
        print("\nResult successfully written to file.")

    except FileNotFoundError:
        print("Error: file not found")
    except UnicodeDecodeError:
        print("Error: file encoding problem")
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
