from datetime import date, time, datetime

today = date.today()
now = datetime.now()

print("Today's date is: ", today)
print("The current time is: ", now)

print("\nDate coomponents are: ", today.year, today.month, today.day)