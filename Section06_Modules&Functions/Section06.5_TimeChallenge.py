__author__ = "crypto"

# Write a small program to
# display information on the four clocks whose functions we have just looked at:
# i.e. time(), Perf_counter, monotonic() and process_time().
#
# Use this documentation for the get_clock_info() function
# to work our how to cal it for each of the clocks.
import time
print("clock No. 1: [Time:\t\t\t", time.get_clock_info('time'))    # time.time()
print("clock No. 2: [monotonic:\t", time.get_clock_info('monotonic'))    # time.monotonic()
print("clock No. 3: [perf_counter:\t", time.get_clock_info('perf_counter'))    # time.perf_counter()
print("clock No. 4: [process_time:\t", time.get_clock_info('process_time'))    # time.process_time()
