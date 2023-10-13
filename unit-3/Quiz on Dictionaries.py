# 이재원 - 2023161840

# Question sample dictionary

soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}

# 1. In the dictionary soundtrack_dict what are the keys ?
print(soundtrack_dic.keys())
# Answer = dict_keys(['The Bodyguard', 'Saturday Night Fever'])

# 2. In the dictionary soundtrack_dict what are the values ?
print(soundtrack_dic.values())
# Answer = dict_values(['1992', '1977'])

# 3. The Albums Back in Black, The Bodyguard and Thriller have the following music recording sales in millions 50, 50 and 65 respectively:
# a) Create a dictionary album_sales_dict where the keys are the album name and the sales in millions are the values.
album_sales_dict = {"Back in Black":50, "The Bodyguard":50, "Thriller":65}
print(album_sales_dict)
# Answer = {'Back in Black': 50, 'The Bodyguard': 50, 'Thriller': 65}

# b) Use the dictionary to find the total sales of Thriller:
print(album_sales_dict["Thriller"])
# Answer = 65

# c) Find the names of the albums from the dictionary using the method keys:
print(album_sales_dict.keys())
# Answer = dict_keys(['Back in Black', 'The Bodyguard', 'Thriller'])

# d) Find the values of the recording sales from the dictionary using the method values:
print(album_sales_dict.values())
# Answer = dict_values([50, 50, 65])
