import json
import time
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
    start_time = 0
    stop_time = 0
    count_time = 0
    count_time_1 = 0

    def __init__(self, name_track, time_track=None, name_singer=None, year=None):
        self.name_track = name_track
        self.time_track = time_track
        self.name_singer = name_singer
        self.year = year
        self.playing = False

    def pause(self):
        """
        Pauses the track if it is playing, or informs you that the track is already on pause.
        """
        if self.play:
            Track.stop_time = Track.count_time + time.time()
            self.playing = False
            print(self.name_track, f'Поставлен на паузу, текущее время '
                                   f'{time.strftime('%M:%S', time.gmtime(
                                       round(Track.count_time + Track.stop_time - Track.start_time)))}')
            Track.count_time = round(Track.count_time + Track.stop_time - Track.start_time)
        else:
            print(self.name_track, 'Уже на паузе')

    def play(self):
        """
        Turns on the track if it is not playing.
        """
        if not self.playing:
            self.playing = True
            Track.start_time = Track.count_time + time.time()
            print('Сейчас играет',self.name_track, time.strftime('%M:%S', time.gmtime(round(Track.count_time))))



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

    def __init__(self, name_album, name_singer=None, year=None):
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
        print(f'трек {name_track} удален')

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

    def pause_track(self, name_track):
        """
        Pauses the current track.
        """
        Album.number_track = self.tracks.index(name_track)
        track = Track(self.tracks[Album.number_track])
        track.pause()

    def play_track(self, name_track):
        """
        Plays the current track
        """
        Album.number_track = self.tracks.index(name_track)
        track = Track(self.tracks[Album.number_track])
        track.play()

with open('album.json', 'r') as file:
    data = json.load(file)

def choose_album():
    print(f'выберете альбом')
    for key in data:
        print(key)
    name_album = str(input())
    print(f'выбран альбом {name_album} \n')
    choose_track(name_album)

def command():
    print('Выбрете номер команды')
    print('1: Поставить на паузу')
    print('2: Возобновить трек')
    print('3: Выбрать альбом')
    print('4: Выбрать трек')
    print('5: Следующий трек')
    print('6: Удалить этот трек из альбома')
def choose_track(name_album):
    album = Album(name_album)
    print('Выберете номер трека')
    number = 0
    number_track = {}
    for i in range(len(data[name_album])):
        number += 1
        album.add_track_album(data[name_album][i][0])
        number_track[number] = data[name_album][i][0]
        print(f'{number} {data[name_album][i][0]} {data[name_album][i][1]}')
    int_number = int(input())
    name_track = number_track[int_number]
    album.play_track(number_track[int_number])
    command()
    while True:
        command_int = int(input())
        if command_int == 1:
            album.pause_track(name_track)
            command()
        if command_int == 2:
            album.play_track(name_track)
            command()
        if command_int == 3:
            choose_album()
            break
        if command_int == 4:
            choose_track(name_album)
        if command_int == 5:
            album.next_track_album()
            command()
        if command_int == 6:
            album.remove_track_album(name_track)
            command()

print(choose_album())