# M5StickC Watch

## Features
* Menu: where can be found the Clock, Battery, Image Reader and Settings
* Clock: for reading time and date.
* Battery: you can see the battery level here. Also battery have different colors depending on the level of the battery (Green for high charge, Orange for middle charge, Red when almost empty and Yellow when charging).
* Image Reader: display images from data/images/ImageReader_Data/
* Settings: set time and date.

## How to use it
* First erase flash
```
esptool.py --chip esp32 --port <YOUR_PORT> erase_flash
```
* Flash the firmware from .firmware-M5StickC/ into a M5Stick C.
```
esptool.py --chip esp32 --port <YOUR_PORT> --baud 750000 write_flash -z 0x1000 bootloader.bin 0x10000 MicroPython.bin 0x8000 partitions_mpy.bin 0xf000 phy_init_data.bin
```
If you use the backup firmware:
```
esptool.py --chip esp32 --port <YOUR_PORT> --baud 750000 write_flash 0x0000 M5StickCWatch.bin
```
* Put "main.py" + "data/" + "lib/" into the filesystem. (You can skip this step if you use the backup firmware)
```
ampy --port <YOUR_PORT> put main.py
ampy --port <YOUR_PORT> mkdir data
ampy --port <YOUR_PORT> put data/fonts data/fonts
ampy --port <YOUR_PORT> put data/images data/images
ampy --port <YOUR_PORT> put lib/
```
*You can also use AmpyGUI: https://github.com/FlorianPoot/AmpyGUI*

* Reboot the M5StickC and that's all !

## Images
<img src="https://raw.githubusercontent.com/FlorianPoot/M5StickCWatch/master/.images/img1.jpg" width="425"/> <img src="https://raw.githubusercontent.com/FlorianPoot/M5StickCWatch/master/.images/img2.jpg" width="425"/>
<img src="https://raw.githubusercontent.com/FlorianPoot/M5StickCWatch/master/.images/img3.jpg" width="425"/> <img src="https://raw.githubusercontent.com/FlorianPoot/M5StickCWatch/master/.images/img4.jpg" width="425"/>
