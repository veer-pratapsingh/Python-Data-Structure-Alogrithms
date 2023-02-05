#POLYMORPHISM
#Different object classes can share the same method name,and those mathod can be called from the same place even through a different objects passed in
class Vansh:
    def __init__(self, name):
        self.name = name
    def type(self):
        return "Java"
    
class Veer:
    def __init__(self, name):
        self.name = name
    def type(self):
        return "Python"
    
person1 = Vansh("Vansh Arora")
person2 = Veer("Veer Pratap Singh")

print(person1.type())
print(person2.type())

for i in [person1, person2]:
    print(i.name)
    print(i.type())
    print("**********")