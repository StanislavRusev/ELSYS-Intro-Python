# Това е int - цяло число
a = 42
print("a = ", a)

# Нека сега е float - реално число
a = 42.5
print("a = ", a)

# Можем да добавим символен низ след числото като използваме функцията str(), която преобразува даден тип в символен низ
print("a = " + str(a))

# А сега нека е string - низ от символи
a = "This is a string"
print("a = ", a)

# Низовете могат да бъдат обградени както от двойни, така и от единични кавички
a = 'This is also a string'

# Оператори за аритметични операции
# Събиране
a = 42
b = 2
print("a = ", a)
print("b = ", b)
print("a + b = ", a + b) # 42 + 2 = 44

# Изваждане
print("a - b = ", a - b) # 42 - 2 = 40

# Умножение
print("a * b = ", a * b) # 42 * 2 = 84

# Дробно деление
c = 4
print("c = ", c)
print("a / b = ", a / b) # 42 / 2 = 21.0
print("a / c = ", a / c) # 42 / 4 = 10.5

# Целочислено деление (закръгля надолу)
print("a // b = ", a // b) # 42 / 2 = 21
print("a // c = ", a // c) # 42 / 4 = 10

# Остатък от деление
print("a % c = ", a % c) # 42 % 4 = 2

# Вдигане на степен
print("4 ** 2 = ", 4 ** 2) # 4^2 = 16 

# Може да залепяме низове с оператор '+'
print("This is а " + " string")

# Може да правим многоредови низове като използваме 3 пъти двойни кавички
multiLine = """First line
Second Line
Third Line
"""
print(multiLine)

# Използваме input() за да поискаме вход от потребителя
# Ако искаме вътре в скобите може да сложим съобщение, което ще се изведе, когато се очаква въвеждането

name = input("Please enter your name: ")
print("Hello, " + name)
