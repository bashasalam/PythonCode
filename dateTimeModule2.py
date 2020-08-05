import datetime
import pytz
print("Assalaamu alaikkum to all")

### String formatting with date
#for tz in pytz.all_timezones:

 #  print(tz)
    #Indian/Chagos
#Indian/Christmas
datetime_today = datetime.datetime.now(tz=pytz.UTC)
print(datetime_today)
print(datetime.datetime.now())
print(datetime.datetime.now(tz=pytz.UTC))
datetime_indian = datetime_today.astimezone(pytz.timezone('Indian/Chagos'))
print(datetime_indian)

# String formating with dates
#2020-08-05-> August 05 ,2020SS
##strftime
print(datetime_indian.strftime('%B %d, %Y'))

### August 02, 2020  from this how to get date time object
##strptime method  ### p for parsing

datetime_thing = datetime.datetime.strptime('August 05, 2020', '%B %d, %Y')

print(datetime_thing)  ## now it is object we can add or substract date by using tdelta
print(repr(datetime_thing))

### MAYA PACKAGE INSTALLED I HAVE TO USE IT SOMEWHERE
