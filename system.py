from pathlib import Path
import sys
import tomllib
from typing import TypedDict


def exit_success():
    sys.exit(0)


def exit_error(message: str):
    print(message)
    input("Press any key to close the console.")
    sys.exit(1)


class config(TypedDict):
    note_dir_path: str


def load_config() -> config:
    config_dir = (
        Path(__file__).parent
        if Path(sys.executable).name == "python.exe"
        else Path(sys.executable).parent
    )

    config_file = config_dir.joinpath("config.toml")
    if not config_file.exists():
        exit_error("config.toml is missing.")

    with open(config_file, "rb") as f:
        data = tomllib.load(f)
    if not data.get("note_dir_path"):
        exit_error("note_dir_path is missing in config.toml.")

    return data
