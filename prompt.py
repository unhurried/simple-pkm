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

    def list(x):
        global mode
        mode = "list" 
        root.destroy()
    root.bind("l", list)

    def escape(x):
        global keyword
        keyword = None
        root.destroy()
    root.bind("<Escape>", escape)

    def change_mode(mode_name: str):
        def _change_mode(event):
            root.title(f"{APP_NAME} - {mode_name.capitalize()}")
            global mode
            mode = mode_name 
            entry.focus_set()
        return _change_mode
    root.bind("c", change_mode("create"))
    root.bind("s", change_mode("search"))

    root.focus_set()
    root.mainloop()

    return mode, keyword
