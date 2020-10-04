__author__ = "crypto"

import time

print(time.gmtime(0))
print(time.localtime())
print(time.time())  # No. of sec in 32 bit till Feb 2038 that must turn to 64 bit

# ---------------------------------------------------------
print('=' * 40)

# we can print them specifically

time_here = time.localtime()
print(time_here)

print("Year: ", time_here[0], time_here.tm_year)
print("Month: ", time_here[1], time_here.tm_mon)
print("Day: ", time_here[2], time_here.tm_mday)

# ---------------------------------------------------------
print('=' * 40)

# Example for time

from time import time as my_timer  # my timer is a module for time in my region
import random

input("Please enter to start: ")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("please enter to stop. . . ")

end_time = my_timer()

# Function strftime() <--- str is the time stands for string time of local time tuple into more readable form
# "%X" this's a sign for locale's appropriate time representation'
print("started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your Reaction time was {} seconds".format(end_time - start_time))

# you can search for more parameter for strftime() in python.org

# another issue that i can cheat by entering twice into the programme and
# the computer will accept it, so, the next section we will try to discover how to fix it!

# ---------------------------------------------------------
print('=' * 40)

import time
from time import perf_counter as my_timer
# This gives an accurate measure of
# the elapse time but the value returned doesn't represent an actual time
# so, we can calculate the difference between two times it returns when we try to convert to local time
import random


input("Please enter to start: ")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("please enter to stop. . . ")

end_time = my_timer()

print("started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your Reaction time was {} seconds".format(end_time - start_time))
# ---------------------------------------------------------
print('=' * 40)

# monotonic function
# it is a difficult to see any difference between monotonic and perf_counter
# may monotonic has a higher resolution in some sort of system
from time import monotonic as my_timer

import random


input("Please enter to start: ")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("please enter to stop. . . ")

end_time = my_timer()

print("started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your Reaction time was {} seconds".format(end_time - start_time))

# ---------------------------------------------------------
print('=' * 40)

# Fourth_function
# Process_time
# its not really appropriate for this little game
# it returns the time that the CPU spends executing the current
# Process rather the actual elapsed
# its only useful in like profiling code and in actual fact its using by python module
# its also being used if you need to know how much of time does the CPU takes in a task

from time import process_time as my_timer

import random


input("Please enter to start: ")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("please enter to stop. . . ")

end_time = my_timer()

print("started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your Reaction time was {} seconds".format(end_time - start_time))

# PEP 0418 -- Add monotonic time, Performance counter, and process time function
