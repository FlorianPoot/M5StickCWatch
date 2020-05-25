from hardware import *
import time_input


class Settings:

    def __init__(self):

        time = time_input.TimeInput(title="Set time")
        date = time_input.TimeInput(title="Set date", date=True)

        rtc.set_time(*time.values)
        rtc.set_date(*date.values.reverse(), 0)
