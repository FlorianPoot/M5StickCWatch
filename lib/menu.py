from hardware import *

import clock
import battery
import image_reader
import settings
import time


class Menu:

    def __init__(self):

        """Initialize Menu."""

        # (Application, Icon).
        self.apps = ((clock.Clock, "Clock"),
                     (battery.Battery, "Battery"),
                     (image_reader.ImageReader, "ImageReader"),
                     (settings.Settings, "Settings"))

        self._pos = 0

        self.refresh()
        self.select()

        while True:
            if buttonA.was_pressed:
                self.pos += 1
                self.select()
            elif buttonB.was_pressed:
                if self.apps[self.pos][0] is None:
                    self.not_implemented()
                else:
                    self.apps[self.pos][0]()

                    self.refresh()
                    self.select()

            time.sleep_ms(10)

    def refresh(self, only_icons=False):

        """Clear and draw yellow rectangles."""

        if not only_icons:
            lcd.clear()
            for i in range(3):
                lcd.roundrect(2 + (i * 53), 4, 50, 72, 8, color=lcd.YELLOW, fillcolor=lcd.YELLOW)

        for i in range(3):
            lcd.image(2 + (i * 53), lcd.CENTER, "data/images/" + self.apps[i + int(self.pos / 3)][1] + ".jpg")

    def select(self):

        """Draw BLACK outline."""

        if self.pos % 3 == 0:
            self.refresh(only_icons=True)

        for i in range(3):
            if i == min(self.pos, 2):
                lcd.roundrect(2 + (i * 53), 4, 50, 72, 8, color=lcd.BLACK)
                lcd.roundrect(3 + (i * 53), 5, 48, 70, 7, color=lcd.BLACK)
            else:
                lcd.roundrect(2 + (i * 53), 4, 50, 72, 8, color=lcd.YELLOW)
                lcd.roundrect(3 + (i * 53), 5, 48, 70, 7, color=lcd.YELLOW)

    def not_implemented(self):

        """When functionality is not implemented yet."""

        lcd.clear()
        lcd.font("data/fonts/arial16.fon")

        lcd.text(lcd.CENTER, 25, "Not implemented", color=lcd.WHITE)
        lcd.text(lcd.CENTER, 45, "yet", color=lcd.WHITE)

        time.sleep(2)

        self.refresh()

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        if self._pos + value > len(self.apps) + 1:
            self._pos = 0
        else:
            self._pos = value
