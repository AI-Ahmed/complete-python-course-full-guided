# The Challenge

# Given the tuple below that represents the Imelda May album "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more that one item to print function, separating them with a comma).

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "psycho"), (3, "Mayhem"), (4, "Kennith Town Waltz"))

# A) Unpacking

album, artist,  year, tracks = imelda
print(album)
print(artist)
print(year)
# list of track
#   style 1 [tuples]

track1, track2, track3, track4 = tracks
print(track1)
print(track2)
print(track3)
print(track4)

#   style 2 [List]
for track in tracks:
    print(list(track))

