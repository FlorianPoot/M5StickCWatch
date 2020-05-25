from hardware import *

import menu
import time


class TimeInput:

    def __init__(self, title, date=False):

        self.exit = False
        self.date = date

        self.values = [0, 0, 0]

        self.index = 0

        lcd.clear()
        lcd.font("data/fonts/arial16.fon")

        lcd.text(lcd.CENTER, 10, title, lcd.WHITE)

        lcd.font("data/fonts/ariblk28.fon")

        self.display_text()

        while not self.exit:

            if buttonA.was_pressed:
                self.next()
            elif buttonB.was_pressed:
                self.set_number()

            time.sleep_ms(100)

    def display_text(self):

        for i in range(3):
            if self.date and i < 2:
                lcd.text((i * 50) + 10, lcd.CENTER, "%02d" % self.values[i] + 1, lcd.WHITE if self.index == i else lcd.LIGHTGREY)
            else:
                lcd.text((i * 50) + 10, lcd.CENTER, "%02d" % self.values[i], lcd.WHITE if self.index == i else lcd.LIGHTGREY)

        for i in range(1, 3):
            lcd.text(50 * i, lcd.CENTER, ":" if not self.date else "-", lcd.WHITE)

    def set_number(self):

        while buttonB.is_pressed:
            self.values[self.index] += 1
            if self.index == 0:
                self.values[self.index] %= 24 if not self.date else 31
            elif self.index == 1:
                self.values[self.index] %= 60 if not self.date else 12
            else:
                self.values[self.index] %= 60 if not self.date else 100

            lcd.text((self.index * 50) + 10, lcd.CENTER, "%02d" % self.values[self.index], lcd.WHITE)

            time.sleep_ms(200)

    def next(self):

        self.index += 1

        if self.index >= 3:
            self.exit = True
        else:
            self.display_text()
