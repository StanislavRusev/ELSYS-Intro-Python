# За задачите нямате право да използвате цикли, позволени са само map, filter и reduce
# Задача 1: Да се напише функция, която приема лист от стрингове и връща лист от същите стрингове, но вече да са изцяло от главни букви
# Задача 2: Да се напише функция, която приема лист от имена и връща лист от тези имена, които 
# имат дължина по-малка от 7 букви
# Задача 3: Да се напише функция, която приема лист от числа и връща тяхното произведение
# Задача 4: Да се напише фунцкяи, която прочита думи от файл (всички думи са на един ред, разделени с " "),
# и връща лист от тези думи, които са палиндроми (четат се еднакво от ляво надясно, и обратното - от дясно наляво)
# Тук, ако искате може да ползвате цикъл при четенето на файла, но не и при премахването на думи, които не са палиндроми.

from functools import reduce

def mapUpper(l):
    return list(map(lambda x: x.upper(), l))

def filterLessThan7(l):
    return list(filter(lambda x: len(x) >= 7, l))

def reduceProduct(l):
    return reduce(lambda x, y: x * y, l, 1)

def filePalindrome():
    with open("words.txt") as file:
        l = file.read().split(" ")
    return list(filter(lambda x: x == x[::-1], l))

print(mapUpper(["asd", "Fghjk", "omgomg"]))
print(filterLessThan7(["Emanuel", "Pedro", "Ivan", "Alexander"]))
print(reduceProduct([2, 3, 5, 10]))
print(filePalindrome())
