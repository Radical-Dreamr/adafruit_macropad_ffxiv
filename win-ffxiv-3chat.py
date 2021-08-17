# MACROPAD Hotkeys example: FFXIV Chat for Windows

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    "name": "FFXIV Chat",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x666666, "/s", [Keycode.FORWARD_SLASH, "s", Keycode.ENTER]),
        (0x004242, "/fc", [Keycode.FORWARD_SLASH, "fc", Keycode.ENTER]),
        (0x000040, "/p", [Keycode.FORWARD_SLASH, "p", Keycode.ENTER]),
        # 2nd row ----------
        (
            0x101010,
            "Hello",
            [
                Keycode.FORWARD_SLASH,
                "smile motion",
                Keycode.ENTER,
                "hello!",
                Keycode.ENTER,
            ],
        ),
        (0x101010, "Hiii", ["hiiiiii!", Keycode.ENTER]),
        (0x120400, "/a", [Keycode.FORWARD_SLASH, "a", Keycode.ENTER]),
        # 3rd row ----------
        (0x000040, "HiLvly", ["hello, lovely people", Keycode.ENTER]),
        (0x000040, "OvrHre", ["over here!", Keycode.ENTER]),
        (0x000040, "LvlyShw", ["lovely show, all!", Keycode.ENTER]),
        # 4th row ----------
        (0x800080, "Oops", ["oops", Keycode.ENTER]),
        (0x800080, "OhNo", ["oh no!", Keycode.ENTER]),
        (0x800080, "L8r", ["until next time!", Keycode.ENTER]),
        # Encoder button ---
        (0x000000, "", [Keycode.CONTROL, "w"]),  # Close tab
    ],
}
