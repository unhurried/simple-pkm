import os
from pathlib import Path
from system import get_config_dir


def search(note_dir: Path, key: str, non_recursive: bool, keyword: str = ""):
    config_dir = get_config_dir()
    search_file = config_dir.joinpath(f"{key}.search-ms")

    search_template = config_dir.joinpath(f"resource/template.search-ms")
    with open(search_template, "r", encoding="utf_8") as t, open(
        search_file, "w", encoding="utf_8"
    ) as f:
        contents = (
            t.read()
            .replace("${note_dir}", str(note_dir))
            .replace("${non_recursive}", str(non_recursive).lower())
            .replace("${keyword}", keyword)
        )
        f.write(contents)

    os.startfile(search_file)
