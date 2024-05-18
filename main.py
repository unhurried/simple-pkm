import os
from pathlib import Path
from prompt import prompt
import pyperclip
import os.path
from search import search
from system import exit_error, exit_success, get_config_dir, load_config

# Load config file.
config = load_config()

# Exit if note_dir doesn't exist.
note_dir = Path(config["note_dir_path"])
if not note_dir.exists():
    exit_error("note_dir_path doesn't exist.")

mode, keyword = prompt()

if mode == "find":
    search(note_dir, "find", False, keyword)

elif mode == "new folder":
    if not keyword:
        exit_success()

    # Prepare a Path object for the folder.
    folder = note_dir.joinpath(f"{keyword}")

    # Create a folder in the directory.
    os.makedirs(folder)

    # Copy the file path to the clipboard and open the file.
    pyperclip.copy(str(folder))
    os.startfile(str(folder))

elif mode == "new page":
    if not keyword:
        exit_success()

    # Prepare a Path object for the page file.
    page_file = note_dir.joinpath(f"{keyword}.md")

    # Create a markdown file in the directory.
    with open(page_file, "w", encoding="utf_8_sig") as f:
        f.write("\r\n")

    # Copy the file path to the clipboard and open the file.
    pyperclip.copy(str(page_file))
    os.startfile(str(page_file))

elif mode == "list":
    search(note_dir, "list", True)
