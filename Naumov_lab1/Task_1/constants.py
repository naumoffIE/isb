PATH_TO_ENCRYPTED_TEXT = "encrypted_text.txt"

PATH_TO_ORIGINAL_TEXT = "original_text.txt"

KEYWORD = "decrypt_key.txt"

RUSSIAN_ALPHABET = [
    "а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
    "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"
]

ALPHABET_LEN = len(RUSSIAN_ALPHABET)
ALPHABET_INDEX = {char: i for i, char in enumerate(RUSSIAN_ALPHABET)}
