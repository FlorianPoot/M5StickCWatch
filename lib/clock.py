from hardware import *
from machine import Timer


class Clock:

    def __init__(self):

        """Set buttons callback, timer, colors and fonts."""

        # rtc.set_date(2020, 3, 18, 3)
        # rtc.set_time(15, 36, 00)

        self.exit = False
        self.date = -1

        lcd.clear()
        lcd.font("data/fonts/ariblk28.fon")  # Time font.

        self.show_time_and_date()

        self.time = Timer(0)
        self.time.init(period=1000, mode=Timer.PERIODIC, callback=self.show_time_and_date)

        while not self.exit:
            if buttonA.was_pressed:
                # Deinit timer and exit.
                self.time.deinit()
                self.exit = True

    def show_time_and_date(self, t=None):

        """Display time, display date only when it change."""

        current_time = rtc.get_time()
        current_date = rtc.get_date()

        lcd.text(lcd.CENTER, 20, "%02d:%02d:%02d" % current_time, color=lcd.WHITE)

        if current_date[2] != self.date:
            lcd.font("data/fonts/arial16.fon")

            lcd.textClear(lcd.CENTER, 55, "00-00-00")
            lcd.text(lcd.CENTER, 55, "%02d-%02d-%02d" % (current_date[2] + 1, current_date[1] + 1, current_date[0]), color=lcd.WHITE)

            lcd.font("data/fonts/ariblk28.fon")  # Restore Time font.

            self.date = current_date[2]
