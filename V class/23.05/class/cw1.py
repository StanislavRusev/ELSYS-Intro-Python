class Counter:
    def __init__(self, initial = 0, step = 1):
        self.__total = initial
        self.__step = step
    def increment(self):
        self.__total += self.__step
    def get_total(self):
        return self.__total
    def get_step(self):
        return self.__step
    
    def __str__(self):
        return f"{self.__total} {self.__step}"
    def __add__(self, self2):
        return Counter(self.__total+self2.__total, self.__step+self2.__step)
    

c1 = Counter(0, 1)
c2 = Counter(0, 2)
c3 = c1 + c2
print(c3)
