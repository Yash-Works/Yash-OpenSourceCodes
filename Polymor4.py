#Polymorphism with a Function & Object
class India():
    def capital(self): 
        print("New Delhi is the capital of India")

    def language(self):
        print("Many languages are spoken in India")
    
    def Space(self):
        print("India has I.S.R.O")

class USA():
    def capital(self):
        print("Washington DC is the capital of USA")
    def language(self):
        print("English the primary language spoken")
    
    def Space(self):
        print("USA has N.A.S.A")
def test(obj):
    obj.capital()
    obj.language()
    obj.Space()

obj1= India()
obj2 = USA()

test(obj1)
test(obj2)