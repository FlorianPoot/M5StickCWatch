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

"""class Button:

    def __init__(self, pin, name="none", long_name="none", dbtime=20):
        self._pin = Pin(pin)
        self._pin.init(Pin.IN, handler=self.irq_cb, trigger=(Pin.IRQ_FALLING | Pin.IRQ_RISING))
        self._wasPressed_cb = None
        self._wasReleased_cb = None
        self._releasedFor_cb = None
        self._timeshoot = 0
        self._dbtime = dbtime
        self._lastState = False
        self._startTicks = 0
        self._timeout = 0
        self._name = name
        self._long_name = long_name
        self._event = 0

    def irq_cb(self, pin):
        pin_val = pin.value()
        print(pin_val)
        if self._pin == pin:
            # FALLING
            if pin_val == 0:
                if ticks_ms() - self._timeshoot > self._dbtime:
                    self._lastState = True
                    self._startTicks = ticks_ms()
                    self._event |= 0x02  # EVENT_WAS_PRESSED
                    if self._wasPressed_cb:
                        self._wasPressed_cb()
            # RISING
            elif pin_val == 1:
                if self._lastState:
                    self._lastState = False
                    self._event |= 0x04  # EVENT_WAS_RELEASED
                    if 0 < self._timeout < ticks_ms() - self._startTicks:
                        self._event = 0
                        self._event |= 0x08  # EVENT_RELEASED_FOR
                        if self._releasedFor_cb:
                            self._releasedFor_cb()
                    elif self._wasReleased_cb:
                        self._wasReleased_cb()
            self._timeshoot = ticks_ms()

    def clear(self):
        self._event = 0
        self._wasPressed_cb = None
        self._wasReleased_cb = None
        self._releasedFor_cb = None

    def read(self):
        return not self._pin.value()

    def is_pressed(self):
        return self.read()

    def is_released(self):
        return not self.read()

    def was_pressed(self, callback=None):
        if callback is None:
            if (self._event & 0x02) > 0:  # EVENT_WAS_PRESSED
                self._event -= 0x02
                return True
            else:
                return False
        else:
            self._wasPressed_cb = callback

    def was_released(self, callback=None):
        if callback is None:
            if (self._event & 0x04) > 0:  # EVENT_WAS_RELEASED
                self._event -= 0x04
                return True
            else:
                return False
        else:
            self._wasReleased_cb = callback

    def pressed_for(self, timeout):
        if self._lastState and ticks_ms() - self._startTicks > timeout * 1000:
            return True
        else:
            return False

    def released_for(self, timeout, callback=None):
        self._timeout = timeout * 1000  # second
        if callback is None:
            if (self._event & 0x08) > 0:  # EVENT_RELEASED_FOR
                self._event -= 0x08
                return True
            else:
                return False
        else:
            self._releasedFor_cb = callback"""
