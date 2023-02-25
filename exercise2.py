import datetime as dt

print("Please input your \n Date of Born \n Month of Born \n Year of Born \n")

date = int(input("Date: \t:"))
month = int(input("Month: \t:"))
year = int(input("Year: \t:"))

date_of_born = dt.date(year,month,date)
print(f"you were born on {date_of_born}")
print(f"the day was {date_of_born: %A}")