# simple-pkm

A simple PKM (Personal Knowledge Management) tool for Windows.

## How to ...

### Build the application

```bash
# Install dependencies.
pipenv shell
pipenv install

# Create an executable with PyInstaller.
pyinstaller --onefile --noconsole --icon="resource/favicon.ico" -n "simple-pkm" .\main.py

# Create an executable with nuitka.
# Note: Exclude --onefile option when the executable is detected as a malware.
nuitka --standalone --onefile --enable-plugin=tk-inter --disable-console --windows-icon-from-ico="resource/favicon.ico" --output-filename=simple-pkm main.py
```

### Run the application

Before running the following commands, please place [`config.toml`](./config.toml) in the same directory with `simple-pkm.exe'.

```bash
simple-pkm.exe
```
