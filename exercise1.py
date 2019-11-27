import datetime


def current_year():
    now = datetime.datetime.now()
    return int(now.year)


def age_delta(user_age):
    delta = 100 - int(user_age)
    return delta


name = input("What is your name? ")
age = input("Age? ")
copy_message = input("How many copies of the result do you want? ")


print(int(copy_message) * (name + " will be 100 years old in " + str(current_year() + age_delta(age)) + "\n"))
