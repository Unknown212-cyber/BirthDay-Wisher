import pandas
import datetime as dt
import smtplib
import random
# Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)


today = dt.datetime.now()
today_tuple = (today.month, today.day)

my_email = "malharpatel2u@gmail.com"
password = "Anandi21"

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as data_file:
        contents = data_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp-mail.outlook.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday {birthday_person['name']}!\n\n{contents}"
        )
