import board
import neopixel

# Konfiguration: Pin D10 wird für die NeoPixel auf dem XIAO ESP32C3/RP2040 verwendet
pixel_pin = board.D10
num_pixels = 10

# Initialisierung der NeoPixel
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=True)

# Alle 10 LEDs auf Orange setzen
pixels.fill((255, 100, 0))
