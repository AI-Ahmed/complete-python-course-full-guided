__author__ = "crypto"

# DocString """ documents... """


class Song:
    """Class to represent a song

    Attributes:
         title (str): Title of the song
         artist (artist): An artist object representing the song's creator.
         duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):  # we defaulting the value here if any variable has a default value like duration
        """Song init method

        Args:
            title (str): Initialises the 'title' attribute
            artist (artist): An artist object representing the song's creator.
            duration (int): The duration of the song in seconds.
                            default to zero if not specified
        """
        self.title = title
        self.artist = artist
        self.duration = duration


# Examples about raw_string and normal string and others ...

a_string = "this is\na string spilt\t\tand tabbed"
print(a_string)

raw_string = r"this is\na string spilt\t\tand tabbed"
print(raw_string)   # row string are useful when you don't want Python to treat the backslash escaped character in special way
#                     when the string literal is defined without the r prefix as you saw these \n causes a lots of line break

b_string = "this is" + chr(10) + "a string spilt" + chr(9) + chr(9) + "and tabbed"
print(b_string)

backslash_string = "this is a backslash \followed by some text"     # if you notice \f treated like a control not a string
print(backslash_string)

backslash_string = "this is a backslash \\followed by some text"     # use double \\ to turn it into string
print(backslash_string)

# when it turns to be an error
# error_string = r"this string ends with \"
error_string = r"this string ends with \\"  # we needed to add double backslash not to face a problem 