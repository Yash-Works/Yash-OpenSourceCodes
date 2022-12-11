class Calc1:
    def add(self , a,b):
        return a + b

class Calc2:
    def multi(self , a, b):
        return a * b

class Calc3(Calc1, Calc2):
    def div(self , a ,b):
        return a/b

a = Calc3()
print(a.add(10,20))
print(a.multi(4,3))
print(a.div(10,5))