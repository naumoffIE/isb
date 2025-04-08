from constants import *

from utility_functions import calculate_freq_letter_occurrence, read_file


def main() -> None:
    text = read_file(PATH_TO_ENCRYPTED_TEXT)

    print("\nEncrypted text:\n")
    print(text)

    percent_dict = calculate_freq_letter_occurrence(text)

    print("\n______________________________________________________________\n")
    print("Character frequency percentages in the encrypted text:\n")
    sorted_dict = {
        i: val for i, val in sorted(enumerate(percent_dict), key=lambda x: x[0])
    }
    print(sorted_dict)

    print("\nRussian frequency dictionary:\n")
    print(RUS_FREQ)

    print("\n______________________________________________________________\n")
    print("Decrypted text:\n")

    replacements: dict[str, str] = {
        "-": " ", "U": "о", "B": "т", "V": "э", "d": "е", "R": "г", "A": "к",
        "9": "р", "K": "м", "h": "у", "I": "д", "O": "ф", "M": "и", "E": "в",
        "8": "ы", ">": "н", "3": "с", "Y": "а", "$": "х", "F": "ш", "!": "б",
        "Q": "п", "L": "ч", "C": "ю", "W": "й", "t": "л", "=": "ц", "G": "ь",
        "J": "з", "P": "я", "Z": "ж", "n": "щ", "x": "ъ"
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    print(text)
    print("\n")


if __name__ == "__main__":
    main()
