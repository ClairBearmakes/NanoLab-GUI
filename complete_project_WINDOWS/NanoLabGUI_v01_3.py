import tkinter as tk
from PIL import ImageTk
import sqlite3
from numpy import random
import pyglet
# Test Commit?
# set colours
bg_colour = "white"
menu_bg_color = "black"
fg_color = "white"
act_fg_color = "#808080"

# load custom fonts
pyglet.font.add_file("fonts/Ubuntu-Bold.ttf")
pyglet.font.add_file("fonts/Shanti-Regular.ttf")

def clear_widgets(frame):
	# select all frame widgets and delete them
	for widget in frame.winfo_children():
		widget.destroy()

def load_menu(): # button bar on top
	menu.pack_propagate(False)

	# 'back' button widget (replace with back icon)
	tk.Button(
		menu,
		text="Back",
		font=("Ubuntu", 12),
		bg=menu_bg_color,
		fg=fg_color,
		cursor="hand2",
		activebackground=menu_bg_color,
		activeforeground=act_fg_color,
		command=lambda:load_frame1()
		).grid(row=0, column=0, sticky="w", padx="8", pady="5") # row==up and down, column==lefft and right

	# create about button widget
	tk.Button(
		menu,
		text="About",
		font=("Ubuntu", 12),
		bg=menu_bg_color,
		fg=fg_color,
		cursor="hand2",
		activebackground=menu_bg_color,
		activeforeground=act_fg_color,
		# command=lambda:load_menu() # load the about frame
		).grid(row=0, column=1, sticky="w", padx="8", pady="5")

	# create storage button widget
	tk.Button(
		menu,
		text="Storage",
		font=("Ubuntu", 12),
		bg=menu_bg_color,
		fg=fg_color,
		cursor="hand2",
		activebackground=menu_bg_color,
		activeforeground=act_fg_color,
		# command=lambda:load_menu() # open file explorer
		).grid(row=0, column=2, sticky="w", padx="8", pady="5")

def load_frame1():
	clear_widgets(frame2)
	# stack frame 1 above frame 2
	frame1.tkraise()
	# prevent widgets from modifying the frame
	frame1.pack_propagate(False)

	# create logo widget
	logo_img = ImageTk.PhotoImage(file="assets/NanoLabs_logo.png")
	logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0)

	# load settings window
	command=lambda:load_frame2()
	print("settings loaded")

def load_frame2():
	clear_widgets(frame1)
	# stack frame 2 above frame 1
	frame2.tkraise()

	# create logo widget
	logo_img = ImageTk.PhotoImage(file="assets/NanoLabs_logo.png")
	logo_widget = tk.Label(frame2, image=logo_img, bg=bg_colour)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0)

	# data results button
	tk.Button(
		frame2, 
		text="Data Results",
		bg=bg_colour,
		fg="white",
		font=("Ubuntu", 20)
		).grid(row=1, column=0)

# initiallize app with basic settings
root = tk.Tk() # root is the main window name
root.title("Universal NanoLab Settings")

# place app in the center of the screen (alternative approach to root.eval())
# x = root.winfo_screenwidth()
# y = int(root.winfo_screenheight())
# root.geometry('1920x1080+' + str(x) + '+' + str(y))

# getting screen dimentions of display
width= root.winfo_screenwidth()
height= root.winfo_screenheight()

# setting tk window size
root.geometry("%dx%d" % (width, height))
root.eval("tk::PlaceWindow . center")

# create a frame widgets
menu = tk.Frame(root, width=width, height="50", bg="#000000")
frame1 = tk.Frame(root, width=width, height=height - int(50), bg=bg_colour)
frame2 = tk.Frame(root, width=width, height=height - int(50), bg=bg_colour)

# place frame widgets in window
menu.grid(row=0, column=0, sticky=tk.E+tk.W)
for frame in (frame1, frame2):
	frame.grid(rowspan=2, row=1, column=0, sticky="nesw")

# load the first frame
load_menu()
load_frame1()

# run app
root.mainloop()
