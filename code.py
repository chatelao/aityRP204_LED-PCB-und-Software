import board
import neopixel
import adafruit_imageload

# Matrix configuration
PIXEL_PIN = board.D10  # Data pin (Commonly used on Xiao ESP32C3)
MATRIX_WIDTH = 16      # Width of your NeoPixel matrix
MATRIX_HEIGHT = 16     # Height of your NeoPixel matrix
BRIGHTNESS = 0.1       # Adjust brightness (0.0 to 1.0)
IMAGE_FILE = "image.png" # 256x256 PNG file

# Initialize NeoPixels
num_pixels = MATRIX_WIDTH * MATRIX_HEIGHT
pixels = neopixel.NeoPixel(PIXEL_PIN, num_pixels, brightness=BRIGHTNESS, auto_write=False)

def load_and_display():
    print(f"Loading {IMAGE_FILE}...")
    try:
        # Load the PNG image
        # Returns a bitmap (indexed pixels) and a palette (colors)
        bitmap, palette = adafruit_imageload.load(IMAGE_FILE)

        print(f"Image loaded: {bitmap.width}x{bitmap.height}")

        # Display the image on the matrix with nearest-neighbor scaling
        for y in range(MATRIX_HEIGHT):
            for x in range(MATRIX_WIDTH):
                # Map matrix coordinates to image coordinates to cover full image range
                img_x = int(x * (bitmap.width - 1) / (MATRIX_WIDTH - 1))
                img_y = int(y * (bitmap.height - 1) / (MATRIX_HEIGHT - 1))

                # Get color from bitmap/palette
                color_index = bitmap[img_x, img_y]
                color = palette[color_index]

                # Map (x, y) to NeoPixel index
                # This assumes a progressive layout.
                # For zigzag layout, use:
                # if y % 2 == 1:
                #     pixel_index = y * MATRIX_WIDTH + (MATRIX_WIDTH - 1 - x)
                # else:
                #     pixel_index = y * MATRIX_WIDTH + x
                pixel_index = y * MATRIX_WIDTH + x

                pixels[pixel_index] = color

        pixels.show()
        print("Done!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    load_and_display()
