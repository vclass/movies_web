import webbrowser


class Movie:
    """A movie class that stores its desription and details
    Attributes:
        title: A string contains movie title name
        storyline: A string decribes main story line of the movie
        release_date: A string indicate movie's release date
        rated: A string indicates movies rated e.g. G, PG, PG-13 etc.
        poster_image_url: A link to movie's poster image
        youtube_url: A link to movie's trailer
    """

    def __init__(self, title, genre, release_date, rated,
                 poster_image_url, youtube_url):
        """Inits Movie class with its attributes"""

        self.title = title
        self.genre = genre
        self.release_date = release_date
        self.rated = rated
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = youtube_url

    def show(self):
        """Show movies trailer in new webbrowser"""

        webbrowser.open(self.trailer_youtube_id)
