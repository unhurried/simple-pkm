import tkinter as tk
from typing import Tuple

APP_NAME = "simple-pkm"


def prompt() -> Tuple[str, str]:
    """Show GUI to prompt a user to select mode and keyword.

    Returns:
        Tuple[str, str]: Mode and keyword that a user entered.
    """
    window = _Window()
    window.start()
    return window.get_input()


class _Window:
    def __init__(self) -> None:
        self._mode: str = None
        self._keyword: str = None

        self._root = tk.Tk()
        self._root.title(APP_NAME)
        self._root.configure(background="white")

        self._entry = tk.Entry(width=40, font=("Meiryo UI", 10), border=0)

        def enter(x):
            self._keyword = self._entry.get()
            self._root.destroy()

        self._entry.bind("<Return>", enter)
        self._entry.pack(padx=10, pady=10)

        def escape(x):
            self._keyword = None
            self._root.destroy()

        self._root.bind("<Escape>", escape)

        def list(x):
            self._mode = "list"
            self._root.destroy()

        def change_mode(mode_name: str):
            def _change_mode(event):
                self._root.title(f"{APP_NAME} - {mode_name}")
                self._mode = mode_name
                self._root.unbind("l")
                self._root.unbind("np")
                self._root.unbind("nf")
                self._root.unbind("f")
                self._entry.focus_set()

            return _change_mode

        self._root.bind("l", list)
        self._root.bind("np", change_mode("new page"))
        self._root.bind("nf", change_mode("new folder"))
        self._root.bind("f", change_mode("find"))

    def start(self):
        self._root.focus_set()
        self._root.mainloop()

    def get_input(self) -> Tuple[str, str]:
        return self._mode, self._keyword
