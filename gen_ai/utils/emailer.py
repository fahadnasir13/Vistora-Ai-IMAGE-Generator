import smtplib
from email.message import EmailMessage
import json
import os

CONFIG_PATH = os.path.join("data", "email_config.json")

def send_email(to_email, subject, content):
    try:
        with open(CONFIG_PATH, "r") as f:
            config = json.load(f)

        from_email = config["from_email"]
        password = config["password"]

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = from_email
        msg["To"] = to_email
        msg.set_content(content)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(from_email, password)
            smtp.send_message(msg)

        print(f"✅ Email sent to {to_email}")

    except Exception as e:
        print(f"❌ Failed to send email: {e}")
