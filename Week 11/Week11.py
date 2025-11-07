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
        self.shows = [TVShow]

    def add_show(self, show):
        self.shows.append(show)

    def display_recommendations(self):
        print(f"Recommendations for {self.profile_name}:")
        for show in self.shows:
            print(show)

    def __str__(self):
        return f"NetflixDashboard for {self.profile_name} with {len(self.shows)} shows"


# Part (c)
dashboard = NetflixDashboard("UserProfile")
show1 = TVShow("The Crown", "Drama")
show2 = TVShow("Black Mirror", "Sci-Fi")
dashboard.add_show(show1)
dashboard.add_show(show2)
dashboard.display_recommendations()