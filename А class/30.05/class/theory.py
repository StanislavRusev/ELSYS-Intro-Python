# OOP
class Product:
    def __init__(self, name, price):
       # self.__name = name // private - can not be accessed outside the class
        self.name = name
        self.price = price

#    def changeName(self):
#       self.__name = "Krastavitsa"
    
    def __str__(self):
        return f"{self.name}: {self.price} lv."
    
    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

p1 = Product("Banitsa", 2)
p2 = Product("Banitsa", 2)
p3 = Product("Krastavitsa", 1)
#p1.changeName()
print(p1 == p3)

# Magic methods
# https://realpython.com/python-magic-methods/

