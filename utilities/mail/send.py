# TODO: make a scanner that gets the path of the every file in the pdf directory and sends it as an attachment

import smtplib, os
from constants import *
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders as Encoders
from email.mime.multipart import MIMEMultipart


def get_all_pdf_files():
    pdf_files = []
    for root, _, files in os.walk(os.path.abspath("results/pdf")):
        for file in files:
            if file.endswith(".pdf"):
                pdf_files.append(os.path.join(root, file))
    return pdf_files
    

def send_mail(username, password, toaddrs_list, attachment_path_list):
    s = smtplib.SMTP(SMTP_SERVER)
    s.starttls()
    s.login(username, password)
    msg = MIMEMultipart()
    msg['Subject'] = MAIL_SUBJECT
    msg['To'] = ", ".join(toaddrs_list)
    if attachment_path_list is not None:
        for each_file_path in attachment_path_list:
            try:
                file_name=each_file_path.split("/")[-1]
                part = MIMEBase('application', "octet-stream")
                part.set_payload(open(each_file_path, "rb").read())
                Encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment' ,filename=file_name)
                msg.attach(part)
            except:
                print("could not attache file")
    msg.attach(MIMEText("Sertifikati za stampu",'html'))
    s.sendmail(SENDER_EMAIL, toaddrs_list, msg.as_string())

if __name__ == "__main__":
    send_mail(
        SENDER_EMAIL,
        SENDER_PASSWORD,
        RECIPIENTS,
        get_all_pdf_files()
    )