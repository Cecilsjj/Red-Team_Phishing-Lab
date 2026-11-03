
import smtplib
from email.message import EmailMessage

msg = EmailMessage()

msg["From"] = "Northstar IT Support <security@northstar-support.example>"
msg["To"] = "employee@northstar.example"
msg["Subject"] = "Action Required: Account Verification"

msg.set_content("""
Hello,

A security review has flagged your Northstar account
for verification.

Review your account notification:
http://127.0.0.1:8080/index.html

Northstar IT Support

Authorized cybersecurity training simulation.
""")

with smtplib.SMTP("127.0.0.1", 1025) as smtp:
    smtp.send_message(msg)

print("Simulated phishing email submitted to local Mailpit.")
