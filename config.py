import machine

STOP_ID = 'HSL:1040144'
OLED_WIDTH, OLED_HEIGHT = 128,64
OLED_WIDTH_CHARS, OLED_HEIGHT_CHARS = OLED_WIDTH // 8, OLED_HEIGHT // 8

# for the esp8266 boards I've been using
#OLED_I2C = machine.I2C(sda=machine.Pin(4), scl=machine.Pin(5))

# for one of the esp32 boards I've been using
#OLED_I2C = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))
raise ImportError('Pick OLED I2C in config.py!')


raise ImportError('Define SSID and WPAKEY in config.py')
SSID = 'ssid_here'
WPAKEY = 'key_here'
