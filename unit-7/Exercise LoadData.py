# 이재원 - 2023161840

import pandas as pd

# initialize list of lists
data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}

# Create DataFrame
df = pd.DataFrame(data)

# Print the output.
print(df)


csvFilePath = "unit-7/TopSellingAlbums.csv"
df = pd.read_csv(csvFilePath)


# Print last five rows of the dataframe
df.tail()



xlsxFilePath = "unit-7/TopSellingAlbums.xlsx"
df = pd.read_excel(xlsxFilePath)
df.head()

x = df[['Genre']]
x

y = df[['Length']]
y

z = df[['Artist']]
z


xyz = df[['Artist','Length','Genre']]
xyz


df.iloc[0, 0] #첫번째 행, 첫번째 열 
df.iloc[1, 0] #두번째 행, 첫번째 열
df.iloc[2, 0] #세번째 행, 첫번째 열

df.iloc[0, 1] #첫번째 행, 두번째 열
df.iloc[1, 1] #두번째 행, 두번째 열

df.loc[0, 'Artist'] #첫번째 행, Artist 열
df.loc[1, 'Artist'] #두번째 행, Artist 열

df.loc[0, 'Released'] #첫번째 행, Released 열
df.loc[1, 'Released'] #두번째 행, Released 열

df.iloc[0:2, 0:3] #첫번째 행부터 두번째 행, 첫번째 열부터 세번째 열

df.loc[0:2, 'Artist':'Released'] #첫번째 행부터 세번째 행, Artist 열부터 Released 열


for i, j in df.iterrows():
    print(i, j)
    print()


filter2 = df["Claimed Sales (millions)"]>40
df.where(filter2)

# Quiz on DataFrame

# Use a variable q to store the column Rating as a dataframe
q = df[['Rating']]
q

# Assign the variable q to the dataframe that is made up of the column Released and Artist:
q = df[['Released', 'Artist']]
q


# Access the 2nd row and the 3rd column of df:
df.iloc[1, 2]
