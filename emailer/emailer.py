import emails
import weather

def get_emails():
    emails = {}

    try:
        email_file = open('emails2.txt', 'r')
        for line in email_file:
            (email, name) = line.strip().split(', ')
            emails[email] = name
    except FileNotFoundError as err:
        print(err)

    return emails 


def get_schedule():
    try:
        schedule_file = open('schedule.txt', 'r')
        schedule = schedule_file.read()
    except FileNotFoundError as err:
        print(err)

    return schedule


def main():
    emails_dict = get_emails()
    print(emails_dict)

    schedule = get_schedule()
    print(schedule)

    forecast = weather.get_weather_forecast()
    print(forecast)

    emails.send_emails(emails_dict, schedule, forecast)


if __name__ == "__main__":
    main()

