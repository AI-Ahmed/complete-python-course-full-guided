__author__ = "crypto"

# from __future__ import print_function # python 2.0
# DocString """ documentation... """


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
            duration (Optional [int]): The duration of the song in seconds.
                            default to zero if not specified
        """
        self.title = title
        self.artist = artist
        self.duration = duration


# we can use help() function to help us for running the class documentation
# help(Song)
# print('=' * 40)
# help(Song.__init__)
# print('=' * 40)
# help(Song.__doc__)
# print('=' * 40)
# help(Song.__init__.__doc__)
# you can add documentation to method using...
# Song.__init__.__doc__ = """hello"""  # not often used
# ---------------------------------------------------------------------------------------
# let's create a Class Album


class Album:
    """Class to represent an Album Docstring, using it's track list

    Attributes:
        name (str): The name of the album.
        year (int): The year was album was released.
        artist: (Artist): The artist that responsible for the album. If not specified,
                          the artist will default to an artist with the name "Various Artists".
        tracks (List[Song]): A list of the songs on the album.

    Methods:
        add_song: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list

        Args:
            song (song): A song to add.
            position (optional [int]): If specified, the song will be added to that position
                                       in the track list - inserting it between other song if necessary.
                                       otherwise, the song will be added to the end of the song

        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)
# ---------------------------------------------------------------------------------------
# Class Artist


class Artist:
    """Basic class to store artist details

    Attributes:
          name (str): the name of the artist.
          albums (List[Album]): A list of the albums by this artist.
                            the list includes only those albums in this collection,
                            it is not an exhaustive list of the artist's published albums.

    Methods:
            add_album: Use to add a new album to the artist's albums list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album (Album): Album object to add to the list.
                If the album is already present, it will not added again (although this is yet to implemented).
        """

        self.albums.append(album)
# ---------------------------------------------------------------------------------------
# The approach is that the objects aren't stored in their collections until
# a new record is read from the file
#
# Example:
#        The current album is only added to the artist album list when a record containing a different album is read
#        what that means is the last set of data won't be stored and that's why i've added this code from line 140
#        to check if there's a valid artist object on that last line adds that to the global list of artist
#        and also adds the current album the last one read into the artist list of albums.
#
# For more understanding, try to implement these lines into the function:
# line 01: (Keisha,Animal,Sony,2010['\n'])---> strip('\n) --->(Keisha,Animal,Sony,2010)
# line 02: Massive Attack,Heligoland,EMI,2013


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

# we will make some changes here that includes
    # [validate if artist is already stored or not, so we can retrieve it directly from the artist_list] (7.11)

    # Flow_chartConditional.png
    with open("Albums.txt", 'r') as albums:
        for line in albums:
            # data row should consist of (artist, album, song, year)    #song as record label
            artist_field, album_field, song_field, year_field = tuple(line.strip('\n').split(','))
            year_field = int(year_field)
            # print(artist_field, album_field, song_field, year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, song_field, year_field))

            if new_artist is None:  # line line ensure that there's a valid & unique data has been inserted (artist)
                # initially adding new_artist (instance)
                new_artist = Artist(artist_field)   # create new object Keisha
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:   # implement after reaching line 02
                # We've just read details for a new artist
                # Store the current album in the currents artist's collection then create a new artist object (Flow Chart 1.0)
                # -------------------------
                # retrieve the artist object if there's one, otherwise create a new artist object and add it to the artist_list (FlowchartConditional)
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:      # return None means it can't find the entry means[it can't find artist field in artist_list]
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None                    # reset the album variable
                # Flow Chart 1.0
                # -------------------------
                # new_artist.add_album(new_album)     # Animal album to Artist class ---> albums[Animal]
                # artist_list.append(new_artist)      # Keisha artist append into global ----> artist_list[Keisha]
                # new_artist = Artist(artist_field)   # create a new object which Massive Attack
                # new_album = None                    # reset the album variable
            # ============================

            if new_album is None:   # line line ensure that there's a valid & unique data has been inserted (album)
                new_album = Album(album_field,  year_field, new_artist)     # ---> (Animal, 2010, Keisha) [01]
                new_artist.add_album(new_album)
            elif new_album.name != album_field:     # implement after reaching line 02
                # We've just read details for a new album
                # Store the current album in the currents artist's collection then create a new album object (Flow Chart 1.0)
                # -------------------------
                # retrieve the album object if there's one, otherwise create a new artist object and add it to the new_artist.albums[] (FlowchartConditional)
                new_album.find_object(album_field, new_artist.albums)
                if new_album is None:   # if you find this new album didn't exist in the name attribute for any entry in our list albums[]
                    new_album = Album(new_album, year_field, new_artist)
                    new_artist.add_album(new_album)
                # Flow Chart 1.0
                # -------------------------
                # new_artist.add_album(new_album)
                # new_album = Album(album_field,  year_field, new_artist)
            # ============================
            # create a new song object (new instance)
            new_song = Song(song_field, new_artist)     # create a new object of line 01 ---> Sony, Keisha
            new_album.add_song(new_song)                # add the object into the class method --> tracks[Sony]
        # ============================
        # Now, we don't need that code because the new flow chart can handle those last lines of code because with the code build-in
        # Flow Chart 1.0
        # # After reading the last line of the text file, we will have an artist and album that haven't been stored - process them now
        #     if new_artist is not None:
        #         if new_album is not None:
        #             new_artist.add_album(new_album)
        #         artist_list.append(new_artist)

    return artist_list

# ================================================================================
# we need to check if the artist is correctly calculated!!  (07.9)


def create_checkfile(artist_list):
    """Create a check file from the object data for comparison with the original file"""
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{2.title}\t{1.year}".format(new_artist, new_album, new_song),
                          file=checkfile)

# =================================================================================
# what we need to do is to validate the artist name not to be duplicates. (Session 121 [07.11] Implement Revised Algorithm)


def find_object(field, object_list):
    """Check 'object_list' to see if an object with a 'name' attribute equal to 'field' exist, return if so"""

    for item in object_list:
        if item.name == field:
            return item
    return None     # if it wasn't able to return anything


if __name__ == '__main__':
    # we will try to evaluate the artist numbers
    artists = load_data()
    print("="*40+'\n')
    print("There are {} artists".format(len(artists)))

    create_checkfile(artists)   # we will create a new file with the new Flow chart

    # Comparison
    # Flow Chart 1.0: 399 artist
    # Flow Chart 3.0: 197 artist <--- after the validation

    # for comparison: Select two files then -->  View --> compare with or Ctrl + D


# Mini- Challenges
# what's the difference between the last two coded that we've written and the others projects that we've done into this course?
# Answer:
#       Actually there's no difference between them. although we've used classes here. But there's no different methodology between them
#       yes, this project uses object but it's not OOP
#
"""Object-oriented program is not just object-orientated programming
  it's not only about classes. it's a different way of OOP is not just classes
  it's thinking about the problems and results in about classes in a different way 
  to a different program design so it uses thinking about problems and results
  so, use classes and objects for sure but it also different program design so it uses
  encapsulation composition inheritance and delegation.  
  """