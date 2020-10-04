__author__ = "crypto"

# Challenge 07.14: Removes Circular
"""Modify the program so that the class structure matches the simplified diagram [Album Class Diagram_Enhancement]:
   Artist objects can hold references to Album objects can hold references to song objects
   but there must no circular references
"""


class Song:
    """Class to represent a song

    Attributes:
         title (str): Title of the song
         # artist (artist): An artist object representing the song's creator. --> Circular Reference
         artist (str): The name the song's creator.
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

    def get_title(self):
        return self.title

    name = property(get_title)
# ---------------------------------------------------------------------------------------
# let's create a Class Album


class Album:
    """Class to represent an Album Docstring, using it's track list

    Attributes:
        name (str): The name of the album.
        year (int): The year was album was released.
        # artist (Artist): The artist that responsible for the album. If not specified,
                          the artist will default to an artist with the name "Various Artists".

        artist (str): The artist that responsible for the album. If not specified,
                          the artist will default to an artist with the name "Various Artists".

        tracks (List[Song]): A list of the songs on the album.

    Methods:
        add_song: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            # self.artist = Artist("Various Artists") circular reference by passing the object
            self.artist = "Various Artists"
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list

        Args:
            song (song): The title of a song to add.
            position (optional [int]): If specified, the song will be added to that position
                                       in the track list - inserting it between other song if necessary.
                                       otherwise, the song will be added to the end of the song

        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)
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

    def add_song(self, name, title, year):
        """Add a new song to the collection of albums

        This method will add the song to an album in the collection
        A new album will be created in the collection if it doesn't already exist

        Args:
            name (str): The name of the album
            title (str): The title of the song
            year (int): 1the title of the song
        """
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + " not found")
            # album_found = Album(name, year, self) by changing that we will pass the value of the artist instead of the object reference
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print("Found album " + name)

        album_found.add_song(title)
# ---------------------------------------------------------------------------------------
# what we need to do is to validate the artist name not to be duplicates. (Session 121 [07.11] Implement Revised Algorithm)


def find_object(field, object_list):
    """Check 'object_list' to see if an object with a 'name' attribute equal to 'field' exist, return if so"""
    for item in object_list:
        if item.name == field:
            return item
    return None     # if it wasn't able to return anything


def load_data():

    artist_list = []

    with open("Albums.txt", 'r') as albums:
        for line in albums:
            # data row should consist of (artist, album, song, year)    #song as record label
            artist_field, album_field, song_field, year_field = tuple(line.strip('\n').split(','))
            year_field = int(year_field)
            # print(artist_field, album_field, song_field, year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, song_field, year_field))

            new_artist = find_object(artist_field, artist_list)
            print()
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, song_field, year_field)

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


if __name__ == '__main__':
    # we will try to evaluate the artist numbers
    artists = load_data()
    print("="*40+'\n')
    print("There are {} artists".format(len(artists)))

    create_checkfile(artists)
