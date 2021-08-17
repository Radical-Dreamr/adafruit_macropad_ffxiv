# Adafruit RP2040 Macropad Hotkeys for Final Fantasy XIV 
A basic macropad hotkey template for Final Fantasy XIV (FFXIV) and the Adafruit RP2040 Macropad using CircuitPython

I play FFXIV using a controller, and while I use a keyboard as well it is helpful to be able to have a few macros on hand. I set the numbered Function keys (F1-F12) to activate emotes or macros in game (like /emote motion or a greeting with a smile emote) that are set to a shared hotbar. The default for these keys is set for targetting, so if you use it that way you may want to change the code to other keys or use a modifier with the function keys. Also, if you use a controller you'll need to change your control mode to mouse temporarily to set up your hotbar, but when you switch back to controller and the Cross Hotbar you should be able to still use the other hotkeys.

You can combine this with the game's macro system, or just try short commands directly from the code. I'm not 100% sure all the chat commands work perfectly, and I didn't end up using the rotary encoder button yet. You can set up a few hotbars this way, I ended up using ALT+(F1-F12) for another set of emotes. You can play around with the colors too, I still need to get mine set up for multiple hotkey configs. I found that I needed to set the color values to very dark, otherwise the LEDs were way too bright for extended use in a dark room.

For documentation on the Macropad and the code for the hotkey configurations can be found at https://learn.adafruit.com/macropad-hotkeys. I just modified one of their examples to create these, I believe it was for the Windows Edge Browser initially.

The .py file should be placed in your /macros directory on your RP2040.

Please understand that I have no idea what I am actually doing, and don't have any intentions to maintain this in any way.

