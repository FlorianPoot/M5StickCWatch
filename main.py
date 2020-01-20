from m5stack import *
from data.menu import *


if __name__ == "__main__":

    axp.screenBreath(10)
    lcd.orient(lcd.LANDSCAPE)

    # Boot on Menu.
    Menu()
