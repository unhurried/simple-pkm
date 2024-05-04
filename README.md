# simple-pkm

A simple PKM (Personal Knowledge Management) tool for Windows.

## How to ...

### Build the application

```bash
# Install dependencies.
pipenv shell
pipenv install

# Create an executable with PyInstaller.
pyinstaller --onefile -n "simple-pkm" .\main.py

# Create an executable with nuitka.
nuitka --standalone --enable-plugin=tk-inter --disable-console --output-filename=simple-pkm main.py
```

### Run the application

Before running the following commands, please place [`config.toml`](./config.toml) in the same directory with `simple-pkm.exe'.

```bash
simple-pkm.exe
```
