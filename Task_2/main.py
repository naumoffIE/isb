from constants import *


def write_to_file(filename: str, content: str) -> None:
    """
    Writes the given content to a file.

    :param: filename: The name of the file to write to.
    :param: content: The content to be written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


def read_file(filename: str) -> str:
    """
    Reads the content from a file.

    :param: filename: The name of the file to read.
    :return: The content of the file as a string.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def calculate_freq_index(text: str) -> dict[str, float]:
    """
    Calculates character frequency index in the given text.

    :param: text: The input text.
    :return: A dictionary with characters as keys and their frequency (as percentage) as values.
    """
    char_count: dict[str, int] = {}
    text_len: int = len(text)

    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    char_percentages: dict[str, float] = {
        char: count / text_len for char, count in char_count.items()
    }

    return char_percentages


def main() -> None:
    try:
        # Read encrypted text
        original_text = read_file(PATH_TO_ENCRYPTED_TEXT)

        print("\nEncrypted text:\n")
        print(original_text)

        # Frequency calculation
        percent_dict = calculate_freq_index(original_text)

        print("\n_________________________________________\n\nFrequency index of encrypted text:\n")
        sorted_dict = {
            key: percent_dict[key]
            for key in sorted(percent_dict, key=percent_dict.get, reverse=True)
        }
        print(sorted_dict)

        # Decryption
        print("\n___________________________________________\n\nDecrypted text:\n")
        decrypted_text = original_text
        for char, replacement in DECRYPT_KEY.items():
            decrypted_text = decrypted_text.replace(char, replacement)
        print(decrypted_text)

        print("\nEncryption key:\n")
        print(DECRYPT_KEY)

        # Save results
        write_to_file(PATH_TO_WRITE_DECRYPTED_TEXT_FILE, decrypted_text)
        write_to_file(PATH_TO_WRITE_KEY, str(DECRYPT_KEY))
        print("\nResults have been successfully saved to files.")

    except FileNotFoundError:
        print("Error: Encrypted text file not found.")
    except UnicodeDecodeError:
        print("Error: Problem with file encoding.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
