class College:
    def __init__(self):
        print("Meerut Institute of Engineering and Technology")
        
    def address(self):
        print("Meerut, Uttar Pradesh")
        
    def pincode(self):
        print("250110")
        
class Student(College):
    def __init__(self):
        College.__init__(self)
        print("Vansh Arora")
        
    def rollno(self):
        print("181B225")
        
    def branch(self):
        print("CSE")
        
    def year(self):
        print("2nd Year")
        
    def section(self):
        print("A")
        
    def address(self):
        print("Meerut, Uttar Pradesh")
        
    def pincode(self):
        print("250110")            

a = Student()
a.year()
a.branch()
a.address()