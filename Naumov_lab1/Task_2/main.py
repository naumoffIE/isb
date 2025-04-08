from constants import *

from utility_functions import calculate_freq_letter_occurrence, read_file, read_json, write_json, write_to_file


def main() -> None:
    try:
        original_text = read_file(PATH_TO_ENCRYPTED_TEXT)
        decrypt_key = read_json(PATH_TO_WRITE_KEY)

        print("\nEncrypted text:\n")
        print(original_text)

        percent_dict = calculate_freq_letter_occurrence(original_text)

        print("\n_________________________________________\n\nFrequency index of encrypted text:\n")
        sorted_dict = {
            key: percent_dict[key]
            for key in sorted(percent_dict, key=percent_dict.get, reverse=True)
        }
        print(sorted_dict)

        print("\n___________________________________________\n\nDecrypted text:\n")
        decrypted_text = original_text
        for char, replacement in decrypt_key.items():
            decrypted_text = decrypted_text.replace(char, replacement)
        print(decrypted_text)

        print("\nEncryption key:\n")
        print(decrypt_key)

        write_to_file(PATH_TO_WRITE_DECRYPTED_TEXT_FILE, decrypted_text)
        write_json(PATH_TO_WRITE_KEY, decrypt_key)
        print("\nResults have been successfully saved to files.")

    except FileNotFoundError:
        print("Error: Encrypted text file not found.")
    except UnicodeDecodeError:
        print("Error: Problem with file encoding.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
