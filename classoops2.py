class Animal:
    def speak(self):
        print("Animal is speaking")
    
class Dog(Animal):
    def bark(self):
        print("Dog is Barking")

class Puppy(Dog):
    def eat(self):
        print("Puppy is eating bread")

a =Puppy()
a.speak()
a.bark()
a.eat()