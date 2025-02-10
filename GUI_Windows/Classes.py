# classes

#"""
import tkinter as tk
import pyglet

# set normal colors
bg_color = "#ffffff"
fg_color = "#000000"
act_bg_color = "#ffffff"
act_fg_color = "#808080"

# set fonts
pyglet.font.add_file("fonts/Ubuntu-Bold.ttf")
normal_font= ("Ubuntu", 12)
title_font= ("Ubuntu", 48)
calender_font= ("Arial", 10)

# set vars
compnum = 5 # number of components
menu_height = 55

class Framework(tk.Tk):
	root = tk.Tk()
	width=600
	height=500
	root.geometry("%dx%d" % (width, height))
	root.title("Universal NanoLab Settings")
	root.configure(bg=bg_color)
	# set logo
	root.iconbitmap("assets/Universal logo.ico")

	def __init__(self, *args, **kwargs):
        
		# self.root.__init__(self, *args, **kwargs)
		container = tk.Frame(self.root, highlightbackground="grey", highlightthickness=1, width=self.width, height=self.height - menu_height, bg=bg_color)
		container.configure(bg=bg_color)

		container.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		frame = StartPage(container, self)

		self.frames[StartPage] = frame

		frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()

        
class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="Welcome to your NanoLab!", font=("Ubuntu-Bold", 20), bg=bg_color)
		label.grid(row=0, columnspan=8, column=0, sticky="")


app1 = Framework()
app1.mainloop()
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