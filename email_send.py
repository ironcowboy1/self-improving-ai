#!/usr/bin/env python3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from smtp_config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, FROM_ADDR, TO_ADDR

def send_email(subject, body, to_addr=None):
    to_addr = to_addr or TO_ADDR
    msg = MIMEMultipart()
    msg["From"] = FROM_ADDR
    msg["To"] = to_addr
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    try:
        if SMTP_PORT == 465:
            server = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT)
        else:
            server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
            server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(FROM_ADDR, to_addr, msg.as_string())
        server.quit()
        print(f"Email sent to {to_addr}")
        return True
    except Exception as e:
        print(f"Email failed: {e}")
        return False

if __name__ == "__main__":
    subject = sys.argv[1] if len(sys.argv) > 1 else "Self-improving AI test"
    body = sys.argv[2] if len(sys.argv) > 2 else "Test email from free-server bootstrap."
    send_email(subject, body)
