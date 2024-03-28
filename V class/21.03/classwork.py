# function
def my_function():
    print("Hello world")

# calling a function
my_function()

# arguments
def my_function(name):
    print(name + " bhfhue")

my_function("emil")
my_function("Emil")
my_function("eMil")

# multiple arguments
def my_function(*kids):
    print("The youngest child in " + kids[1])

my_function("Emil", "Herb")

# multiple arguments with key
def my_function(**kid):
    print("His last name is " + kid["lname"])

# defining the keys 
my_function(fname = "Tobias", lname = "Frenski")

# default argument
def my_function(country = "Nprway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()

# passing list as an argument
def my_function(food):
    for x in food:
        print(x)

# list
fruits = ["apple", "banana"]
my_function(fruits)

# return
def my_function(x):
    return 5 * x
print(my_function(3))

# empty function
def my_function():
    pass