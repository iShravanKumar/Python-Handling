import os
import smtplib
from email.message import EmailMessage
from log_generator import logging

EMAIL_ADDR = os.environ.get('EMAIL_USER_TEMP')
EMAIL_PASS = os.environ.get('EMAIL_USER_P_TEMP')


def send_build_email(to_address, subject, body):
    try:
        message = EmailMessage()
        message['Subject'] = subject
        message['From'] = EMAIL_ADDR
        message['To'] = to_address
        message.set_content(body)
        return message
    except Exception as error:
        logging.error(f'Unknown error during Build Email Operation, {error}')


def attach_email(file_list, message):
    try:
        for file in file_list:
            with open(file, 'rb') as f:
                file_data = f.read()
                file_name = f.name
            message.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    except Exception as error:
        logging.error(f'Unknown error during Attach Email Operation, {error}')


def send_email(message):
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDR, EMAIL_PASS)
            smtp.send_message(message)
    except Exception as error:
        logging.error(f'Unknown error during Send Email Operation, {error}')
