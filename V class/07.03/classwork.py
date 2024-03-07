# l = [1, "b", False] # list (масив)

# print(f"{l = }")
# l[-1] = True
# print(f"{l = }")


# t = (91, "b", False) # tuple лист, който не можеш да промениш
# t = 1,
# print(f"{t = }")


# s = {1, "b", False} # set
# print(f"{s = }")


# d = {"a":1, "d":2, "j":3, "f":None,} # dictionary

# print(f"{d = }")

# print(f"{d['b'] = }")
# print(f"{d.get('b',0) = }")


# impostor = 1j   #in
# squad = [0, 1j, 2, 3, 4, 5]
# print(f"{impostor in squad = }")

# members = {"A": 0, "B":1j, "C":2}
# print(f"{impostor in members = }")

# print("mile" in "lime")


# print(len([0, 1, 2]))

lowerBound = int(input("Enter lower bound: "))
upperBound = int(input("Enter upper bound: "))

for i in range(lowerBound, upperBound):
    isPrime = True
    if i <= 1:
        isPrime = False
    else:
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
    
    if isPrime is True:
        print(i, " ")