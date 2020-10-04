__author__ = "Crypto"

# Let's Create a Tuple

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "psycho"), (3, "Mayhem"), (4, "Kennith Town Waltz"))
# This tuple is 'Master Tuple' with 'multi subset of tuples'
print(imelda)

title, artist, year, track = imelda
print(title)
print(artist)
print(year)
print(track)

# -----------------------------------------------
print("\n")
# Let's turn it down to one tuple

imelda = "More Mayhem", "Imelda May", 2011, (1, "Pulling the Rug"), (2, "psycho"), (3, "Mayhem"), (4, "Kennith Town Waltz")
# This tuple is 'Master Tuple' with 'multi subset of tuples'
print(imelda)

title, artist, year, track1, track2, track3, track4 = imelda
print(title)
print(artist)
print(year)
print(track1)
print(track2)
print(track3)
print(track4)
print("\n\n")
# -----------------------------------------------
# The Challenge

# Given the tuple below that represents the Imelda May album "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more that one item to print function, separating them with a comma).

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "psycho"), (3, "Mayhem"), (4, "Kennith Town Waltz"))

print(imelda)
# Master Tuple
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
# sub-Master tuple
track1, track2, track3, track4 = tracks  # <--- Like this one
print("\tTrack Number {}, Title: {}".format(track1[0], track1[1]))
print("\tTrack Number {}, Title: {}".format(track2[0], track2[1]))
print("\tTrack Number {}, Title: {}".format(track3[0], track3[1]))
print("\tTrack Number {}, Title: {}".format(track4[0], track4[1]))
print("\n")
# Another Solution <--- This solution is good because you don't have to initialize every tuple you have in your master
# you can only trace the main variable you have not initializing every tuple with a variable
for song in tracks:
    track, title = song
    print("\tTrack Number {}, Title: {}".format(track, title))

# ------------------------------------------------------------------------
print("\n")
print("=" * 50)
# Now, Lets Listing the tracks
imelda = "More Mayhem", "Imelda May", 2011, (
    [(1, "Pulling the Rug"), (2, "psycho"), (3, "Mayhem"), (4, "Kennith Town Waltz")]) # <--- if you notice that we listed it
# now, we can append some more tracks
print(imelda)

imelda[3].append((5, "All for you"))

title, artist, year, tracks = imelda
tracks.append((6, "Eternity"))
print(title)
print(artist)
print(year)

for song in tracks:
    track, title = song
    print("\tTrack Number {}, Title: {}".format(track, title))

# Now, like we start, Tuples is immutable that can't be changed. but if you appended a list like the previous
# exaple you can see that we can change the content or append to it!