import json
from key_generation import KeyGenerator
from encryptor import Encryptor
from decryptor import Decryptor


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


def load_config(config_path: str) -> dict:
    """Load JSON configuration from the given file path."""
    with open(config_path, "r") as f:
        return json.load(f)


def main():
    print("Hybrid Crypto System (RSA + 3DES)")
    print("1 - Generate keys")
    print("2 - Encrypt file")
    print("3 - Decrypt file")
    choice = input("Choose an option (1/2/3): ").strip()

    config = load_config("config.json")

    if choice == "1":
        key_length = ask_key_length()
        generator = KeyGenerator(
            sym_key_length=key_length,
            priv_key_path=config["private_key_path"],
            pub_key_path=config["public_key_path"],
            encrypted_key_path=config["encrypted_sym_key_path"]
        )
        generator.generate()

    elif choice == "2":
        encryptor = Encryptor(
            private_key_path=config["private_key_path"],
            encrypted_key_path=config["encrypted_sym_key_path"]
        )
        encryptor.encrypt(
            input_file=config["input_file"],
            output_file=config["encrypted_output"]
        )

    elif choice == "3":
        decryptor = Decryptor(
            private_key_path=config["private_key_path"],
            encrypted_key_path=config["encrypted_sym_key_path"]
        )
        decryptor.decrypt(
            input_file=config["encrypted_output"],
            output_file=config["decrypted_output"]
        )

    else:
        print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
