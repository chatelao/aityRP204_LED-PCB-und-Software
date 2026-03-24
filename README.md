# Aity Kids 4-LED Board

This project provides a simple 4-LED board powered by a Seeed Studio XIAO RP2040 (or compatible XIAO module). It includes examples for both CircuitPython and Microsoft MakeCode Maker.

## Hardware Configuration

- **Microcontroller**: Seeed Studio XIAO RP2040.
- **NeoPixel Data Pin**: Connected to **D10** (which corresponds to **GP3** on the RP2040).
- **LED Matrix**: Configured for a 16x16 matrix (256 LEDs) in the provided examples.

<img width="616" height="432" alt="image" src="https://github.com/user-attachments/assets/f364a9d5-ba34-4fb9-b765-a625a0828113" />


## Preparing the XIAO RP2040

To flash new firmware (CircuitPython or MakeCode) to the XIAO RP2040, you must first enter **Bootloader Mode**:

1. Connect the XIAO RP2040 to your computer via USB.
2. Press and hold the **BOOT** button (labeled 'B').
3. While holding **BOOT**, press the **RESET** button (labeled 'R') once, or plug in the USB cable.
4. Release the **BOOT** button.
5. A new drive named `RPI-RP2` should appear on your computer.

---

## CircuitPython (CPy) Installation

### 1. Install CircuitPython Firmware
1. Download the latest CircuitPython UF2 file for the **Seeeduino XIAO RP2040** from [circuitpython.org](https://circuitpython.org/board/seeeduino_xiao_rp2040/).
2. Enter Bootloader Mode (see above) so the `RPI-RP2` drive appears.
3. Drag and drop the downloaded UF2 file onto the `RPI-RP2` drive.
4. The board will reboot, and a new drive named `CIRCUITPY` will appear.

### 2. Install Libraries
CircuitPython requires external libraries to run the example.
1. Download the [CircuitPython Library Bundle](https://circuitpython.org/libraries).
2. Create a `lib` folder on your `CIRCUITPY` drive if it doesn't exist.
3. Copy the following folders/files from the bundle to the `lib` folder:
   - `adafruit_neopixel.mpy` (or the folder)
   - `adafruit_imageload` (folder)
   - `adafruit_display_text` (if needed by future expansions)

### 3. Deploy the Code
1. Copy the `code.py` file from the root of this repository to the `CIRCUITPY` drive.
2. If the code requires an image, copy `image.png` to the root of the `CIRCUITPY` drive.
3. The board will automatically reload and start running the script.

---

## MakeCode Installation

Microsoft MakeCode Maker provides a block-based and TypeScript editor for the RP2040.

### 1. Open the Project
1. Go to [Microsoft MakeCode Maker](https://maker.makecode.com).
2. Click on **Import**, then select **Import File...**.
3. Choose the `makecode/pxt.json` or `makecode/main.ts` file from this repository.
4. When prompted, select **Seeed Studio XIAO RP2040** as your board.

### 2. Download and Flash
1. Click the **Download** button in the MakeCode editor.
2. It will generate a `.uf2` file.
3. Enter Bootloader Mode (see above) on your XIAO RP2040.
4. Drag and drop the downloaded UF2 file onto the `RPI-RP2` drive.
5. The board will reboot and immediately begin running your MakeCode program.
