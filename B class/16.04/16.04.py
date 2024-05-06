nums = [1,2,3,4,5,6,7]
#k = int(input())

def rotateOnce(nums):
    lastElement = nums[-1]
    # for i in range(len(nums)):
    #     firstElement = nums[i]
    #     nums[i] = lastElement
    #     lastElement = firstElement

    nums.pop(-1)
    nums.insert(0, lastElement)
    print(nums)
    

def rotateK(nums, k):
    for i in range(k):
        rotateOnce(nums)


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
    print(num % 2, end = "")


### New

list1 = [1, 3, 4, 5, 2]
print(list1)

def isBigger(num1, num2):
    return num1 > num2

def isSmaller(num1, num2):
    return num1 < num2


def mySelectionSort(list1, check):
    length = len(list1)

    for i in range(length):
        min_index = i

        for j in range(i + 1, length):
            if check(list1[j], list1[min_index]):
                min_index = j
        temp = list1[i]
        list1[i] = list1[min_index]
        list1[min_index] = temp

mySelectionSort(list1, isSmaller)
print(list1)

mySelectionSort(list1, isBigger)
print(list1)

