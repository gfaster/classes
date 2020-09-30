# classes

This generates today's class schedule. 

## Configuration

to configure:
change values in config.json to reflect your classes and periods

---
## Building from Source

1. Install [pyinstaller](https://pypi.org/project/pyinstaller/) via pip
2. Configure config.json to reflect your classes and periods
3. Run the following command:
	- **Windows:** `pyinstaller --add-data 'config.json;.' main.py`
	- **Linux and macOS:** `pyinstaller --add-data 'config.json:.' main.py`
