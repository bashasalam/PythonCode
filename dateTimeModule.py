print("Assalaamu alaikkum to all")

### date time date time objects

### distance between day and birthday

import datetime
import pytz
today = datetime.date.today()
print(today)
birthday = datetime.date(1987,4,24)
print(birthday)
days_since_birth = (today - birthday).days

## Actually no need of .days if u miss the .days the uotput will be 12156days
print(days_since_birth)
#### delta for differing or adding days
tdelta = datetime.timedelta(days=10)
print(today - tdelta)
print(today + tdelta)

this_month = today.month
print(this_month)
print(today.month)
print(today.day)
print(today.weekday()) # monday = 0 , # sunday = 6

#### To Deal with hours mins and seconds and microsec

print(datetime.time(18,57,45,15))

print(datetime.date(2020,8,4))  ### pass parameters (Y ,M ,D)
print(datetime.time(19,1,33,45))    #### (h,m,s,microsec
print(datetime.datetime(2020,8,4,19,2,36,256))  ###(Y ,M,D,H,M,S,millisec)

hour_delta = datetime.timedelta(hours=10)

###Current time
print(datetime.datetime.now())

####Add 10 hours from now
print(datetime.datetime.now() + hour_delta)

#### it doesn't understand time zone so i 've to import pytz

datetime_today=datetime.datetime.now(tz = pytz.UTC)
print(datetime_today)

#for tz in pytz.all_timezones: ## for all timezones
 #  print(tz)

print(datetime_today.astimezone(pytz.timezone('Indian/Antananarivo')))
print(datetime_today.astimezone(pytz.timezone('Indian/Chagos')))
print(datetime_today.astimezone(pytz.timezone('Indian/Christmas')))
print(datetime_today.astimezone(pytz.timezone('Indian/Cocos')))
print(datetime_today.astimezone(pytz.timezone('Indian/Comoro')))
print(datetime_today.astimezone(pytz.timezone('Indian/Kerguelen')))
print(datetime_today.astimezone(pytz.timezone('Indian/Mahe')))
print(datetime_today.astimezone(pytz.timezone('Indian/Maldives')))
print(datetime_today.astimezone(pytz.timezone('Indian/Mauritius')))
print(datetime_today.astimezone(pytz.timezone('Indian/Antananarivo')))
print(datetime_today.astimezone(pytz.timezone('Indian/Mayotte')))
print(datetime_today.astimezone(pytz.timezone('Indian/Reunion')))

print("Alhamdhulillah I found my time zone")


