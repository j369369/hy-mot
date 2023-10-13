# 이재원 - 2023161840

# 1. Write a for loop the prints out all the element between -5 and 5 using the range function.
for i in range(-5, 6):
    print(i)
# Answer = -5 ~ 5

# 2. Print the elements of the following list: Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop'] Make sure you follow Python conventions.
Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for i in Genres:
    print(i)
# Answer = rock R&B Soundtrack R&B soul pop

# 3. Write a for loop that prints out the following list: squares=['red', 'yellow', 'green', 'purple', 'blue']
squares=['red', 'yellow', 'green', 'purple', 'blue']
for i in squares:
    print(i)
# Answer = red yellow green purple blue

# 4. Write a while loop to display the values of the Rating of an album playlist stored in the list PlayListRatings. 
# If the score is less than 6, exit the loop. The list PlayListRatings is given by: PlayListRatings = [10,9.5,10,8,7.5,5,10,10]
PlayListRatings = [10,9.5,10,8,7.5,5,10,10]
i = 0
while PlayListRatings[i] >= 6:
    print(PlayListRatings[i])
    i += 1
# Answer = 10 9.5 10 8 7.5

# 5. Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. 
# Stop and exit the loop if the value on the list is not 'orange':
squares=['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while squares[i] == 'orange':
    new_squares.append(squares[i])
    i += 1
print(new_squares)
# Answer = ['orange', 'orange']
