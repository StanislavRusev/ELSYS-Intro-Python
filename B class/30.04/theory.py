import os
import shutil

# Files

print(os.path.join("Users", "stanislavrusev", "Desktop"))

file = open("file1.txt", "+a")

fileData = file.read() # all of the file data
fileLine = file.readline() # one line
fileLine2 = file.readline() # another line
fileLines = file.readlines() # list of all the lines

# r - read - chetene of fail
# w - write - pisane vuv fail, kato faila se zachistva
# a - append - pisane vuv kraq na fail
# x - suzdavane na fail, ako ne sushtestuvava
# b - binary - otvarq fail vuv binaren rejim
# + - read + write

file.write("This is from theory.py")
file.write("This is also from there")

file.writelines(["This is the first line\n", "This is the second line\n"])
print(file.tell()) # see file pointer position
file.seek(10) # set file pointer position
print(file.read())

file.close()

shutil.copy("file1.txt", "file2.txt")
shutil.copy2("file1.txt", "file2.txt")
with open("file1.txt", "r") as file:
    print(file.read())

# Задача 1: Напишете функция, която прочита текстов файл и връща броя думи в него. След това изведете общия брой думи.
# Задача 2: Създайте функция, която прочита текстов файл и връща броя на редовете в него. Изведете общия брой редове.
# Задача 3: Направете функция, в която въвеждате двете си имена и класа и ги записвате в нов файл
# Задача 4: Напишете функция, която приема два файла и копира съдържанието на единия в другия файл.