
import os
import ssl
import smtplib
from email.message import EmailMessage

# Load credentials securely
email_sender = "sumbulsaleem907@gmail.com"
email_password = "igug hyjx dfow apgl"
email_receiver = "shamim.ahmedkk07@gmail.com"  

subject = "Check out my new video"
body = """Hello,

I've just uploaded a new video! You can find it on my official website.

Best regards,
Your Sumbul
"""

msg = EmailMessage()
msg["From"] = email_sender
msg["To"] = email_receiver
msg["Subject"] = subject
msg.set_content(body)

context = ssl.create_default_context()

# Connect securely to Gmail's SMTP server
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_receiver, msg.as_string())

print("Email sent successfully!")
