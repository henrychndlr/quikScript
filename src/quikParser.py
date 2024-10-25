import time

def delay(milliseconds):
    """Simulate a delay."""
    seconds = milliseconds / 1000.0
    print(f"Delaying for {milliseconds} ms ({seconds} seconds)")
    time.sleep(seconds)

def type_string(text):
    """Simulate typing a string of characters."""
    print(f"Typing string: {text}")
    # Simulate keypresses (could be done later with HID on microcontroller)
    # e.g., using pyautogui or microcontroller USB HID library

def press_key(key):
    """Simulate pressing a single key."""
    print(f"Pressing key: {key}")
    # Simulate a keypress action

def press_key_combo(modifier, key):
    """Simulate pressing a combination like CTRL+C."""
    print(f"Pressing {modifier} + {key}")
    # Simulate key combo action

def execute_command(command):
    """Interpret and execute QuickScript commands."""
    if command.startswith("DELAY"):
        delay_time = int(command.split()[1])
        delay(delay_time)

    elif command.startswith("STRING"):
        text = command[7:]  # Everything after "STRING "
        type_string(text.strip())

    elif command.startswith("ENTER"):
        press_key("ENTER")

    elif command.startswith("TAB"):
        press_key("TAB")

    elif command.startswith("BACKSPACE"):
        press_key("BACKSPACE")

    elif command.startswith("CTRL") or command.startswith("ALT") or command.startswith("SHIFT"):
        parts = command.split('+')
        if len(parts) == 2:
            press_key_combo(parts[0], parts[1])

    elif command.startswith("CLICK"):
        print("Mouse Click")
        # Simulate mouse click

    elif command.startswith("RIGHTCLICK"):
        print("Right Mouse Click")
        # Simulate right click

    else:
        print(f"Unknown command: {command.strip()}")

def parse_file(file_path):
    """Parse and execute commands from a .ducky file."""
    with open(file_path, "r") as file:
        for line in file:
            execute_command(line.strip())

if __name__ == "__main__":
    # Test with a new extended script
    script_file = "../scripts/extended_example.ducky"
    parse_file(script_file)
