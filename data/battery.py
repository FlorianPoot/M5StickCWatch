from hardware import *
from machine import Timer

import data.menu


class Battery:

    def __init__(self):

        """Initialize Battery."""

        self.vbat = int()

        lcd.clear()

        buttonA.was_pressed(callback=self.exit)
        buttonB.was_pressed(callback=lambda: None)

        self.show_battery()

        self.refresh = Timer(0)
        self.refresh.init(period=10000, mode=Timer.PERIODIC, callback=self.show_battery)

    def show_battery(self, t=None):

        """Convert battery voltage into bars."""

        self.vbat = self.map_value(axp.get_vbat_data() * 1.1, 3000, 4100, 0, 6)
        print(axp.get_vbat_data() * 1.1)
        print(self.vbat)

        if axp.get_icharge_data() / 2 > 0:
            color = lcd.YELLOW
        elif self.vbat == 1:
            color = lcd.RED
        elif self.vbat == 2:
            color = lcd.ORANGE
        else:
            color = lcd.GREEN

        # Battery Icon.
        lcd.rect(22, 10, 125, 60, lcd.BLACK, lcd.BLACK)
        lcd.rect(12, 30, 10, 20, lcd.BLACK, lcd.BLACK)

        # Reset bars.
        for i in range(6):
            lcd.rect((i * 20) + 27, 15, 15, 50, lcd.BLACK, lcd.BLACK)

        # Draw bars.
        if self.vbat >= 1:
            lcd.rect(127, 15, 15, 50, color, color)
        if self.vbat >= 2:
            lcd.rect(107, 15, 15, 50, color, color)
        if self.vbat >= 3:
            lcd.rect(87, 15, 15, 50, color, color)
        if self.vbat >= 4:
            lcd.rect(67, 15, 15, 50, color, color)
        if self.vbat >= 5:
            lcd.rect(47, 15, 15, 50, color, color)
        if self.vbat >= 6:
            lcd.rect(27, 15, 15, 50, color, color)

    def exit(self):

        """De-init timer and exit."""

        self.refresh.deinit()

        # Return to menu
        return data.menu.Menu()

    @staticmethod
    def map_value(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
