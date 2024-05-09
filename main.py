import os
from pathlib import Path
from prompt import prompt
import pyperclip
import os.path
from system import exit_error, exit_success, get_config_dir, load_config

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

elif mode == "create folder":
    if not keyword:
        exit_success()

    # Prepare a Path object for the folder.
    folder = note_dir.joinpath(f"{keyword}")

    # Create a folder in the directory.
    os.makedirs(folder)

    # Copy the file path to the clipboard and open the file.
    pyperclip.copy(str(folder))
    os.startfile(str(folder))

elif mode == "create page":
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
    config_dir = get_config_dir()
    search_file = config_dir.joinpath("list.search-ms")
    if not search_file.exists():
        search_template = config_dir.joinpath(f"resource/template.search-ms")
        with open(search_template, "r", encoding="utf_8") as t, open(
            search_file, "w", encoding="utf_8"
        ) as f:
            contents = t.read().replace("${note_dir}", str(note_dir))
            f.write(contents)

    os.startfile(search_file)
