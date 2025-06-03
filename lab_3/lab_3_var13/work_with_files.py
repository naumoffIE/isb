import json


class WorkWithFiles:
    @staticmethod
    def read_file(path: str) -> bytes:
        """Read binary content of a file."""
        with open(path, "rb") as f:
            return f.read()

    @staticmethod
    def read_text_file(path: str) -> str:
        """Read text content of a file."""
        with open(path, "r") as f:
            return f.read()

    @staticmethod
    def write_file(path: str, data: bytes) -> None:
        """Write binary content to the path."""
        with open(path, "wb") as f:
            f.write(data)

    @staticmethod
    def write_text_file(path: str, data: str) -> None:
        """Write text content to the path."""
        with open(path, "w") as f:
            f.write(data)

    @staticmethod
    def load_config(config_path: str) -> dict:
        """Load JSON configuration from the given file path."""
        with open(config_path, "r") as f:
            return json.load(f)
