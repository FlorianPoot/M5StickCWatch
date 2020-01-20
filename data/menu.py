from m5stack import *

import data.clock
import data.battery
import data.image_reader

import time


class Menu:

    def __init__(self):

        """Initialize Menu."""

        # (Application, Icon).
        self.apps = ((data.clock.Clock, "Clock"),
                     (data.battery.Battery, "Battery"),
                     (data.image_reader.ImageReader, "ImageReader"),
                     (None, "Settings"))

        self._pos = 0

        buttonA.wasPressed(callback=self.select)

        self.refresh()

    def refresh(self):

        """Clear and draw yellow rectangles."""

        lcd.clear(0xFF8000)
        for i in range(3):
            lcd.roundrect(2 + (i * 53), 4, 50, 72, 8, color=lcd.YELLOW, fillcolor=lcd.YELLOW)

        self.select()

    def menu(self, menu_pos=0):

        """Draw Menu's icons."""

        for i in range(3):
            lcd.image(2 + (i * 53), lcd.CENTER, "data/images/" + self.apps[i + menu_pos][1] + ".jpg")

    def select(self):

        """Draw BLACK outline and set callback to current selected item."""

        if self.pos % 3 == 0:
            self.menu(menu_pos=int(self.pos / 3))

        if self.apps[self.pos][0] is None:
            buttonB.wasPressed(callback=self.not_implemented)
        else:
            buttonB.wasPressed(callback=self.apps[self.pos][0])

        for i in range(3):
            if i == min(self.pos, 2):
                lcd.roundrect(2 + (i * 53), 4, 50, 72, 8, color=lcd.BLACK)
                lcd.roundrect(3 + (i * 53), 5, 48, 70, 7, color=lcd.BLACK)
            else:
                lcd.roundrect(2 + (i * 53), 4, 50, 72, 8, color=lcd.YELLOW)
                lcd.roundrect(3 + (i * 53), 5, 48, 70, 7, color=lcd.YELLOW)

        self.pos += 1

    def not_implemented(self):

        """When functionality is not implemented yet."""

        lcd.clear(0xFF8000)
        lcd.font("data/fonts/arial16.fon", transparent=True)

        lcd.print("Not implemented", lcd.CENTER, 25)
        lcd.print("yet", lcd.CENTER, 45)

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
