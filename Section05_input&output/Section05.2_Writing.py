__author__ = "Crypto"

# ---------------------------------------------------------------------------

# Writing process
#   1 - Data is written to the buffer
#
#   2 - The contents of the buffer is transferred to the external device in the background.
#
#   3 - it happens automatically to allow the program to continue without waiting that write process to complete
#
#   4 - So, sometimes, when you write a large file with mgb size it may takes sometimes till end the process
#       even if the debugging and the running process end .
#
#   5 - sometimes you want the data to be written out immediately.
#       and you want the user to be able to see the output straight away
#       so, with buffering, data could be sent to the screen from the buffer for
#       example, and then immediately overwritten by subsequent data from the buffer.
#       displaying the last on the screen could suffer from that effect
#       now closing a file causes the buffer to be "flushed" automatically
#       but if you wanna ensure your data's written sooner, you can pass
#       'flush=True' to cause the data to be written immediately

# ---------------------------------------------------------------------------

# Example for writing

# cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]
#
# with open("write.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file, flush=True)     # city_file is the parameter for the file argument
#                                                      even the 'flush=True' not recommended

# let's read the file
with open("write.txt", 'r') as city_file:
    line = city_file.readline()
    while line:
        print(line, end='')
        line = city_file.readline()

print('=' * 40)

# Another way to Read the file and append into a list
# in another word, you're reading from file then appending into list
_cities = []
with open("write.txt", 'r') as city_file:
    for city in city_file:
        _cities.append(city.strip('\n'))  # strip() very useful for removes the double spacing between lines
print(_cities)
for city in _cities:
    print(city)  # using end instead of strip() will be a bad idea with using append()
# --------------------------------------------------------------------------------
print('=' * 40)
# To know how strip() working...
print("How strip() works!")
print("Adelaide".strip("A"))  # strip() is discard the char that you insert into it!
# --------------------------------------------------------------------------------
print('=' * 40)
# ---------------------------------------------------------------------------------
# Examples

imelda = "More Mayhem", "Imelda May", "2011", (
    (1, "pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

# You can write and read at the same time

# Writing

# with open("imelda_writing_file.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)

# Reading
with open("imelda_writing_file.txt", 'r') as imelda_file:
    contents = imelda_file.readline()

# imelda = eval(contents)     # eval() is not a good idea when  you dealing with content of file could be changed
#                             beside eval() is a security hole that has a lack of security.
#                             they're using it to convert the string into sort of any format depending on the content
# instead you can use int(), str(), etc..
print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)
# --------------------------------------------------------------------------
# for Open a disk file for updating (reading and writing)
# you can use '+'
# Example : with open ("fileName.txt", '+') as updateing_file
