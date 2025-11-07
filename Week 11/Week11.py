import math

class Song:
    def __init__(self, _title = "unknown", _artist = "unknown"):
        self.title = _title
        self.artist = _artist
    def get_artist(self):
        return self.artist
    def set_artist(self, val):
        self.artist = val
    def play(self):
        return f"{self.title} is playing !"
    def __str__(self):
        return f"{self.title} by {self.get_artist()}"
    
class Playlist:
    def __init__(self, _playlistName):
        self.playlistName = _playlistName
        self.songs = []

    def add_song(self, aSong ):
        self.songs.append(aSong)
    
    def play_all(self):
        message = ""
        for song in self.songs:
            message += song.play()
        return message
    def __str__(self):
        return f"Playlist Name = {self.playlistName} , No. Of Songs: {len(self.songs)}"


song1 = Song("Vampire Money")
song1.set_artist("Chemical Romance")

song2 = Song("Despacito", "One Direction")

cis121Jam = Playlist("cis121 Section 3")
cis121Jam.add_song(song1)
cis121Jam.add_song(song2)
print(cis121Jam)
print(cis121Jam.play_all())

#Question 12
class TVShow:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_genre(self, new_genre):
        self.genre = new_genre

    def preview(self):
        print(f"Title: {self.title}, Genre: {self.genre}")

    def __str__(self):
        return f"{self.title} ({self.genre})"


class NetflixDashboard:
    def __init__(self, profile_name):
        self.profile_name = profile_name
        self.shows = []

    def add_show(self, show : TVShow):
        self.shows.append(show)

    def display_recommendations(self):
        print(f"Recommendations for {self.profile_name}:")
        for show in self.shows:
            print(show)
   
    def __str__(self):
        return f"NetflixDashboard for {self.profile_name} with {len(self.shows)} shows"

dashboard = NetflixDashboard("UserProfile")
show1 = TVShow("The Crown", "Drama")
show2 = TVShow("Black Mirror", "Sci-Fi")
dashboard.add_show(show1)
dashboard.add_show(show2)
dashboard.display_recommendations()

class Point:
    def __init__(self,_x, _y):
        self.x = _x
        self.y = _y
    
    def __eq__(self, point2):
        return self.x == point2.x and self.y == point2.y


    def get_distance(self, other):
        return math.sqrt((self.x - other.x)**2+(self.y - other.y)**2)
    
point1 = Point(3,2)
point2 = Point(3,2)
point3 = Point(3,6)


print(point1 == point2 == point3)

