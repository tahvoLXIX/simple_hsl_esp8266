import network
import usocket, ussl, utime
import machine, ssd1306
import ujson


import config
import time_utils
import qry

i2c = machine.I2C(sda=machine.Pin(4), scl=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(config.OLED_WIDTH, config.OLED_HEIGHT, i2c)
oled.fill(0)
oled.text('connecting', 0, 4)
oled.show()

sta_if = network.WLAN(network.STA_IF)
sta_if.active(1)

sta_if.connect(config.SSID, config.WPAKEY)
for n in range(0,8):
    oled.fill_rect(0,18,config.OLED_WIDTH,30,0)
    oled.text('{}'.format(8-n), 20,19)
    oled.show()
    utime.sleep(1)

oled.fill(0)
oled.text('connected', 0, 4)
oled.text(sta_if.ifconfig()[0], 0, 10)
oled.show()

time_utils.init_time()

N_ITEMS = 4
DELAY_BETWEEN_CHECKS = 20

def main():
    fmt_str = '{: <' + str(config.OLED_WIDTH_CHARS//2) + '}{: >' + str(config.OLED_WIDTH_CHARS//2) + '}'
    while True:
        t = time_utils.time()
        output = []
        if config.OLED_WIDTH_CHARS > 8:
            output.append('time {}'.format(time_utils.format_time(time_utils.localtime())))
        else:
            output.append('{}'.format(time_utils.format_time(time_utils.localtime())))
        res = qry.transform_response(qry.doit(t))
        for item in res[:N_ITEMS]:
            buss_name = item['trip']['route']['shortName']
            print(item)
            ts_of_departure = (item['serviceDay']+item['realtimeDeparture']) - t
            if ts_of_departure < 0:
                output('{} XXX'.format(buss_name))
            minutes_to_departure = ts_of_departure // 60
            seconds_to_departure = ts_of_departure % 60
            output.append(fmt_str.format(buss_name, minutes_to_departure))
        if output:
            oled.fill(0)
            y = 4
            for line in output:
                print(line)
                oled.text(line, 0, y)
                y+=9
            oled.show()
        utime.sleep(DELAY_BETWEEN_CHECKS)


main()
# EOF
