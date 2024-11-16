import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
from numpy import random
import pyglet
import webbrowser
import serial

# set colours
menu_bg_color = "#000000"
menu_fg_color = "#ffffff"
menu_act_bg_color = "#000000"
menu_act_fg_color = "#808080"
bg_colour = "#ffffff"
fg_color = "#000000"
act_bg_color = "#ffffff"
act_fg_color = "#808080"

# load custom fonts
pyglet.font.add_file("fonts/Ubuntu-Bold.ttf")
pyglet.font.add_file("fonts/Shanti-Regular.ttf")

# set about website
new = 1
url = "https://sites.google.com/jeffcoschools.us/universal-nanolab/project-home-page"
url1 = "https://github.com/ClairBearmakes/NanoLab-GUI"

# initiallize app with basic settings
root = tk.Tk() # root is the main window name
root.title("Universal NanoLab Settings")

# getting screen dimentions of display
width= root.winfo_screenwidth()
height= root.winfo_screenheight()

# setting tk window size
root.geometry("%dx%d" % (width, height))
root.eval("tk::PlaceWindow . center")

# create a frame widgets
menu = tk.Frame(root, width=width, height="50", bg=menu_bg_color)
frame1 = tk.Frame(root, width=width, height=height - int(50), bg=bg_colour)
settings_frame = tk.Frame(root, width=width, height=height - int(50), bg=bg_colour)

# place frame widgets in window
menu.grid(row=0, column=0, sticky=tk.E+tk.W)
settings_frame.grid(rowspan=3, columnspan=3, row=1, column=0, sticky="nesw")

# funtion for about button website
def openweb():
    webbrowser.open(url,new=new)

# function for update button website
def openweb1():
	webbrowser.open(url1,new=new)

def clear_widgets(root):
	# select all frame widgets and delete them
	for widget in root.winfo_children():
		widget.destroy()

def load_menu(): # button bar on top
	# prevent widgets from modifying the frame
	menu.pack_propagate(False)

	tk.Button( # 'back' button widget (replace with back icon)
		menu,
		text="Back",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=menu_bg_color,
		fg=menu_fg_color,
		cursor="hand2",
		activebackground=menu_act_bg_color,
		activeforeground=menu_act_fg_color,
		command=lambda:load_settings_frame()
		).grid(row=0, column=0, sticky="w", padx="5", pady="3") # row==up and down, column==left and right

	# create about button widget
	tk.Button(
		menu,
		text="About",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=menu_bg_color,
		fg=menu_fg_color,
		cursor="hand2",
		activebackground=menu_act_bg_color,
		activeforeground=menu_act_fg_color,
		# webbrowser.open(url, new=new),
		command=openweb
		).grid(row=0, column=1, sticky="w", padx="5", pady="3")

	# create storage button widget
	tk.Button(
		menu,
		text="Storage",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=menu_bg_color,
		fg=menu_fg_color,
		cursor="hand2",
		activebackground=menu_act_bg_color,
		activeforeground=menu_act_fg_color,
		# command=lambda:load_menu() # open file explorer
		).grid(row=0, column=2, sticky="w", padx="5", pady="3")

	# create updates button widget
	tk.Button(
		menu,
		text="Updates",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=menu_bg_color,
		fg=menu_fg_color,
		cursor="hand2",
		activebackground=menu_act_bg_color,
		activeforeground=menu_act_fg_color,
		# webbrowser.open(url1, new=new),
		command = openweb1
		# command=lambda:load_menu() # open site with changes to code/app
		).grid(row=0, column=3, sticky="w", padx="5", pady="3")

	# create log button widget
	tk.Button(
		menu,
		text="Log",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=menu_bg_color,
		fg=menu_fg_color,
		cursor="hand2",
		activebackground=menu_act_bg_color,
		activeforeground=menu_act_fg_color,
		# command=lambda:load_menu() # open a log of what is happening right now
		).grid(row=0, column=4, sticky="w", padx="5", pady="3")
	
def load_settings_frame():
	# clear_widgets(frame1)
	# stack settings frame above frame 1
	# settings_frame.tkraise()
	# prevent widgets from modifying the frame
	settings_frame.pack_propagate(False)

	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((100, 100))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(settings_frame, image=logo_img, bg=bg_colour)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	# create data results button widget
	tk.Button(
		settings_frame,
		text="Data Results",
		font=("Ubuntu", 20),
		height=("2"),
		width=("17"),
		bg=bg_colour,
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		# command=lambda:load_settings_frame(), # load data results frame
		).grid(row=1, column=1, sticky="w", padx="8", pady="5")

# create water pump settings button widget
	tk.Button(
		settings_frame,
		text="Water Pump Settings",
		font=("Ubuntu", 20),
		height=("2"),
		width=("17"),
		bg=bg_colour,
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		# command=lambda:load_settings_frame(), # load water pump settings frame
		).grid(row=1, column=2, sticky="w", padx="8", pady="5")

	# create LED settings button widget
	tk.Button(
		settings_frame,
		text="LED Settings",
		font=("Ubuntu", 20),
		height=("2"),
		width=("17"),
		bg=bg_colour,
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		# command=lambda:load_settings_frame(), # LED settings frame
		).grid(row=1, column=3, sticky="w", padx="8", pady="5")

	# create fan settings button widget
	tk.Button(
		settings_frame,
		text="Fan Settings",
		font=("Ubuntu", 20),
		height=("2"),
		width=("17"),
		bg=bg_colour,
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		# command=lambda:load_settings_frame(), # load fan settings frame
		).grid(row=2, column=1, sticky="w", padx="8", pady="5")

	# create camera settings button widget
	tk.Button(
		settings_frame,
		text="Camera Settings",
		font=("Ubuntu", 20),
		height=("2"),
		width=("17"),
		bg=bg_colour,
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		# command=lambda:load_settings_frame(), # load camera settings frame
		).grid(row=2, column=2, sticky="w", padx="8", pady="5")

	# create atmospheric sensor button widget
	tk.Button(
		settings_frame,
		text="Atmospheric Sensor",
		font=("Ubuntu", 20),
		height=("2"),
		width=("17"),
		bg=bg_colour,
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		# command=lambda:load_settings_frame(), # load camera settings frame
		).grid(row=2, column=3, sticky="w", padx="8", pady="5")

	# load settings window
	command=lambda:load_settings_frame()
	print("settings loaded")



# ser = serial.Serial('COM3')
# # open serial port

 
# print(ser.name)
#  # check which port was really used
 
# ser.write(b'hello')
#  # write a string
 
# ser.close()
#  # close port	

# load the first frame and button bar
load_menu()
load_settings_frame()

# run app
root.mainloop()