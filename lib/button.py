from machine import Pin


class Button:

    def __init__(self, pin):

        self.pin = Pin(pin, mode=Pin.IN, handler=self.handler, trigger=Pin.IRQ_FALLING, debounce=100)
        self._was_pressed = False

    def handler(self, pin):
        self._was_pressed = True

    @property
    def is_pressed(self):
        return not self.pin.value()

    @property
    def was_pressed(self):
        if self._was_pressed:
            self._was_pressed = False
            return True
        else:
            return False
