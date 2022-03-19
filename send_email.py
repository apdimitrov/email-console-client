import smtplib
import ssl
import getpass
from email.message import EmailMessage

sender_mail = input("Please, enter your email: ")
password = getpass.getpass("Please, enter a password: ")
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_mail, password)

    print("Welcome! You have logged in successfully!")

    receiver_mail = input("To: ")
    subject = input("Subject: ")
    body = input("Body: ")

    message = EmailMessage()
    message["From"] = sender_mail
    message["To"] = sender_mail
    message["Subject"] = subject

    html = f"""
    <html>
        <body>
            <h1 style="font-family: 'Raleway',sans-serif; font-size: 62px; font-weight: 800; line-height: 72px; margin: 0 0 24px; text-align: center; text-transform: uppercase;">{subject}</h2>
            <p style ="font-family: 'Raleway',sans-serif; font-size: 18px; font-weight: 500; line-height: 32px; margin: 0 0 24px; ">{body}</p>
        </body>
    </html>
    """

    message.add_alternative(html, subtype = "html")

    print("Sending Email..")

    server.sendmail(sender_mail, receiver_mail, message.as_string())

print("Success!")
