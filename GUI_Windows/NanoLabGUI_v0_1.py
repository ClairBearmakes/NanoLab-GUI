
# Code writen by Asher Powell at Warren Tech North
# Version 0.1
vernum = "0.1"

import tkinter as tk
from PIL import ImageTk
import sqlite3
from numpy import random
import pyglet

# set colours
bg_colour = "#808080"

# load custom fonts
pyglet.font.add_file("fonts/Ubuntu-Bold.ttf")

def clear_widgets(frame):
	# select all frame widgets and delete them
	for widget in frame.winfo_children():
		widget.destroy()

def fetch_db():
	# connect an sqlite database
	connection = sqlite3.connect("data/recipes.db")
	cursor = connection.cursor()

	# fetch all the table names
	cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
	all_tables = cursor.fetchall()

	# choose random table idx
	idx = random.randint(0, len(all_tables)-1)

	# fetch records from table
	table_name = all_tables[idx][1]
	cursor.execute("SELECT * FROM " + table_name + ";")
	table_records = cursor.fetchall()

	connection.close()

	return table_name, table_records

def pre_process(table_name, table_records):
	# preprocess table name
	title = table_name[:-6]
	title = "".join([char if char.islower() else " " + char for char in title])

	# preprocess table records
	ingredients = []

	for i in table_records:
		name = i[1]
		qty = i[2]
		unit = i[3]
		ingredients.append(qty + " " + unit + " of " + name)

	return title, ingredients

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
	logo_widget.pack()

	# create button widget
	tk.Button(
		frame1,
		text="START",
		font=("Ubuntu", 30),
		bg="#28393a",
		fg="white",
		cursor="hand2",
		activebackground="#badee2",
		activeforeground="black",
		command=lambda:load_frame2()
		).pack(pady=20)

def load_frame2():
	clear_widgets(frame1)
	# stack frame 2 above frame 1
	frame2.tkraise()

	# fetch from database
	table_name, table_records = fetch_db()
	title, ingredients = pre_process(table_name, table_records)

	# create logo widget
	logo_img = ImageTk.PhotoImage(file="assets/NanoLabs_logo.png")
	logo_widget = tk.Label(frame2, image=logo_img, bg=bg_colour)
	logo_widget.image = logo_img
	logo_widget.pack(pady=20)

	# recipe title widget
	tk.Label(
		frame2, 
		text=title,
		bg=bg_colour,
		fg="white",
		font=("Ubuntu", 20)
		).pack(pady=25, padx=25)

	# recipe ingredients widgets
	for i in ingredients:
		tk.Label(
			frame2, 
			text=i,
			bg="#28393a",
			fg="white",
			font=("Shanti", 12)
			).pack(fill="both", padx=25)

	# 'back' button widget
	tk.Button(
		frame2,
		text="BACK",
		font=("Ubuntu", 18),
		bg="#28393a",
		fg="white",
		cursor="hand2",
		activebackground="#badee2",
		activeforeground="black",
		command=lambda:load_frame1()
		).pack(pady=20)


# initiallize app with basic settings
root = tk.Tk() # root is the window name
root.title("Universal NanoLab Settings")

# place app in the center of the screen (alternative approach to root.eval())
# x = root.winfo_screenwidth()
# y = int(root.winfo_screenheight())
# root.geometry('1920x1080+' + str(x) + '+' + str(y))

# getting screen dimentions of display
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
# width= int(width)
# height= int(height)

# setting tk window size
root.geometry("%dx%d" % (width, height))
root.eval("tk::PlaceWindow . center")

# create a frame widgets
frame1 = tk.Frame(root, width=width, height=height, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)

# place frame widgets in window
for frame in (frame1, frame2):
	frame.grid(row=0, column=0, sticky="nesw")

# load the first frame
load_frame1()

# run app
root.mainloop()
