# simple HSL buss-information display using MicroPython on esp32/8266
Inspired the work of [@stetro](https://github.com/stetro). 

## requirements
 * SSD1306 based oled display
 * ESP32/ESP8266 microcontroller
 * python
 * micropython firmware

## installation & configuration
Clone the repository. Insert ssid / wpa-key information into `config.py`. Set correct I2C settings (pins) for `OLED_I2C`.

`STOP_ID` in config.py is currently pointing at a stop in Kamppi, Helsinki. Change it as appropriate.

Setup a python virtualenv and install `esptool` and `adafruit-ampy` into it.

 * [ampy](https://github.com/pycampers/ampy)
 * [esptool](https://github.com/espressif/esptool)

Download MicroPython firmware from [here](http://micropython.org/download) and install the firmware using esptool, as per instructions on the MicroPython site.

Copy the python files from this repo to the microcontroller using ampy. The order is somewhat significant, the following order should work (change the `/dev/ttyUSB0` device to whatever you have):

    ampy -p /dev/ttyUSB0 config.py
    ampy -p /dev/ttyUSB0 utils.py
    ampy -p /dev/ttyUSB0 qry.py
    ampy -p /dev/ttyUSB0 time_utils.py
    ampy -p /dev/ttyUSB0 ssd1306.py
    ampy -p /dev/ttyUSB0 boot.py

