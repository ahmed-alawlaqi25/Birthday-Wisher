##################### Extra Hard Starting Project ######################
import pandas as pd
import random
import datetime as dt
import smtplib
# 1. Update the birthdays.csv

birth_data = pd.read_csv("birthdays.csv")
new_data = birth_data.to_dict()
name = new_data['name'][0]
email = new_data['email'][0]

# 2. Check if today matches a birthday in the birthdays.csv
year = new_data['year'][0]
month = new_data['month'][0]
day = new_data['day'][0]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
    new_name = (letter.readline().replace('[NAME]', name))
    next_line = letter.readlines()
    final_letter = new_name + "".join(next_line)

# 4. Send the letter generated in step 3 to that person's email address.
birth_day = dt.datetime(year,month,day)
current_time = dt.datetime.now()
current_date = current_time.date()
if (current_date.month == birth_day.month) and (current_date.day == birth_day.day):
    my_email = "xxw6gamer@gmail.com"
    password = "oewb ygow oqfi mipg "
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= my_email, password= password)
        connection.sendmail(
            from_addr= my_email,
            to_addrs="wijas18205@fentaoba.com",
            msg=f"Subject: Happy Birthday {new_name}\n\n {final_letter}",
        )


