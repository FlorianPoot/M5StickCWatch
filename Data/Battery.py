from m5stack import *
from machine import Timer

import Data.Menu


class Battery:

    def __init__(self):

        """Initialize Battery."""

        self.vbat = int()

        lcd.clear(0xFF8000)

        buttonA.wasPressed(callback=self.exit)
        buttonB.wasPressed(callback=lambda: None)

        self.show_battery()

        self.refresh = Timer(0)
        self.refresh.init(period=10000, mode=Timer.PERIODIC, callback=self.show_battery)

    def show_battery(self, t=None):

        """Convert battery voltage into bars."""

        self.vbat = self.map_value(axp.getVbatData() * 1.1, 3000, 4100, 0, 6)
        print(axp.getVbatData() * 1.1)
        print(self.vbat)

        if axp.getIChargeData() / 2 > 0:
            color = lcd.YELLOW
        elif self.vbat == 1:
            color = lcd.RED
        elif self.vbat == 2:
            color = lcd.ORANGE
        else:
            color = lcd.GREEN

        # Battery Icon.
        lcd.fillRect(22, 10, 125, 60, lcd.BLACK)
        lcd.fillRect(12, 30, 10, 20, lcd.BLACK)

        # Reset bars.
        lcd.fillRect(127, 15, 15, 50, lcd.BLACK)
        lcd.fillRect(107, 15, 15, 50, lcd.BLACK)
        lcd.fillRect(87, 15, 15, 50, lcd.BLACK)
        lcd.fillRect(67, 15, 15, 50, lcd.BLACK)
        lcd.fillRect(47, 15, 15, 50, lcd.BLACK)
        lcd.fillRect(27, 15, 15, 50, lcd.BLACK)

        # Draw bars.
        if self.vbat >= 1:
            lcd.fillRect(127, 15, 15, 50, color)
        if self.vbat >= 2:
            lcd.fillRect(107, 15, 15, 50, color)
        if self.vbat >= 3:
            lcd.fillRect(87, 15, 15, 50, color)
        if self.vbat >= 4:
            lcd.fillRect(67, 15, 15, 50, color)
        if self.vbat >= 5:
            lcd.fillRect(47, 15, 15, 50, color)
        if self.vbat >= 6:
            lcd.fillRect(27, 15, 15, 50, color)

    def exit(self):

        """De-init timer and exit."""

        self.refresh.deinit()

        # Return to menu
        return Data.Menu.Menu()

    @staticmethod
    def map_value(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
