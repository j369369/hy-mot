# 이재원 - 2023161840

# Write an if statement to determine if an album had a rating greater than 8. Test it using the rating for the album “Back in Black” that had a rating of 8.5. If the statement is true print "This album is Amazing!"
album_ratings = {"Back in Black":8.5, "The Bodyguard":9.0, "Thriller":7.8}
if album_ratings["Back in Black"] > 8:
    print("This album is Amazing!")
# Answer = This album is Amazing!

# Write an if-else statement that performs the following. If the rating is larger then eight print “this album is amazing”. If the rating is less than or equal to 8 print “this album is ok”.
if album_ratings["Back in Black"] > 8:
    print("This album is Amazing!")
else:
    print("This album is ok")
# Answer = This album is Amazing!

# Write an if statement to determine if an album came out before 1980 or in the years: 1991 or 1993. If the condition is true print out the year the album came out.
album_year = 1979
if album_year < 1980 or album_year == 1991 or album_year == 1993:
    print("This album came out", album_year)

