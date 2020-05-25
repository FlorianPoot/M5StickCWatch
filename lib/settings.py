from hardware import *
import time_input


class Settings:

    def __init__(self):

        time = time_input.TimeInput(title="Set time")
        rtc.set_time(*time.values)

        date = time_input.TimeInput(title="Set date", date=True)

        date.values.reverse()
        date.values.append(0)
        date.values[0] += 2000

        rtc.set_date(*date.values)
