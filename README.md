# Keylogger with Start/Stop Toggle (Python + pynput)

This is a basic keylogger tool built using Python and the `pynput` library. It allows you to start and stop keyboard logging with hotkeys and records keystrokes to a text file.

> ⚠️ **For educational and authorized use only. Do not use this tool without explicit permission.**

---

## 🔐 Features

- 🟢 Start logging with **F9**
- 🔴 Stop logging with **F10**
- ⛔ Exit the program with **Esc**
- Records all keystrokes to `keylog.txt`
- Supports special keys (space, enter, arrows, etc.)
- Simple and minimal implementation

---

## 📦 Requirements

- Python 3.x
- `pynput` library

Install with pip:

```bash
pip install pynput
```

---

## 🚀 Usage

1. **Clone the Repository**:

```bash
git clone https://github.com/your-username/python-keylogger.git
cd python-keylogger
```

2. **Run the Script**:

```bash
python keylogger.py
```

3. **Controls**:

- Press **F9** to start logging keys to `keylog.txt`
- Press **F10** to pause logging
- Press **Esc** to exit the program

4. **Output**:

Logged keys will be saved in a file named `keylog.txt` in the same directory.

---

## 📁 File Structure

```
keylogger.py         # Main keylogging script
keylog.txt           # Output log file
README.md            # Project documentation
```

---

## ⚠️ Disclaimer

This tool is intended strictly for educational purposes and **must not be used for unauthorized or malicious activity**. Always obtain proper consent before running a keylogger.

---

> Created for learning purposes by Ashik Ahmed 🛡️
