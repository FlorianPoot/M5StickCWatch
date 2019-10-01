# M5StickC Watch

## Functionality
* Menu: where can be found the Clock, Battery and Image Reader. (Later, there will be a Settings icon for set clock and date)
* Clock: for reading time and date.
* Battery: you can see the battery level here. Also battery have different colors depending on the level of the battery (Green for high charge, Orange for middle charge, Red when almost empty and Yellow when charging).
* Image Reader: display images from Libraries/Images/ImageReader_Data/

## How to use it
* First erase flash
```
esptool.py --chip esp32 --port <YOUR_PORT> erase_flash
```
* Flash the firmware from .firmware-M5StickC/ into a M5Stick C.
```
esptool.py --chip esp32 --port <YOUR_PORT> write_flash -z 0x1000 bootloader_0x1000.bin 0x10000 MicroPython_0x10000.bin 0x8000 partitions_mpy_0x8000.bin 0xf000 phy_init_data_0xf000.bin
```
* Set time and date in Data/Clock.py by uncomment the two corresponding field in __init__().
* Put main.py + Data/ + Libraries/ into the filesystem. (Warning: On Windows 
```
ampy --port <YOUR_PORT> put main.py
ampy --port <YOUR_PORT> mkdir Libraries
ampy --port <YOUR_PORT> put Libraries/Fonts Libraries/Fonts
ampy --port <YOUR_PORT> put Libraries/Images Libraries/Images
ampy --port <YOUR_PORT> put Data/
```
* Reboot the M5StickC and that's all !

## Images
<img src="https://raw.githubusercontent.com/FlorianPoot/M5StickCWatch/master/Images/img1.jpg" width="425"/> <img src="https://raw.githubusercontent.com/FlorianPoot/M5StickCWatch/master/Images/img2.jpg" width="425"/>
<img src="https://raw.githubusercontent.com/FlorianPoot/M5StickCWatch/master/Images/img3.jpg" width="425"/> <img src="https://raw.githubusercontent.com/FlorianPoot/M5StickCWatch/master/Images/img4.jpg" width="425"/>
