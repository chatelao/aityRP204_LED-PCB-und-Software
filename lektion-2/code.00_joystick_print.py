import board
import digitalio
import time

# Pin-Konfiguration für den Arcade-Controller
# Wir verwenden interne Pull-Up Widerstände, daher ist der Wert 'False', wenn gedrückt.
# Mapping: Oben=D2, Unten=D3, Links=D1, Rechts=D0

pins = {
    "Oben": board.D2,
    "Unten": board.D3,
    "Links": board.D1,
    "Rechts": board.D0
}

# Initialisierung der Eingabestifte
inputs = {}
for name, pin in pins.items():
    io = digitalio.DigitalInOut(pin)
    io.direction = digitalio.Direction.INPUT
    io.pull = digitalio.Pull.UP
    inputs[name] = io

print("Arcade-Joystick Test")
print("Bewege den Joystick!")

while True:
    active = []
    for name, io in inputs.items():
        if not io.value: # Signal ist LOW, wenn gedrückt
            active.append(name)

    if active:
        print("Aktiv: " + ", ".join(active))

    time.sleep(0.1)
