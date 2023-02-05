"""class Student:
    print("Hello Everyone!")
x = Student()
print(type())"""

"""class Student:
    def func():
        print("Hello we are learning Python")
        
Student.func()"""

"""class Student:
    def func(self):
        print("Hello we are learning Python")
x= Student()
x.func()"""

#Class object attribute - Same for any instance of the class
"""class Student:
    year = '2023'
    def func():
        print("Hello we are learning Python")
    
x = Student()
print(x.year)"""

"""class Student:
    year = '2023'
    def func(self):
        print("Hello we are learning Python", self.year)
        
x = Student()
x.func()"""

"""class Student:
    def __init__(self, name): #__init_ (Method) to initialize attribute of an object 
        self.name = name #self.name = attribute initialized
#(Creating Instance of Student class {Object of certain class})
elon = Student (name='Elon Musk !') #name: argument

print (elon.name) #accessing class attribute through object"""

"""class Student:
    def __init__(self,name):
        self.name=name
vansh = Student(name="VANSH ARORA")
print(vansh.name)"""

"""class Student:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
vansh = Student(name="Vansh Arora",age=21)
print(vansh.name)        
print(vansh.age)"""

"""class Student:
    Total = 500

    def __init__(self, marks):
        self.marks= marks
        print("Initialised...")
        
    def findloss(self):
        return self.Total - self.marks
    
    def findpercentage(self):
        return self.marks/self.Total*100
    
a = Student(marks=450)
print("Total marks:",a.Total)
print("Lossed marks:",a.findloss())
print("Percentage:",a.findpercentage()"""
            
class Student:
    def __init__(self, name, age, marks, gender):
        self.name = name
        self.age = age
        self.marks = marks
        self.gender = gender
        print("Initialised...")
        
    def __len__(self):
        return self.marks
    
    def __str__(self):
        return " Name : %s |  Age : %s  | Marks : %s  | Gender : %s" %(self.name, self.age, self.marks, self.gender)
    
    def __del__(self):
        print("Student Database is deleted")
        
a = Student("Vansh",21,450,"male")
print(a)
print("Marks:",len(a))
del a                    
