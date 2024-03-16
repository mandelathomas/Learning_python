
#using date and time. First thing, we have to import the datetime module and assigned dt to it and use the "dt" to perform any function.
import datetime as dt

#using both time and date

record = dt.datetime.now()
print(record)

#accessing just the date
record = dt.date.today()
print(record)

#accessing just the time
record = dt.time()
print(record)

#using date individually

record = dt.datetime.now()
print("Year : ", record.year)
print("Day : ", record.day)
print("Month : ", record.month)
print("Year : ", record.minute)

#The strftime() Method
"""
The strftime() Method is used to convert string into a datetime object.

# %Y - Year, full version - (9999)
# %y -year short version (24)
# %b - Month name, short version - (Jan- Dec)
# %B - Month name, full version - (January- December)
# %m - Month in a number - (01- 12)
# %d - Day of month - (01-31)
# %H - Hour - (00, 01, ..., 23)
# %M - Minute - (00, 01, ..., 59)
# %S - Second - (00, 01, ..., 59)

"""

record = dt.datetime.now()
print("date: ", record.strftime("%d/%m/%Y"))
print("date: ", record.strftime("%d/%B/%Y"))
print("date: ", record.strftime("%d,%B,%Y"))

#project with date and time
print("ATSMAS Work clocking Station \n Please clock in and out with your EID")

name = "Mandela Philip Thomas"
lname = name.split()[2]

#clock in system
clock_in = input("Enter Your EID: ")
if len(clock_in) == 6:
  print(f"Thank you {lname }, you clock in at", record.strftime("%B/%d/%Y  %H:%M:%S."), "\n Have a good working day")
elif len(clock_in) > 6:
  print("Your EID must be 6 digits!")
elif len(clock_in) <6:
  print("Your EID must be 6 digits!")
else:
  print("System lock your acocunt. Please call your supervisor!")

#clok out system
clock_out = input("Enter Your EID: ")
if len(clock_out) == 6:
  print(f"Thank you {lname }, you clock out at", record.strftime("%B/%d/%Y  %H:%M:%S."), "\n Have a nice day!!")
elif len(clock_out) > 6:
  print("Your EID must be 6 digits!")
elif len(clock_out) <6:
  print("Your EID must be 6 digits!")
