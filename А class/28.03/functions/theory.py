# tuple
#t = (1, "b", False)

#print(f"{t = }")

#list
#l = [1, "b", False]
    
#print(f"{l = }")

#set
#s = {1, "b", False}

#print(f"{s = }")

# dictionary
#d = {"a": 1, "b": 2, "c": 3, "d": 4}

#print(f"{d = }")

# empty set
# s = set()
# empty dictionary
# d = {}

# in
#if(2 in d):
#    print("yes")
#else:
#    print("no")
    
#if("mile" in "Smile" and "ile" in "Smile") :
#    print("yes")
#else:
#    print("no")


# changing list values using index
#l[0] = 2
#print(f"{l = }")

# Error when trying to change set
# s[0] = 2
#print(f"{s = }")

# print(d["e"])
#print(d.get('e'))

# functions

def my_function():
    print("Hello")

# calling a function
my_function()

# arguments
def function_arguments(fname, age):
    print("Hello " + fname)

function_arguments("Alex", 1)

# many arguments *args
def function_multiple_arguemnts(*student):
    print(student[1])


function_multiple_arguemnts("Dara", "Filip")

# defining arguments
def function_multiple_arguemnts(student1, student2, student3):
    print(student1)


function_multiple_arguemnts(student1="Dara", student3="Filip", student2="Georgi")

# non defined arguments
def function_non_defined_arguemnts(**students):
    print(students["student1"])

function_non_defined_arguemnts(student1="Dara", student3="Filip", student2="Georgi")

# default argument
def country_function(country = "Norway"):
    print(country)

country_function("Moldova")
country_function()

# list
l = [1, 2, 3]
def list_function(list) :
    for i in list:
        print(i)

list_function(l)

# return
def funtion_return(x):
    return x * 2

funtion_return(5)
print(funtion_return(3))
a = funtion_return(6)
print(a)

# empty function
def future_function():
    pass