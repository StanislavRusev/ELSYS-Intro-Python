# Opening a file
file = open("test.txt")
print(file.read())
file.close()

# This line gives an error, because it's permission is write only. To read and write at the same time 
# We should simply use 'w+' or 'r+'
# file = open("test.txt")
file = open("test.txt", 'w+')
file.write("Hello, Tom. My name is Harry Potter")
print(file.read())
# Always close the file at the end of its usage
file.close()

# We can create a new file with 'w' or 'x'. The difference is if there is an existing one
# the 'x' will throw an error and the 'w' will override the existing one
file = open("new.txt", 'w')
file.write("I'm a new file")
file.close()
# Throws error - Already existing file
# file = open("new.txt", 'x')

# Reading the new file
file = open("new.txt", 'r')
print(file.read())
file.close()

# You want to write in a file without overriding it? Just use 'a' append. 
f = open("new.txt", "a+")
f.write(" Now the file has more content!")
f.close()
# Open and read the file after the appending:
f = open("new.txt", "r")
print(f.read())

# Let's look at a multiple line file
file = open("multilinetext.txt", 'r+')
# Read the first line of the file
print(file.readline()) # Returns the first line
print(file.readline()) # Which line does it return? First or second?
# Reset the page counter
file.seek(0)
print(file.readline()) # Returns the first line
file.seek(0)
print(file.readlines())
file.close()
# write a line
file = open("multilinetext.txt", "w+")
lines = ["Goeorgi, Aleksandur, Petur"]
file.writelines(lines)
print(file.readlines())

# Delete a file
#import os
#os.remove("new.txt")

# Check if file exists and then delete
# if os.path.exists("new2.txt"): - FALSE
#if os.path.exists("new.txt"):
#  os.remove("new.txt")
#else:
#  print("The file does not exist")

# Delete a folder
# os.rmdir("folder")

# using with 
with open("new.txt", "r") as file:
    print(file.read())
# You do not need to use file.close(), because with is calling __enter()__ and __exit()__ - built in methods

import os
#if os.path.exists(path):
#    print("True")


