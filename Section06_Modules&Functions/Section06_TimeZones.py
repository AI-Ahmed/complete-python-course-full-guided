__author__ = "crypto"

import time

print("the epoch on this system at " + time.strftime('%c', time.gmtime(0)))
# %c of .strftime() --> Locale's appropriate date and time representation

print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("\tDaylight Saving Time is in effect for this location")
    print("\tThe DST timezone is " + time.tzname[1])    # EET or EEST

print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print("UTC time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))

# ----------------------------------------------------------------------------------
print('='*40)
# There's another thing called 'DateTime'

import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
# ----------------------------------------------------------------------------------
print('='*40)
print("using Timezones")
# using Timezones   "This's not accurate because it depends on the device process date/time

import pytz

country = 'Africa/Cairo'

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))
# --------------------------------------
print('='*40)

for x in pytz.all_timezones:
    print(x)
# --------------------------------------
print('='*40)
# we can sort them depending on the IOS316 code of the country
# For Signal time Zone
for x in sorted(pytz.country_names):
    print(x + ": " + pytz.country_names[x])
# --------------------------------------
print('='*40)

# this one if the same country has two different timezones
# for x in sorted(pytz.country_names):
    # print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones[x]))
# if you notice there's an error related to ireland timezone that it don't have one, so, the problem not related to pytz
# Time Zone Database came from 'iana' which internet Assigned Number Authority
# --------------------------------------
print('='*40)
# to run the code defensively, we can use get
for x in sorted(pytz.country_names):
    print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones.get(x)))
# this time we will not get error because we called function that obtain the timezone from the database
# --------------------------------------
print('='*40)

# if you want to make it more complex you can assign the country in a loop

for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]), end=': ')
    if x in pytz.country_timezones:
        print(pytz.country_timezones[x])
    else:
        print("No Time Zone Defined!")

print('='*100)
# another way by using sorted method

for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]), end=': ')
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\tNo Time Zone Defined!")
# ----------------------------------------------------------------------------------
print('='*40)
print("Naive Time")

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive Local time {}, Time zone {}".format(local_time, local_time.tzinfo))
print("Naive UTC {}".format(utc_time, utc_time.tzinfo))

print()
print("Aware Time")

# to to use the localize the better way to do that is to use UTC and then convert it into local  time
# aware_local_time = pytz.utc.localize(local_time)
aware_local_time = pytz.utc.localize(utc_time).astimezone()  # astimezone() is using to convert to the timezone you want

aware_utc_time = pytz.utc.localize(utc_time)

print("Aware  Local time {}, time zone {}".format(aware_local_time, aware_local_time.tzinfo))
print("Aware UTC {}, Time zone {}".format(aware_utc_time, aware_utc_time.tzinfo))
# ----------------------------------------------------------------------------------
print('='*40)

gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())     # this function effected by two major objects [timezone, location]

# lets create a test included the value of the timezone of UK and see if it will be effected by our timezone

s = 1445733000   # the correct time zone in the UK
t = s + (60 * 60)   # T is one hour greater than the time zone of UK
# by calculating this equation we try to reach the gap_time
gb = pytz.timezone('GB')
# dt1 = pytz.utc.localize((datetime.datetime.fromtimestamp(s))).astimezone(gb)
# dt2 = pytz.utc.localize((datetime.datetime.fromtimestamp(t))).astimezone(gb)
#
# print("{} seconds since the epoch is {}".format(s, dt1))
# print("{} seconds since the epoch is {}".format(t, dt2))

# if you notice the result is totally wrong because our timezone is totally different from GB
# so, it depends on the time zone of the runner

# so, lets try to fix the problem
# need to change the lines from 121 to 122
# so, instead of using the local timestamp we need to use the UTC time stamp then convert it into our local

dt1 = pytz.utc.localize((datetime.datetime.utcfromtimestamp(s))).astimezone(gb)
dt2 = pytz.utc.localize((datetime.datetime.utcfromtimestamp(t))).astimezone(gb)

print("{} seconds since the epoch is {}".format(s, dt1))
print("{} seconds since the epoch is {}".format(t, dt2))
