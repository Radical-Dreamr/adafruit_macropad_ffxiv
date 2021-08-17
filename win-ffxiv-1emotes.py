# MACROPAD Hotkeys example: Final Fantasy FFXIV for Windows

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    "name": "FFXIV Emotes",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x00002e, "Wink", [Keycode.F1]),  # add notes here
        (0x00002e, "Smile", [Keycode.F2]),
        (0x00002e, "Wave", [Keycode.F3]),
        # 2nd row ----------
        (0x420042, "Greet", [Keycode.F4]),
        (0x420042, "Clap", [Keycode.F5]),
        (0x420042, "Yes", [Keycode.F6]),
        # 3rd row ----------
        (0x002A2A, "BsKnee", [Keycode.F7]),
        (0x002A2A, "Pose", [Keycode.F8]),
        (0x002A2A, "V-Pose", [Keycode.F9]),
        # 4th row ----------
        (0x101010, "Lean", [Keycode.F10]),
        (0x101010, "Sit", [Keycode.F11]),
        (0x101010, "ChgPse", [Keycode.F12]),
        # Encoder button ---
        (
            0x000000,
            "",
            [
                Keycode.CONTROL,
            ],
        ),
    ],
}
