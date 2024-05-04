import datetime
import os
from pathlib import Path
from prompt import prompt
import pyperclip
import os.path
import argparse
from system import exit_error, exit_success, load_config

# Load config file.
config = load_config()

# Exit if note_dir doesn't exist.
note_dir = Path(config["note_dir_path"])
if not note_dir.exists():
    exit_error("note_dir_path doesn't exist.")

mode, keyword = prompt()

if mode == "search":
    if not keyword:
        exit_success()
    os.startfile(
        f"search-ms:displayname=Search Result&query={keyword}&crumb=location:{note_dir}"
    )

elif mode == "create":
    if not keyword:
        exit_success()

    # Prepare a Path object for the page file.
    date = format(datetime.date.today(), "%Y_%m%d")
    page_dir_name = f"{date}_{keyword}"
    page_dir = note_dir.joinpath(page_dir_name)
    page_file = page_dir.joinpath("index.md")

    # Create a directory and a markdown file in the directory.
    os.makedirs(page_dir)
    with open(page_file, "w", encoding="utf_8_sig") as f:
        f.write("\r\n")

    # Copy the file path to the clipboard and open the file.
    pyperclip.copy(str(page_file))
    os.startfile(str(page_file))

elif mode == "list":
    os.startfile(note_dir)
