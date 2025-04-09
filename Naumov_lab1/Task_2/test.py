from constants import *

from utility_functions import calculate_freq_letter_occurrence, read_file, read_json


def main() -> None:
    text = read_file(PATH_TO_ENCRYPTED_TEXT)

    print("\nEncrypted text:\n")
    print(text)

    freq_dict = calculate_freq_letter_occurrence(text)

    print("\n______________________________________________________________\n")
    print("Frequency of a letter occurrence:\n")
    print(freq_dict)

    print("\nRussian frequency dictionary:\n")
    print(RUS_FREQ)

    print("\n______________________________________________________________\n")
    print("Decrypted text:\n")

    replacements = read_json(PATH_TO_WRITE_KEY)

    for old, new in replacements.items():
        text = text.replace(old, new)

    print(text)
    print("\n")


if __name__ == "__main__":
    main()
