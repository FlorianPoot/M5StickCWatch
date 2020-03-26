from hardware import *
from machine import Timer

import data.menu
import time


class Battery:

    def __init__(self):

        """Initialize Battery."""

        self.bar_pos = 0

        lcd.clear()
        lcd.font("data/fonts/aril24.fon")
        lcd.set_bg(lcd.BLACK)

        buttonA.was_pressed(callback=self.exit)
        buttonB.clear()

        # Battery icon.
        lcd.rect(12, 22, 10, 16, lcd.BLACK, lcd.BLACK)
        # Percentage rectangle.
        lcd.roundrect(45, 58, 70, 20, 8, lcd.BLACK, lcd.BLACK)

        self.refresh = Timer(0)
        self.refresh.init(period=10000, mode=Timer.PERIODIC, callback=self.show_battery)

        self.show_battery()

    def show_battery(self, t=None):

        """Convert battery voltage into bars."""

        if axp.get_icharge_data() / 2 > 0:
            # If pluged in.
            self.refresh.period(500)

            if self.bar_pos == 0:
                # Battery Icon.
                lcd.rect(22, 5, 125, 50, lcd.BLACK, lcd.BLACK)

                lcd.roundrect(45, 58, 70, 20, 8, lcd.BLACK, lcd.BLACK)
                lcd.text(lcd.CENTER, 63, "--%", lcd.WHITE)

            else:
                lcd.rect(((6 - self.bar_pos) * 20) + 27, 10, 15, 40, lcd.GREEN, lcd.GREEN)

            self.bar_pos += 1
            self.bar_pos %= 7

        else:
            self.refresh.period(10000)

            bat_data = axp.get_vbat_data() * 1.1

            vbat = round(self.map_value(bat_data, 3000, 4100, 0, 7))
            pbat = max(min(round(self.map_value(bat_data, 3000, 4100, 0, 100)), 100), 0)

            print(bat_data)
            print(vbat)
            print(pbat)

            # Battery Icon.
            lcd.rect(22, 5, 125, 50, lcd.BLACK, lcd.BLACK)

            if vbat == 1:
                color = lcd.RED
            elif vbat == 2:
                color = lcd.ORANGE
            else:
                color = lcd.GREEN

            # Draw bars.
            for i in range(1, 7):
                if vbat >= i:
                    lcd.rect(((6 - i) * 20) + 27, 10, 15, 40, color, color)

            lcd.roundrect(45, 58, 70, 20, 8, lcd.BLACK, lcd.BLACK)
            lcd.text(lcd.CENTER, 63, str(pbat) + "%", lcd.WHITE)

    def exit(self):

        """De-init timer and exit."""

        self.refresh.deinit()
        lcd.set_bg(0xFF8000)

        # Return to menu
        return data.menu.Menu()

    @staticmethod
    def map_value(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
