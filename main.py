import datetime
import os
from pathlib import Path
import pyperclip
import os.path
import argparse

from system import exit_error, load_config

# Load command options.
parser = argparse.ArgumentParser(
    prog="simple-pkm",
    usage="simple-pkm <command>",
    add_help=False,
)
parser.add_argument("command", choices=["create", "search"])
args = parser.parse_args()

# Load config file.
config = load_config()

# Exit if note_dir doesn't exist.
note_dir = Path(config["note_dir_path"])
if not note_dir.exists():
    exit_error("note_dir_path doesn't exist.")

if args.command == "search":

    search_keyword: str = input("Enter search keyword: ")
    os.startfile(
        f"search-ms:displayname=Search Result&query={search_keyword}&crumb=location:{note_dir}"
    )

elif args.command == "create":

    page_title: str = input("Enter page title: ")

    # Prepare a Path object for the page file.
    date = format(datetime.date.today(), "%Y_%m%d")
    page_dir_name = f"{date}_{page_title}"
    page_dir = note_dir.joinpath(page_dir_name)
    page_file = page_dir.joinpath("index.md")

    # Create a directory and a markdown file in the directory.
    os.makedirs(page_dir)
    with open(page_file, "w", encoding="utf_8_sig") as f:
        f.write("\r\n")

    # Copy the file path to the clipboard and open the file.
    pyperclip.copy(str(page_file))
    os.startfile(str(page_file))
