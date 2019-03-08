import config
def oled_ml_msg(msg, oled, start_y=4, clear=True):
    if clear:
        oled.fill(0)
    # truncate msg
    tmsg = msg[:config.OLED_WIDTH_CHARS*(config.OLED_HEIGHT_CHARS-1)]
    n = 0
    while n <= len(tmsg):
        s = tmsg[n:n+config.OLED_WIDTH_CHARS]
        oled.text(s, 0, start_y)
        start_y += 8
        print(s)
        n += config.OLED_WIDTH_CHARS
    oled.show()


