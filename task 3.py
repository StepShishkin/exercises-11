class Track:
    """
    A class for representing a track.

        Attributes:
            name_track (str): The name of the track.
            time (str, optional): The duration of the track (can be None).
            name_singer (star, optional): The name of the artist (may be None).
            year (int, optional): The year of the album's release (maybe None).
            playing (bool): A flag indicating whether the track is currently playing.

        Methods:
            pause(): Pauses the track if it is playing, or informs you that the track is already on pause.
            play(): Turns on the track if it is not playing.
    """
    def __init__(self, name_track, time=None, name_singer=None, year=None):
        self.name_track = name_track
        self.time = time
        self.name_singer = name_singer
        self.year = year
        self.playing = False

    def pause(self):
        """
        Pauses the track if it is playing, or informs you that the track is already on pause.
        """
        if self.play:
            print(self.name_track, 'Поставлен на паузу')
            self.playing = False
        else:
            print(self.name_track, 'Уже на паузе')

    def play(self):
        """
        Turns on the track if it is not playing.
        """
        if not self.playing:
            print(self.name_track, 'Включен')


class Album:
    """
    Class for album presentation.

        Attributes:
            name_album (str): The name of the album.
            name_singer (str): The name of the artist.
            year (int): The year of the album's release.
            tracks (list): The list of tracks in the album.
            playing (bool): A flag indicating whether the album is currently playing.

        Methods:
            add_track_album(name_track): Adds a track to the album.
            remove_track_album(name_track): Removes a track from the album.
            play_album(): Plays the first track of the album.
            next_track_album(): Plays the next track of the album.
            pause_track(): Pauses the current track.
            play_track(): Plays the current track.
    """
    number_track = 0

    def __init__(self, name_album, name_singer, year):
        self.name_album = name_album
        self.name_singer = name_singer
        self.year = year
        self.tracks = []
        self.playing = False

    def add_track_album(self, name_track):
        """
        Adds a track to the album.
        """
        self.tracks.append(name_track)

    def remove_track_album(self, name_track):
        """
        Deletes a track from the album.
        """
        self.tracks.remove(name_track)

    def play_album(self):
        """
        Plays the first track of the album.
        """
        track = Track(self.tracks[0])
        track.play()

    def next_track_album(self):
        """
        Plays the next track of the album.
        """
        Album.number_track += 1
        track = Track(self.tracks[Album.number_track])
        track.play()

    def pause_track(self):
        """
        Pauses the current track.
        """
        track = Track(self.tracks[Album.number_track])
        track.pause()

    def play_track(self):
        """
        Plays the current track
        """
        track = Track(self.tracks[Album.number_track])
        track.play()




album = Album('рок', 'певец', 2001)
album.add_track_album('fghjkl')
album.add_track_album('vbnm')
album.add_track_album('tyuiop')
album.play_album()
album.next_track_album()
album.pause_track()




"""track1 = Track('ghjk', '3:20', 'fghjkl', 2001)
track2 = Track('ghfhholdsjfl', '3:20', 'fghjkl', 2001)
track3= Track('ghjsmdbfksnlk', '3:20', 'fghjkl', 2001)
track4 = Track('ghfjasljk', '3:20', 'fghjkl', 2001)
"""