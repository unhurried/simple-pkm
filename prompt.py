import tkinter as tk
from typing import Tuple

APP_NAME = "simple-pkm"

mode: str = None
keyword: str = None


def prompt() -> Tuple[str, str]:
    root = tk.Tk()
    root.title(APP_NAME)
    root.configure(background="white")

    entry = tk.Entry(width=40, font=("Meiryo UI", 10), border=0)

    def enter(x):
        global keyword
        keyword = entry.get()
        root.destroy()

    entry.bind("<Return>", enter)
    entry.pack(padx=10, pady=10)

    def escape(x):
        global keyword
        keyword = None
        root.destroy()

    root.bind("<Escape>", escape)

    def list(x):
        global mode
        mode = "list"
        root.destroy()

    def change_mode(mode_name: str):
        def _change_mode(event):
            root.title(f"{APP_NAME} - {mode_name}")
            global mode
            mode = mode_name
            root.unbind("l")
            root.unbind("p")
            root.unbind("f")
            root.unbind("s")
            entry.focus_set()

        return _change_mode

    root.bind("l", list)
    root.bind("p", change_mode("create page"))
    root.bind("f", change_mode("create folder"))
    root.bind("s", change_mode("search"))

    root.focus_set()
    root.mainloop()

    return mode, keyword
