from hardware import *
from data.menu import *


if __name__ == "__main__":

    axp.screen_breath(10)

    lcd.orient(lcd.LANDSCAPE)
    lcd.set_bg(0xFF8000)

    # Boot on Menu.
    Menu()
