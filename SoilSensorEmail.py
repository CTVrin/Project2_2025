import RPi.GPIO as GPIO
import time
import smtplib
from email.message import EmailMessage

#Name: Zhang you
#Date: 2025/4/16


def callback(channel):
    if GPIO.input(channel):
        print("Water Detected!")
    else:
        send_email()




def send_email():
    
    # Set the sender email and password and recipient email
    from_email_addr = "2547421656@qq.com"
    from_email_pass = "rqulxeokmgdlecdi"
    to_email_addr = "2018009351@qq.com"

    # Create a message object
    msg = EmailMessage()

    # Set the email body
    body = "Please water your plant"
    msg.set_content(body)

    # Set sender and recipient
    msg['From'] = from_email_addr
    msg['To'] = to_email_addr

    # Set your email subject
    msg['Subject'] = 'Water'

    # Connecting to server and sending email
    # Edit the following line with your provider's SMTP server details
    server = smtplib.SMTP_SSL('smtp.qq.com', 465)

    # Comment out the next line if your email provider doesn't use TLS
    # server.starttls()

    # Login to the smtp server
    server.login(from_email_addr, from_email_pass)

    # Send the message
    server.send_message(msg)
    print('Email sent')

    # Disconnect from the Server
    server.quit()


if __name__ == '__main__':
    
    # GPIO SETUP
    channel = 4
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.IN)

    callback(channel)

    GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # detect the pin goes high or low
    GPIO.add_event_callback(channel, callback)  # set call back function

    while True:
        time.sleep(1)
