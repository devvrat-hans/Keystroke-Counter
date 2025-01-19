key_count = 0  # Initialize the keystroke count

# Define a function that will be called when a key is pressed
def on_press(key):
    global key_count
    try:
        key_count += 1
    except AttributeError:
        pass  # Ignore special keys like "space" or "shift" if you don't want to count them

# Define a function to stop the listener when a specific key is pressed (e.g., "esc")
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener if the Escape key is pressed
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
