"""CircuitPython Capacitive Touch HID Example for Neo Trinkey"""
import time
import board
import touchio
import usb_hid
import neopixel


from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, brightness=0.02)
Red = (255, 0, 0)
Green = (0, 255, 0)

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

ledCounterAudio = 1
ledCounterVideo = 1

pixels.fill(Red)
pixels.show()

touched = time.monotonic()


while True:
    if time.monotonic() - touched < 0.25:
        continue
    if touch1.value:  # If touch pad 1 is touched...
        while touch1.value:  # Wait for release...
            time.sleep(0.1)
        print("Mute")  # Then send key press.)
        keyboard.send(Keycode.SHIFT, Keycode.CONTROL, Keycode.M)
        time.sleep(0.1)

        ledCounterAudio += 1
        if ledCounterAudio > 2:
            ledCounterAudio = 1

        if ledCounterAudio == 1:
            pixels[2] = Green
            pixels[3] = Green
            pixels.show()

        if ledCounterAudio == 2:
            pixels[2] = Red
            pixels[3] = Red

        pixels.show()
        touched = time.monotonic()

    if touch2.value:  # If touch pad 1 is touched...
        while touch1.value:  # Wait for release...
            time.sleep(0.1)
        print("Video off")  # Then send key press.)
        keyboard.send(Keycode.ALT, Keycode.V)
        ledCounterVideo += 1
        if ledCounterVideo > 2:
            ledCounterVideo = 1

        if ledCounterVideo == 1:
            pixels[0] = Green
            pixels[1] = Green
            pixels.show()

        if ledCounterVideo == 2:
            pixels[0] = Red
            pixels[1] = Red

        pixels.show()
        touched = time.monotonic()
