
"""
A class is a blueprint or a template that defines the properties (attributes) and functionalities (methods) of similar objects.
An object is an instance of a class. It's a concrete realization of the class definition.

Relationship Between Class and Object:
You create a class first, which serves as the blueprint.
Then, you use the class to create objects (instances).
Multiple objects can be created from a single class, each with its own unique set of attribute values.
This process is called procedural programming  ( Object oriented programming)

we have two things
attributes (what they have) and methods ( and what they can do) using functions

class and object Syntax
----------------------------------------------------------------------------
#defining new object type
class className:
      statements

#creating an object
objectName = className()
"""

#constructing class and objects (attributes and methods)

"""
The __init__() function: It is automatically executed when a new instance of class is created. 
It allows the class to initialize object's properties or other operations which is needed to create an object.

"""
#example 1
class university: #object
  def __init__ (self):  #method
    self.student_name = "Mandela Thomnas"  #attributes
    self.student_age = 29
    self.student_major = "Data Analytics"
    self.Student_education = "PHD"

# Call object methods
atsmas_university = university()
# Access object attributes
print(atsmas_university.student_name)


#Example 2
# ---- Assigning parameters to an attributes with classes and objects---

class college:
      #Attributes (define college properties)
  def __init__(self, name, age, major, gpa):
    self.name = name
    self.age = age
    self.major = major
    self.gpa = gpa
#Create objects (Instances) from the college class)
atsmas_college = college('Mandela Thomas', 29, 'healthcare Management', 4.0)
print(atsmas_college.age)

#Example 3
#----- using two methods

class techincal:
#Attributes (define college properties)
  def __init__(self, fname, education, profession, university):
    self.fname = fname
    self.education = education
    self.profession = profession
    self.university = university

 #Methods (define technical functionalities)
  def info(self):
    print(f"My name is {self.fname} and I a {self.education} researcher at the {self.university}")
    print(f"I work as the {self.profession} of ATS Meta Analytics LLC, a USA and Int'l based company")

#Create objects (Instances) from the college class)
myinfo = techincal("Mandela Thomas", "Doctoral", "Senoir Strategic Consultant", "Walden University")
# Call object methods
myinfo.info()
