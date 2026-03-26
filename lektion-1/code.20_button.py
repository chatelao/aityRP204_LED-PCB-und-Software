import board
import neopixel
import digitalio
import time

# NeoPixel Konfiguration
pixel_pin = board.D10
pixels = neopixel.NeoPixel(pixel_pin, 1, brightness=0.1, auto_write=True)

# Button Konfiguration (Passe den Pin an, falls nötig, z.B. D0)
button_pin = board.D0
button = digitalio.DigitalInOut(button_pin)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # Interner Pull-Up Widerstand

print("Drücke den Knopf, um die LED-Farbe zu ändern!")

while True:
    if not button.value: # Wenn der Knopf gedrückt wird (Low-Signal wegen Pull-Up)
        pixels[0] = (0, 255, 0) # Grün
    else:
        pixels[0] = (255, 0, 0) # Rot

    time.sleep(0.01) # Kurze Pause zum Entprellen
