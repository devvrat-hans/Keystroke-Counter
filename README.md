# Keystroke Counter

A simple Python script that monitors keystrokes on macOS and Windows. This script counts the number of key presses during a session and prints the count to the terminal. It also allows you to stop the counter by pressing the **Escape** key.

## Features:
- Counts all keypresses made on the keyboard.
- Stops counting when the **Escape** key is pressed.
- Compatible with **macOS** and **Windows**.

## Requirements:
- Python 3.x
- `pynput` library

## Installation:

1. **Clone the repository** (or download the ZIP):
    ```bash
    git clone https://github.com/your-username/keystroke-counter.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd keystroke-counter
    ```

3. **Install the required dependencies**:
    ```bash
    pip install pynput
    ```

## Usage:

1. **Run the script**:
    In your terminal (Command Prompt, PowerShell, or macOS Terminal), run the script with:
    ```bash
    python keystroke_counter.py
    ```

2. **Keystroke Counting**:
    - The script will start counting keystrokes immediately.
    - Every time you press a key, the count will increase by one.

3. **Stop the Counter**:
    - To stop the keystroke counter, simply press the **Escape** key. This will stop the listener and end the script.

## Example Output:
```bash
Keystroke Counter is running...
Keystrokes: 1
Keystrokes: 2
Keystrokes: 3
...
```
## Platform Compatibility:
- The script works on **macOS** and **Windows**.
- On **macOS**, you may need to give the script accessibility permissions to allow it to monitor keystrokes. This can be done in **System Preferences > Security & Privacy > Privacy**.

## Notes:
- The script uses the `pynput` library for cross-platform key event handling.
- Special keys like `Shift`, `Ctrl`, etc., are not counted by default but can be included by modifying the script.

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
