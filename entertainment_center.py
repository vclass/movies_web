import media
import fresh_tomatoes
import urllib
import json


# Create list of movies to add in webpage

movies = [
    "your name",
    "avatar",
    "inception",
    "back to the future",
    "the martian",
    "hello stranger"
]

# Create dictionary of movies trailers

youtube_url = {
    "your name": "https://www.youtube.com/watch?v=xU47nhruN-Q",
    "avatar": "https://www.youtube.com/watch?v=5PSNL1qE6VY",
    "inception": "https://www.youtube.com/watch?v=YoHD9XEInc0",
    "back to the future": "https://www.youtube.com/watch?v=qvsgGtivCgs",
    "the martian": "https://www.youtube.com/watch?v=ej3ioOneTy8",
    "hello stranger": "https://www.youtube.com/watch?v=6AGtFT52ASY"
}

list_movies = []  # List to collect all movies details

# Loop through each movie
# Get details of movie from omdbapi that return details in json format
# Get Youtube trailer url from pre-define dictionary

for movie in movies:

    # Send request to omdbapi with movie title

    response = urllib.urlopen("http://www.omdbapi.com/?t=" + movie)

    # Get response and load json file into dictionary

    json_movie = json.loads(response.read())

    # define details of movie

    object_movie = media.Movie(
        json_movie["Title"],
        json_movie["Genre"],
        json_movie["Released"],
        json_movie["Rated"],
        json_movie["Poster"],
        youtube_url[movie]
    )
    list_movies.append(object_movie)  # add movie into list

# create webpage with fresh_tomotoes

fresh_tomatoes.open_movies_page(list_movies)
