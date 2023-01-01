import os

SMTP_SERVER = "smtp.gmail.com:587"
SENDER_EMAIL = "hamzaplojovic9@gmail.com"
SENDER_PASSWORD = os.environ["SMTP_PASSWORD"]
RECIPIENTS = [
    "hamzaplojovic9@gmail.com",
    "semsudinplojovic@gmail.com",
]
MAIL_SUBJECT = "Sertifikati za stampu"