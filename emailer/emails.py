
import smtplib

# sample python emailer using gmail server 
def send_emails(emails, schedule, forecast):
    # Connect to the smtp server
    # Allow less secure apps: ON
    server = smtplib.SMTP('smtp.gmail.com', '587')

    # Start TLS encryption
    server.starttls()

    # Login
    from_email = input("What's your Gmail email address? ")
    password = input("What's your Gmail email password? ")

    # As mentioned above, Allow less secure apps otherwise
    # login would fail.
    server.login(from_email, password)

    """ Send to entire email list sample message:
    subject:	Welcome to the Circus!
    Hi Ferd DeRamos!

    The Circus forecast for today is clear sky with a high of 89.6 and a low of 84.2

    Circus event 01 - 9:00am
    Circus event 02 - 12:00pm
    Circus event 03 - 3:00pm
    Circus event 04 - 6:00pm
    Circus event 05 - 9:00pm


    Hope to see you there!
    """    
    for to_email, name in emails.items():
        message = "Subject: Welcome to the Circus!\n"
        message += "Hi " + name + "!\n\n"
        message += forecast + "\n\n"
        message += schedule + "\n\n"
        message += "Hope to see you there!"
        server.sendmail(from_email, to_email, message)

    server.quit()
