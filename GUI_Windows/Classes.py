# classes

# https://pythonprogramming.net/object-oriented-programming-crash-course-tkinter/

# create class
class person:
	lastname = "Powell" # class attribute

	def __init__(self, name, age, height): # setting instance vars 
		self.name = name # instance attribute
		self.age = age # instance attribute
		self.height = height # instance attribute
		self.othername = ""
		# self.lastname = self.othername # this breaks things

	def __str__(self): # string representation of class vars the good way
		return f"{self.name} {self.lastname} is {self.age} years old and their height is {self.height} inches."

# create object of the class
person1 = person("Asher", 17, 62)
print(person1)

# call and concatenate attributes the boring way
allinfo1 = str(person1.name) + " " + str(person1.lastname) + ", age " + str(person1.age) + ", height " + str(person1.height) + " inches"
# print(allinfo1)
# print("**************************")

# create 2nd object of the class
person2 = person("Rick", 800, 68)

print(person2)

# modifying instance var
person2.age = 1250
person2.height = 60
print(person2)

# modifying class var
person.lastname = "Albrecht"
person3 = person("Dave", 400000, 65)
print(person3)

print(person1)