import os

def clear_console() -> None:
    """Clear console using cls or clear according to the os name"""

    os.system('cls' if os.name == 'nt' else 'clear')