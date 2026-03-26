import board, neopixel
pixels = neopixel.NeoPixel(board.D10, 1, brightness=0.05, auto_write=True)
pixels[0] = (128, 0, 128) # Ein dezentes Lila
