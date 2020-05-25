from hardware import *
from menu import *


if __name__ == "__main__":

    axp.screen_breath(10)

    lcd.orient(lcd.LANDSCAPE)
    lcd.set_bg(0xFF8000)

    # DEBUG mode
    if buttonA.is_pressed or buttonB.is_pressed:
        lcd.font("data/fonts/ariblk28.fon")

        lcd.clear()
        lcd.text(lcd.CENTER, 30, "DEBUG", color=lcd.WHITE)
    else:
        # Start on Menu.
        Menu()
