# WAP to ask the user to enter names of their three favorite movies and store them into list


# creating a list
fav_movies=[]

for i in range(3):
    movies=input("Enter your favorite movie :")
    fav_movies.append(movies)

print("the favorite movies are ",fav_movies)