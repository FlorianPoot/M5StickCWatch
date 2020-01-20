from m5stack import *
from machine import Timer

import data.menu


class Clock:

    def __init__(self):

        """Set buttons callback, timer, colors and fonts."""

        # rtc.setDate(2019, 9, 28, 6)
        # rtc.setTime(15, 37, 00)

        self.date = -1

        lcd.clear(0xFF8000)
        lcd.font("data/fonts/ariblk28.fon", transparent=False)  # Time font.
        lcd.setTextColor(color=lcd.WHITE, bcolor=0xFF8000)

        buttonA.wasPressed(callback=self.exit)
        buttonB.wasPressed(callback=lambda: None)

        self.show_time_and_date()

        self.time = Timer(0)
        self.time.init(period=1000, mode=Timer.PERIODIC, callback=self.show_time_and_date)

    def show_time_and_date(self, t=None):

        """Display time, display date only when it change."""

        current_time = rtc.getTime()
        lcd.print("%02d:%02d:%02d" % current_time, lcd.CENTER, 20)

        current_date = rtc.getDate()
        if current_date[2] != self.date:
            lcd.font("data/fonts/arial16.fon")
            lcd.print("%02d-%02d-%02d" % (current_date[2], current_date[1], current_date[0]), lcd.CENTER, 55)
            lcd.font("data/fonts/ariblk28.fon")  # Restore Time font.

            self.date = current_date[2]

    def exit(self):

        """De-init timer and exit."""

        self.time.deinit()

        # Return to menu
        return data.menu.Menu()
