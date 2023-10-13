# 이재원 - 2023161840

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", "R&B", "progressive rock", "disco") 

# 1. Find the length of the tuple, genres_tuple:
print(len(genres_tuple))
# Answer = 8

# 2. Access the element, with respect to index 3:
print(genres_tuple[3])
# Answer = hard rock

# 3. Use slicing to obtain indexes 3, 4 and 5:
print(genres_tuple[3:6])
# Answer = ('hard rock', 'soft rock', 'R&B')

# 4. Find the first two elements of the tuple genres_tuple:
print(genres_tuple[0:2])
# Answer = ('pop', 'rock')

# 5. Find the first index of "disco":
print(genres_tuple.index("disco"))
# Answer = 7

# 6. Generate a sorted List from the Tuple C_tuple=(-5, 1, -3):
C_tuple = (-5, 1, -3)
print(sorted(C_tuple))
# Answer = [-5, -3, 1]