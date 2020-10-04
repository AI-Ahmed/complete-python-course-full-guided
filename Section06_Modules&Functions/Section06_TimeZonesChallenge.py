__author__ = "crypto"

# Create a program that allows a user to choose of
# up to 9 times zones from a menu. you can choose any zones
# you want from the all_timezones list.
#
# The program will then display the time in that timezone,
# as well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time

import time
import datetime
import pytz

# print(pytz.all_timezones)

tz_list = [('Africa/Abidjan', 1), ('Africa/Accra', 1), ('Africa/Addis_Ababa', 1),
           ('Africa/Algiers', 1), ('Africa/Asmara', 1), ('Africa/Asmera', 1),
           ('Africa/Cairo', 1), ('Africa/Bangui', 1), ('Africa/Banjul', 1)]

while True:
    print("This's a menu of time zones:")
    for t in tz_list:
        print("\t\tTime Zone: {}".format(t[0]))
    timezone = input("Please enter timezone of the time you want | or press 0 to quit:  ")
    if timezone == '0':
        break

    local_time = datetime.datetime.now()
    utc_time = datetime.datetime.utcnow()

    aware_local_time = pytz.utc.localize(utc_time).astimezone()
    aware_utc_time = pytz.utc.localize(utc_time)

    print("Local Time: {}, Time zone: {}".format(aware_local_time, aware_local_time.tzinfo))
    print("UTC Time: {}, Time zone: {}".format(aware_utc_time, aware_utc_time.tzinfo))
    print("--" * 40)

# ------------------------------------------------------------------------------------------------------
# another solution

available_zones = {'1': "Africa/Tunis",
                   '2': "Asia/Kolkata",
                   '3': "Australian/Adelaide",
                   '4': "Europe/Brussels",
                   '5': "Europe/London",
                   '6': "Japan",
                   '7': "Pacific/Tahiti",
                   '8': "US/Havaii",
                   '9': "Africa/Tunis"}

print("Please Choose a time zone (or 0 to quit):")
for place in sorted(available_zones):
    print("\t{}. {}".format(place, available_zones[place]))

while True:
    choice = input()

    if choice == '0':
        break

    if choice in available_zones.keys():
        tz_to_display = pytz.timezone(available_zones[choice])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {} {}".format(available_zones[choice], world_time.strftime('%A %x %X %z'), world_time.tzname()))
        print("Local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))
        print()
