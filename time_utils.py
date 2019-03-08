import utime
import ntptime

UTC_OFFSET_SECONDS = 2 * 60 * 60 # Helsinki, 2 hours (2*60*60 seconds)
# micropython epoch is from 2000-01-01 instead of 1970-01-01
EPOCH_OFFSET = 946684800

def time():
    return utime.time() + EPOCH_OFFSET

def localtime():
    return utime.localtime((time() + UTC_OFFSET_SECONDS) - EPOCH_OFFSET)

def format_time(time_struct):
    hour,minute = time_struct[3:5]
    return '{:02}:{:02}'.format(hour, minute)

def format_date(time_struct):
    year,month,day = time_struct[0:3]
    return '{:04}-{:02}-{:02}'.format(year, month, day)

def init_time():
    ntptime.settime()
