import machine

STOP_ID = 'HSL:1040144'
HAS_RTC = hasattr(machine, 'RTC')
OLED_WIDTH, OLED_HEIGHT = 128,64
OLED_WIDTH_CHARS, OLED_HEIGHT_CHARS = OLED_WIDTH // 8, OLED_HEIGHT // 8
raise ImportError('Define SSID and WPAKEY in config.py')
SSID = 'ssid_here'
WPAKEY = 'key_here'
