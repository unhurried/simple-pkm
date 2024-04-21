# simple-pkm

A simple PKM (Personal Knowledge Management) tool for Windows.

## How to ...

### Build the application

```bash
# Install dependencies.
pipenv shell
pipenv install

# Create an executable with PyInstaller.
pyinstaller --onefile --console -n "simple-pkm" .\main.py
```

### Run the application

Before running the following commands, please place [`config.toml`](./config.toml) in the same directory with `simple-pkm.exe'.

```bash
# Create a new page.
simple-pkm.exe create

# Search pages for keywords.
simple-pkm.exe search
```
