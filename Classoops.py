#inheritance
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self , name, age, year):
        super().__init__(name, age)
        self.year= year

    def Welcome(self):
        print("Welcome",self.name," ,You are",self.age,"years old",",Your D.O.B is",self.year)

a = Employee("Yash", 17, 2005)
a.Welcome()