# Import necessary modules
import pywhatkit as kit
import datetime

# Replace with the recipient's phone number
number = "**************"

# Get the current date and time
now = datetime.datetime.now()

# Set the scheduled time for the message (8:21 AM in this case)
scheduled_time = datetime.datetime(now.year, now.month, now.day, 9, 1)

# Calculate the delay in seconds until the scheduled time
delay_seconds = (scheduled_time - now).seconds

# Use pywhatkit to send a WhatsApp message with a delay
# Message content: 'Hello How Are U!'
kit.sendwhatmsg(number, 'Hello How Are U!', now.hour, now.minute + 1, wait_time=delay_seconds)
