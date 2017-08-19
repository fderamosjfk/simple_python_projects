
import smtplib

def send_emails(emails, schedule, forecast):
    # Connect to the smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')

    # Start TLS encryption
    server.starttls()

    # Login
    from_email = input("What's your Gmail email address? ")
    password = input("What's your Gmail email password? ")
    server.login(from_email, password)

    # Send to entire email list
    for to_email, name in emails.items():
        message = "Subject: Welcome to the Circus!\n"
        message += "Hi " + name + "!\n\n"
        message += forecast + "\n\n"
        message += schedule + "\n\n"
        message += "Hope to see you there!"
        server.sendmail(from_email, to_email, message)

    server.quit()
