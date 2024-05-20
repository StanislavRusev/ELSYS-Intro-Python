# Lambdas, filter, map, reduce

def multiply(a, b):
    return a * b

def sum(a, b):
    return a + b

def applyF(a, b, f):
    return f(a, b)

def func():
    def innerFunc():
        print("Hello from innerFunc")
    return innerFunc

def add1(x):
    return x + 1

# print(applyF(2, 3, multiply))
# print(applyF(2, 3, sum))
# print(add1(2))
# print((lambda x: x + 1)(2))
# print((lambda a, b: a + b)(2, 3))

# list1 = [4, 2, 3, 1]
# print(list1)
# list1.sort(key=lambda x: -x)
# print(list1)

# Map
def my_map(list1, func):
    result = []

    for element in list1:
        result.append(func(element))
    
    return result

# print(my_map([1, 2, 3, 4], lambda a: a ** 3))
# print(list(map(lambda a: a * 2, [1, 2, 3, 4])))

# Filter
def my_filter(func, list1):
    result = []
    for element in list1:
        if func(element):
            result.append(element)
    return result

# print(my_filter(lambda a: a > 2, [1, 2, 3, 4]))
# print(list(filter(lambda a: a * a < 3, [1, 2, 3, 4])))

# Reduce
list1 = [2, 5, 7, 10]
def my_Reduce(list1, func, start):
    result = start
    for element in list1:
        result = func(result, element)
    return result

# print(my_Reduce(list1, lambda x, y: x + y, 0))
# # Import the Reduce
# from functools import reduce
# print(reduce(lambda x, y: x + y, list1, 0))

# Zadachi
from functools import reduce

list1 = ["asd", "Asd", "asdiasdunsdn"]
def toUpper(list1):
    return list(map(str.upper, list1))

print(toUpper(list1))

list1 = ["asd", "Asd", "asdiasdunsdn", "aaaaaaaa"]
def lessThan7(list1):
    return list(filter(lambda x: len(x) < 7, list1))
print(lessThan7(list1))

list1 = [1, 3, 2, 10]
def calcProd(list1):
    return reduce(lambda x, y: x * y, list1, 1)

print(calcProd(list1))