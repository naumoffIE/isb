import json


def write_to_file(filename: str, content: str) -> None:
    """
    Writes the given content to a file.

    :param: filename: The name of the file to write to.
    :param: content: The content to be written.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print(f"Error on file record {filename}: {e}")


def read_file(filename: str) -> str:
    """
    Reads the content from a file.

    :param: filename: The name of the file to read.
    :return: The content of the file as a string.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Error on reading {filename}: {e}")


def calculate_freq_letter_occurrence(text: str) -> dict[str, float]:
    """
    Calculates character frequency index in the given text.

    :param: text: The input text.
    :return: A dictionary with characters as keys and their frequency (as percentage) as values.
    """

    try:
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        if len(text) == 0:
            raise ValueError("Input text must not be empty.")

        char_count: dict[str, int] = {}
        text_len: int = len(text)

        for char in text:
            char_count[char] = char_count.get(char, 0) + 1

        char_freq: dict[str, float] = {
            char: count / text_len for char, count in char_count.items()
        }

        return char_freq

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


def read_json(filename: str) -> dict:
    """
    Reads the content from a .json .
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error on reading {filename}: {e}")
        return {}


def write_json(file_path: str, data: dict | list) -> None:
    """
    Records data into JSON-file on the specified path
    :param: file_path: file path.
    :param: data: data to record (dictionary or list).
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except (OSError, TypeError) as e:
        print(f"Error on file record: {e}")
