class TVshow:
    def __init__(self, title = "Unknown", genre = "Unknown"):
        self.title = title
        self.genre = genre

    def get_genre(self):
        return self.genre
    
    def get_title(self):
        return self.title
    
    def set_genre(self, _genre):
        self.genre = _genre
    
    def set_title(self, _title):
        self.title = _title
    
    def __str__(self):
        return f"The tv show is : {self.get_title()} and the genre is : {self.get_genre()}"


class NetflixDashboard:
    def __init__(self, profile_name= "unknown"):
        self.TVshows = []
        self.profile_name = profile_name
    
    def add_show(self, show):
        self.TVshows.append(show)

    def display_recommendations(self):
        for show in self.TVshows:
            print(show)
            

tvshow1 = TVshow("Two and a half men", "sitcom")
tvshow2 = TVshow("Friends", "sitcom")

profile1 = NetflixDashboard("Evan")
profile1.add_show(tvshow1)
profile1.add_show(tvshow2)

profile1.display_recommendations()