from asymmetric_encryption import AsymmetricKeyManager
from symmetric_encryption import SymmetricEncryptor, SymmetricDecryptor
from utility_functions import ask_key_length
from work_with_files import load_config


def main():
    print("Hybrid Crypto System (RSA + 3DES)")
    print("1 - Generate keys")
    print("2 - Encrypt file")
    print("3 - Decrypt file")
    choice = input("Choose an option (1/2/3): ").strip()

    config = load_config("config.json")

    if choice == "1":
        key_length = ask_key_length()
        manager = AsymmetricKeyManager(sym_key_length=key_length)
        manager.generate_keys(
            priv_key_path=config["private_key_path"],
            pub_key_path=config["public_key_path"],
            encrypted_key_path=config["encrypted_sym_key_path"]
        )

    elif choice == "2":
        key = AsymmetricKeyManager.load_symmetric_key(
            priv_key_path=config["private_key_path"],
            encrypted_key_path=config["encrypted_sym_key_path"]
        )
        encryptor = SymmetricEncryptor(key)
        encryptor.encrypt(
            input_file=config["input_file"],
            output_file=config["encrypted_output"]
        )

    elif choice == "3":
        key = AsymmetricKeyManager.load_symmetric_key(
            priv_key_path=config["private_key_path"],
            encrypted_key_path=config["encrypted_sym_key_path"]
        )
        decryptor = SymmetricDecryptor(key)
        decryptor.decrypt(
            input_file=config["encrypted_output"],
            output_file=config["decrypted_output"]
        )

    else:
        print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
