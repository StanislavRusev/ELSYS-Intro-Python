# Lambdas, filter, map, reduce

def multiply(a, b):
    return a * b

def sum(a, b):
    return a + b

def applyF(a, b, f):
    return f(a, b)

# print(applyF(2, 3, multiply))
# print(applyF(2, 3, sum))

def func():
    def innerFunc():
        print("Hello from innerFunc")
    def secondFunc():
        print("Hello from second")
    
    return secondFunc

def add1(x):
    return x + 1

# lambda x: x + 1
# print((lambda a, b: a + b)(2, 3))


# list1 = [5, 3, 4, 1, 2]
# print(list1)
# list1.sort(key=lambda x: -x)
# print(list1)

# Map

def my_map(f, list1):
    result = []
    for i in list1:
        result.append(f(i))
    return result

# print(my_map(lambda x: x ** 3, [1, 2, 3, 4]))
# print(my_map(lambda x: x ** 2, [1, 2, 3, 4]))
# print(my_map(lambda x: x + 10, [1, 2, 3, 4]))

# print(list(map(lambda x: x ** 3, [1, 2, 3, 4])))

# Filter
def my_filter(f, list1):
    result = []
    for i in list1:
        if f(i):
            result.append(i)
    return result

# print(my_filter(lambda x: x % 2 == 1, [1, 2, 3, 4]))
# print(my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))

# print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))

# Reduce

def my_reduce(f, list1, start):
    result = start
    for i in list1:
        result = f(result, i)
    return result

# print(my_reduce(lambda res, x: res + x, [1, 2, 3, 4], 0))


# Import the reduce
from functools import reduce
# print(reduce(lambda res, x: res + x, [1, 2, 3, 4], 0))

# Zadachi
list1 = ["asd", "Bsasd", "asdasd", "asdasdhasdghasvdyasdu"]
def listToUpper(list1):
    return list(map(str.upper, list1))

print(listToUpper(list1))

def lessThan7(list1):
    return list(filter(lambda x: len(x) < 7, list1))

print(lessThan7(list1))

def prodList(list1):
    return reduce(lambda x, y: x * y, list1, 1)

print(prodList([2, 3, 5]))

def filePalindrome():
    with open("words.txt") as file:
        l = file.read().split(" ")
    return list(filter(lambda x: x == x[::-1], l))
