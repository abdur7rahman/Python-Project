
import pywhatkit as kit
import datetime

number = "+91 96299 00038" 

now = datetime.datetime.now()

scheduled_time = datetime.datetime(now.year, now.month, now.day, 9, 26)

delay_seconds = (scheduled_time - now).seconds

kit.sendwhatmsg (
    number,
    'Hello How Are U!',
    now.hour,
    now.minute + 1,
    wait_time=delay_seconds)
