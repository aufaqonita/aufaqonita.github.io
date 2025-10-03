
class Person:
    name = ""

    def__init__(self, name);
    self.name = name
    
    def getInfo(self):
        print("this person's name", self.name)


class Person:
    name = ""

    def__init__(self, name);
    self.name = name
    
    def getInfo(self):
        print("this person's name", self.name)



class Student(Person):
   pass
student1 = Student("Ahmad")
student.getInfo      

class Person:
    name = ""

    def__init__(self, name);
    self.name = name
    
    def getInfo(self):
        print("this person's name", self.name)



class Student(Person):
    def__init__(self, name, nis)
    self.name = name
    self.nis = nis
Person1 = Person("Ahmad")
Student1= Student("Beni","21211243")

class Student(Person):
    def__init__(self, name, nis)
    super().__init__(name)
    self.nis = nis
Person1 = Person("Ahmad")
Student1= Student("Beni","21211243")

class Student(Person):
    nis = ""

    def__init__(self, name, nis)
    super( ).__init__(name)
    self.nis = nis
    def study(subject):
       print(self.name, "is studying", subject)

Student1= Student("Beni", "20211243") 
Student1.study("Math")

class Student(Person):

    def__init__(self, name, nis)
    super( ).__init__(name)
    self.nis = nis

    def study(subject):
       print(self.name, "is studying", subject)
    def getInfo():
        print("This student's name is", self.name)  

Student1= Student("Beni", "20211243") 
Student1.getInfo()        