// Create a light strip with 256 WS2811 LEDs on GP3 (GPIO03)
let strip = light.createStrip(pins.GP3, 256);

// Set brightness
strip.setBrightness(50);

// Show a simple animation: a cycling rainbow
forever(function () {
    strip.showRainbow();
    strip.rotate(1);
    pause(50);
});
