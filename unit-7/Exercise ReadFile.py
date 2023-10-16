# 이재원 - 2023161840

# from google.colab import drive
# drive.mount('/content/gdrive')
# 저는 colab을 사용하지 않아서 이 부분은 주석처리했습니다.

# file reading 하는 코드 작성해줘
# open() 함수를 사용해서 파일을 읽어옵니다.

example1 = "Example1.txt"
file1 = open(example1, "r") #"r"는 example1 객체를 읽을 수 있는 상태로 만들자. 

print(file1.name) # 파일의 이름을 출력합니다.


FileContent = file1.read() # 파일의 내용을 읽어옵니다.
print(FileContent) # 파일의 내용을 출력합니다.

type(FileContent) # 파일의 타입을 출력합니다.

file1.close() # 파일을 닫습니다.


# ex1
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)


# ex2
with open(example1, "r") as file1:
    print(file1.read(4))

# ex3
with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))

# ex4
with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))

# ex5
with open(example1, "r") as file1:
    print("first line: " + file1.readline())
    print("second line: " + file1.readline())
    print("third line: " + file1.readline())

# ex6    
with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1;

# ex7
with open(example1, "r") as file1:
    FileAsList = file1.readlines()
    print(FileAsList[0])
    print(FileAsList[1])
    print(FileAsList[2])