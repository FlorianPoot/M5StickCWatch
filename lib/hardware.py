import display
import axp192
import rtc
import button

# Power
axp = axp192.Axp192()
axp.power_all()

# Real Time Clock
rtc = rtc.RTC()

# Display
lcd = display.TFT()
lcd.init(lcd.M5STICK, width=80, height=160, rst_pin=18, miso=36, mosi=15, clk=13, cs=5, dc=23, bgr=True, speed=30000000, splash=False)

# Buttons
buttonA = button.Button(39)
buttonB = button.Button(37)
