# 이재원 - 2023161840

# from google.colab import drive
# drive.mount('/content/gdrive')
# 저는 colab을 사용하지 않아서 이 부분은 주석처리했습니다.

# file reading 하는 코드 작성해줘
# open() 함수를 사용해서 파일을 읽어옵니다.

filePath = "Example2.txt"


# file writing
with open(filePath, 'w') as writefile:
    writefile.write("This is line A")

# file reading
with open(filePath, "r") as file1:
    FileContent = file1.read()
    print(FileContent)



with open(filePath, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")
    writefile.write("This is line 10\n")


Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]

with open(filePath, 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)



with open(filePath, "r") as file1:
    FileContent = file1.read()
    print(FileContent)




# Append
with open(filePath, 'a') as writefile:
    writefile.write("This is line D\n")



# copy file
with open(filePath,'r') as readFile:
    with open('Example3.txt','w') as writefile:
          for line in readFile:
                writefile.write(line)

# check
with open('Example3.txt', "r") as file1:
    FileContent = file1.read()
    print(FileContent)
