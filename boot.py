import network
import usocket, ussl, utime
import machine, ssd1306
import ujson


import config
import time_utils
import qry
import utils

oled = ssd1306.SSD1306_I2C(config.OLED_WIDTH, config.OLED_HEIGHT, config.OLED_I2C)

sta_if = network.WLAN(network.STA_IF)
sta_if.active(1)

sta_if.connect(config.SSID, config.WPAKEY)

for n in range(0,10):
    oled.fill(0)
    utils.oled_ml_msg('trying to connect {} sec left..'.format(10-n), oled)
    utime.sleep(1)

utils.oled_ml_msg('connected {}'.format(sta_if.ifconfig()[0]), oled)

time_utils.init_time()

N_ITEMS = 4
DELAY_BETWEEN_CHECKS = 20

def main():
    fmt_str = '{: <' + str(config.OLED_WIDTH_CHARS//2) + '}{: >' + str(config.OLED_WIDTH_CHARS//2) + '}'
    while True:
        try:
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
        except Exception as ex:
            print(ex)
            utils.oled_ml_msg(str(ex), oled)
        utime.sleep(DELAY_BETWEEN_CHECKS)


main()
# EOF
