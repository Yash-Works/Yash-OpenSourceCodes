#polymorphism with inheritance
class bird:
    def intro(self):
        print("Hi this is a bird")

    def flight(self):
        print("Most of the birds can fly")

class parrot(bird):
    def flight(self):
        print("Parrots can fly")
class ostrich(bird):
    def flight(self):
        print("Ostrich can't fly")

obj1=bird()
obj2=parrot()
obj3=ostrich()

obj1.intro()
obj1.flight()

obj2.intro()
obj2.flight()

obj3.intro()
obj3.flight()
