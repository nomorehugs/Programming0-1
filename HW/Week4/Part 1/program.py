from datetime import date

first_name = input("Your first name: ")
second_name = input("Your second name: ")
last_name = input("Your last name: ")
birth_date = input("Your birth year: ")
birth_date = int(birth_date)

dict = {"first_name": first_name, "second_name": second_name, "last_name": last_name, "birth_date": birth_date, "current_age": date.today().year-birth_date}
print(dict)
