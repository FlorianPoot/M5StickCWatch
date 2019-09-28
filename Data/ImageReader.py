from m5stack import *

import Data.Menu
import os


class ImageReader:

    def __init__(self):

        """Read images from ImageReader_Data"""

        self.images = os.listdir("Libraries/Images/ImageReader_Data")
        self._pos = 0

        lcd.clear(0xFF8000)

        buttonA.wasPressed(callback=Data.Menu.Menu)
        buttonB.wasPressed(callback=self.next_image)

        self.next_image()

    def next_image(self):

        """Display next image."""

        lcd.image(0, 0, "Libraries/Images/ImageReader_Data/" + self.images[self.pos])
        self.pos += 1

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        if self._pos + value > len(self.images):
            self._pos = 0
        else:
            self._pos = value
