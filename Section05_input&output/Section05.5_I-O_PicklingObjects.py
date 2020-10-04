__author__ = "Crypto"

# we will talk about something called "pickle"
# in java its related to something called "serialization"
# That's a process that allows objects to be saved to a file

import pickle

# create a tuple

imelda = ("More Mayhem",
          "Imelda May",
          "2011",
          ((1, "Pulling the Rug"),
           (2, "Psycho"),
           (3, "Mayhem"),
           (4, "Kentish Town Waltz")))

# lets try to write multiple objects in file using pickle

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

# Writing
with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)        # To append in that file, we can use pickle.dump()
    pickle.dump(even, pickle_file, protocol=0)  # protocol helps to sort the data vertically
    pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(2998302, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)

# Reading
with open("imelda.pickle", "rb") as imeldaPickle:
    imelda_reading = pickle.load(imeldaPickle)
    evenList = pickle.load(imeldaPickle)
    oddList = pickle.load(imeldaPickle)
    x = pickle.load(imeldaPickle)


print(imelda_reading)

album, artist, year, track_list = imelda_reading

print(album)
print(artist)
print(year)
for track in track_list:
    track_number, track_title = track
    print("Track No. {0}: {1}".format(track_number, track_title))

for e in evenList:
    print(e)
print('-' * 20)

for o in oddList:
    print(o)

print('-' * 20)

print(x)
# -------------------------------------------------------------------------------------------
print("=" * 40)

# So, what the msg here is that you should really only unpickling
# data that you can trust.
# Pickling is fun for storing your program's data but shouldn't be used when dealing
# with data of untrusted sources such as over the internet for argument's sake

# Pickle using the dumps and loads methods, so instead of writing to we're reading from a file
# what they do is send data to or get data from a bytes object, in another word
# a sequence of bytes so, we're gonna create a row bytes sequence that uses
# that pickle load to create an object that it represents, but exactly the same effect
# could be reduced by saving the bytes in a file and calling the pickle.load method
# Now our data was a representation of an os dot system object
# and because our stream pickle included the command to delete the file
# The simple act of loading a data file resulted in another file being deleted
# Just loading the file caused something else to be deleted
# and again, a very simple example but you can image some
# spywares could be create or could be caused by easy untrusted sources here.
# Pickle is great for storing and retrieving your own data
# there's also ways to prevent the security problems we've just seen
# So, it is possible to use pickle in production code
# but these methods is quite advanced

# ----------------------------------------------------------------------------------------------

# let's run a simple command for deleting pickle file

# pickle.loads(b"cos\nsystem\n(S'rm imelda.pickle'\ntR.")     # Mac/Linux
