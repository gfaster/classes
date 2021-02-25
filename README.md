# classes

**Need someone to write a linux/OSX build script**

## Configuration

to configure:
change values in config.json to reflect your classes and periods

---
## Building from Source

1. Install [pyinstaller](https://pypi.org/project/pyinstaller/) via pip
2. Configure config.json to reflect your classes and periods, as well as your browser
3. Run the following command:
	- **Windows:** Run `build.bat`
	- **Linux and macOS:** `pyinstaller --add-data 'config.json:.' main.py`