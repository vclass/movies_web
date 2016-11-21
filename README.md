# MoviesWeb
MovieWeb is a Movie Trailer Website where users can see list of movies and watch the trailers. 

# Description
MovieWeb is wrote in Pyhon. Descriptions and details of the movies are pulled from OMDb API (https://www.omdbapi.com/)
There are 3 python files and 1 html file showing example of webpage output 

1. media.py - movie class that contains description of movie including trailer link and image
2. entertainment_center.py - initializes movie instances from movie class, make the list, and send to fresh_tomatoes to generate html page
3. fresh_tomatoes.py - recieve list of Movie instance to display in html page

# How to run 
1. Install python 2.7.x
2. Download 3 python files media.py, entertainment_center.py, and fresh_tomatoes.py into same folder
3. Execute entertainment_center.py
