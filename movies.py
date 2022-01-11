current_movies = {
    "The Grinch": "11:00am",
    "Rudolph": "1:00pm",
    "Frosty the Snowman": "3:00pm",
    "Christmas Vacataion": "5:00pm",
}

print("We're showing the following movies:")
for key in current_movies:
    print(key)
movie = input("What movied would you like the show time for?\n")

showtime = current_movies.get(movie)
if showtime == None:
    print("Requested showtime is not playing")
else:
    print(movie, "is playing at", showtime)
