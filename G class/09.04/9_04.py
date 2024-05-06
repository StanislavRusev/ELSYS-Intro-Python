nums = [1, 2, 7, 3, 4, 5, 6, 7]
#k = int(input())

def rotateOnce(list1):
    lastElement = list1[-1]
    list1.pop(-1)
    # list1.reverse()
    # list1.remove(lastElement)
    # list1.reverse()
    list1.insert(0, lastElement)
    print(list1)

def rotateK(list1, k):
    for i in range(k):
        rotateOnce(list1)

def toBinary(num):
    list1 = []
    while num > 0:
        list1.append(num % 2)
        num = num // 2
    list1.reverse()
    print(list1)

def toBinaryRec(num):
    if num == 0:
        return
    toBinaryRec(num // 2)
    print(num % 2, end="")


#### New 

def isBigger(num1, num2):
    return num1 > num2

def isSmaller(num1, num2):
    return num1 < num2

def mySort(list1, check):
    length = len(list1)

    for i in range(length):
        min_index = i

        for j in range(i + 1, length):
            if check(list1[j], list1[min_index]):
                min_index = j

        temp = list1[i]
        list1[i] = list1[min_index]
        list1[min_index] = temp

list1 = [1, 4, 3, 2, 5]
print(list1)
mySort(list1, isBigger)
print(list1)
mySort(list1, isSmaller)
print(list1)
    


