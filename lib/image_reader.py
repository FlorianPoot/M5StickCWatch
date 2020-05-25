from hardware import *
import os


class ImageReader:

    def __init__(self):

        """Read images from ImageReader_Data"""

        self.images = os.listdir("data/images/ImageReader_Data")
        self._pos = 0
        self.exit = False

        lcd.clear()

        self.next_image()

        while not self.exit:
            if buttonA.was_pressed:
                self.exit = True
            elif buttonB.was_pressed:
                self.next_image()

    def next_image(self):

        """Display next image."""

        lcd.image(0, 0, "data/images/ImageReader_Data/" + self.images[self.pos])
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
