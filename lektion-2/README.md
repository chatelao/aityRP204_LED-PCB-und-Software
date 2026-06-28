# Lektion 2: Arcade Controller

In dieser Lektion lernst du, wie du einen Arcade-Joystick an dein Board anschliesst und damit die LED-Matrix steuerst. Wir werden Schritt für Schritt von einfachen Eingabetests bis hin zu einem kleinen Spiel gehen.

## Hardware-Aufbau

Verbinde deinen Arcade-Joystick gemäss der folgenden Tabelle mit dem XIAO RP2040. Die meisten Arcade-Joysticks schliessen den Pin gegen Masse (GND), wenn sie in eine Richtung bewegt werden. Wir nutzen im Code die internen Pull-Up-Widerstände des XIAO.

### Anschlussplan

<img width="313" height="216" alt="image" src="https://github.com/user-attachments/assets/f364a9d5-ba34-4fb9-b765-a625a0828113" />



| Arcade-Eingang | XIAO Pin | GP-Nummer |
| :--- | :--- | :--- |
| Joystick Oben | **D0** | GP26 |
| Joystick Unten | **D1** | GP27 |
| Joystick Links | **D4** | GP06 |
| Joystick Rechts | **D5** | GP07 |
| Gemeinsame Masse | **GND** | GND |

---

## Übungen

Um eine Übung auszuführen, benenne die entsprechende Datei in `code.py` um und kopiere sie auf deinen Microcontroller.

### 1. Hardware-Test (`code.00_joystick_print.py`)
Dieses Skript ist ein einfacher Test, um sicherzustellen, dass alles korrekt verkabelt ist.
- Bewege den Joystick.
- Öffne den seriellen Monitor in deinem Editor (z.B. Mu Editor oder VS Code), um die Ausgabe zu sehen.
- Wenn du eine Richtung bewegst, sollte der entsprechende Name in der Konsole erscheinen.

### 2. Pixel bewegen (`code.01_pixel_move.py`)
Jetzt bringen wir Bewegung auf die LED-Matrix!
- Ein einzelner weisser Punkt erscheint in der Mitte der 16x16 Matrix.
- Mit dem Joystick kannst du den Punkt in alle vier Richtungen steuern.
- Das Programm sorgt dafür, dass der Punkt nicht über den Rand der Matrix hinausläuft.

### 3. Mini-Spiel: Fang das Pixel (`code.10_mini_game.py`)
Zum Abschluss programmieren wir ein einfaches Spiel.
- Du steuerst einen **blauen** Punkt.
- Ein **roter** Punkt (das Ziel) erscheint an einer zufälligen Stelle.
- Deine Aufgabe: Bewege den blauen Punkt zum roten Punkt, um ihn zu "fangen".
- Jedes Mal, wenn du das Ziel erreichst, bekommst du einen Punkt (sichtbar in der Konsole) und ein neues Ziel erscheint.

Viel Spass beim Spielen und Experimentieren!
