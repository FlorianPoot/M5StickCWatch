# M5StickCWatch

## Functionality
* Menu: where can be found the Clock, Battery and Image Reader. (Later, there will be a Settings icon for set clock and date)
* Clock: for reading time and date.
* Battery: you can see the battery level here. Also battery have different colors depending on the level of the battery (Green for high charge, Orange for middle charge, Red when almost empty and Yellow when charging).
* Image Reader: display images from Libraries/Images/ImageReader_Data/

## How to use it
* Flash the firmware from.firmware-M5StickC/ into a M5Stick C.
* Set time and date in Data/Clock.py by uncomment the two corresponding field in __init__().
* Put main.py + Data/ + Libraries/ into the filesystem. (You can use Ampy or PyCharm with MicroPython plugin)
* Reboot the M5Stick C and that's all !

## Images
<img src="https://raw.githubusercontent.com/FlorianPoot/M5StickCWatch/master/Images/img1.jpg" width="425"/> <img src="https://raw.githubusercontent.com/FlorianPoot/M5StickCWatch/master/Images/img2.jpg" width="425"/>
<img src="https://raw.githubusercontent.com/FlorianPoot/M5StickCWatch/master/Images/img3.jpg" width="425"/> <img src="https://raw.githubusercontent.com/FlorianPoot/M5StickCWatch/master/Images/img4.jpg" width="425"/>
