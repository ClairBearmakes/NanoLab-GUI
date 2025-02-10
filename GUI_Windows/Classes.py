# classes

#"""
import tkinter as tk
import pyglet

# set fonts
pyglet.font.add_file("fonts/Ubuntu-Bold.ttf")
normal_font= ("Ubuntu", 12)
title_font= ("Ubuntu", 48)
calender_font= ("Arial", 10)

# set starting variables
dev_mode = True # if True will show log button and test buttons # Make a beta test review sheet to go with this or separate thing?
beta = True
dark_mode = False
component_count = 5
type_selected = False
box_type = ""
menu_height = 55

if dark_mode == False: 
	# set normal colors
	menu_bg_color = "#000000"
	menu_fg_color = "#ffffff"
	menu_act_bg_color = "#000000"
	bg_color = "#ffffff"
	fg_color = "#000000"
	act_bg_color = "#ffffff"
	act_fg_color = "#808080"
else: # fix these
	# set dark mode colors
	menu_bg_color = "#ffffff"
	menu_fg_color = "#000000"
	menu_act_bg_color = "#ffffff"
	bg_color = "#000000"
	fg_color = "#ffffff"
	act_bg_color = "#808080"
	act_fg_color = "#ffffff"

class Framework(tk.Tk):
	# config root window
	root=tk.Tk()
	self.width=width
	self.height=width
	root.geometry("%dx%d" % (width, height))
	root.title("Universal NanoLab Settings")
	root.configure(bg=bg_color)
	root.iconbitmap("assets/Universal logo.ico")

	def __init__(self, *args, **kwargs):
		frame = tk.Frame(self.root, highlightbackground="grey", highlightthickness=1, width=self.width, height=self.height - menu_height, bg=bg_color)
		frame.configure(bg=bg_color)

	def startframe1():
		

setup = Framework()
setup.mainloop()
#"""

"""
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
"""