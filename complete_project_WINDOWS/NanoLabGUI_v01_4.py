import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
from numpy import random
import pyglet
import webbrowser
import serial
import sys
import glob

# set colours
menu_bg_color = "#000000"
menu_fg_color = "#ffffff"
menu_act_bg_color = "#000000"
menu_act_fg_color = "#808080"
bg_color = "#ffffff"
fg_color = "#000000" # normal

# colors
red_fg = "red"
orange_fg = "orange"
yellow_fg = "yellow"
green_fg = "green"
blue_fg = "blue"
purple_fg = "purple"
violet_fg = "violet"

act_bg_color = "#ffffff"
act_fg_color = "#808080"

# load custom fonts
pyglet.font.add_file("fonts/Ubuntu-Bold.ttf")
pyglet.font.add_file("fonts/Shanti-Regular.ttf")

# set about website
new = 1
url = "https://sites.google.com/jeffcoschools.us/universal-nanolab/project-home-page"
url1 = "https://github.com/ClairBearmakes/NanoLab-GUI"

# Set serial port and baudrate
# port = 'COM4'  # Replace with your serial port
# baudrate = 9600  # Replace with your Arduino's baudrate (rate of symbol flow)

# Initialize serial connection
arduino = serial.Serial(port="COM4", baudrate=9600, timeout=0.1)

# initiallize app with basic settings
root = Tk() # root is the main window name
root.title("Universal NanoLab Settings")

# getting screen dimentions of display
width= root.winfo_screenwidth()
height= root.winfo_screenheight()

# setting tk window size
root.geometry("%dx%d" % (width, height))
root.eval("tk::PlaceWindow . center")

# create a frame widgets
menu = tk.Frame(root, width=width, height="50", bg=menu_bg_color)
settings_frame = tk.Frame(root, width=width, height=height - int(50), bg=bg_color)
led_settings_frame = tk.Frame(root, width=width, height=height - int(50), bg=bg_color)

# canvas
"""
settingsCanvas = tk.Canvas(root, width = width, 
                 height = height - int(50), bg="blue") 

settingsCanvas.grid(rowspan=3, columnspan=1, row=0, column=0, #fill = "both", expand = True
	)
"""

# place frame widgets in window
menu.grid(row=0, column=0, sticky=tk.E+tk.W)
settings_frame.grid(rowspan=5, columnspan=3, row=1, column=0, sticky="nesw")
# led_settings_frame.grid(rowspan=3, columnspan=3, row=1, column=0, sticky="nesw")

# funtion for about button website
def openweb():
    webbrowser.open(url,new=new)

# function for update button website
def openweb1():
	webbrowser.open(url1,new=new)

def open_files():
    webbrowser.open_new("C:") 

def clear_widgets(root):
	# select all frame widgets and delete them
	for widget in root.winfo_children():
		widget.destroy()

def load_menu(): # button bar on top
	menu.tkraise()
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
		command=open_files # open file explorer
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
	clear_widgets(led_settings_frame)
	# stack settings frame above frame 1
	settings_frame.tkraise()
	# prevent widgets from modifying the frame
	settings_frame.pack_propagate(False)

	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((100, 100))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(settings_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	# create data results button widget
	tk.Button(
		settings_frame,
		text="Data Results",
		font=("Ubuntu", 20),
		height=("2"),
		width=("17"),
		bg=bg_color,
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
		bg=bg_color,
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
		bg=bg_color,
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		command=lambda:load_led_settings_frame(), # LED settings frame
		).grid(row=1, column=3, sticky="w", padx="8", pady="5")

	# create fan settings button widget
	tk.Button(
		settings_frame,
		text="Fan Settings",
		font=("Ubuntu", 20),
		height=("2"),
		width=("17"),
		bg=bg_color,
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
		bg=bg_color,
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
		bg=bg_color,
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		# command=lambda:load_settings_frame(), # load camera settings frame
		).grid(row=2, column=3, sticky="w", padx="8", pady="5")

	# load settings window
	command=lambda:load_settings_frame()
	print("settings loaded")

# slider current value
current_value = tk.DoubleVar()
value_label=0


def get_current_value():
    return '{: .2f}'.format(current_value.get())

# def slider_changed():
    # value_label.configure(text=get_current_value())
    # ser.write(get_current_value()) # relace with send brightness to Arduino
	# arduino.write(str(get_current_value()))  # Convert to bytes

def greenLED():
	l_color="2"
	arduino.write(bytes(l_color))
	# time.sleep(0.05)

def blueLED():
	l_color="3"
	arduino.write(bytes(l_color))
	# time.sleep(0.05)

def redLED():
	l_color="1"
	arduino.write(bytes(l_color))
	# time.sleep(0.05)

def load_led_settings_frame():
	clear_widgets(settings_frame)
	# stack settings frame above frame 1
	led_settings_frame.tkraise()
	# prevent widgets from modifying the frame
	led_settings_frame.pack_propagate(False)

	w1 = Scale(led_settings_frame, from_=0, to=255, orient=HORIZONTAL, variable=current_value)
	# w1.set(23)
	w1.grid(row=2, columnspan=7, column=1)
	Button(led_settings_frame, text='Test').grid(row=3, columnspan=7, column=1) #, command=slider_changed

	# create red color button widget
	tk.Button(
		led_settings_frame,
		text="Red",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=bg_color,
		fg=red_fg,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		# ser.write("rr") # send color to Arduino
		# arduino.write("rr")  # Convert to bytes
    	# time.sleep(0.05)  # Optional delay
    	command=redLED
		).grid(row=0, column=1, sticky="w", padx="5", pady="3")

	# create orange color button widget
	tk.Button(
		led_settings_frame,
		text="Red",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=bg_color,
		fg=orange_fg,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		# command=openweb # send color to Arduino
		).grid(row=0, column=2, sticky="w", padx="5", pady="3")

	# create yellow color button widget
	tk.Button(
		led_settings_frame,
		text="Red",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=bg_color,
		fg=yellow_fg,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		# command=openweb # send color to Arduino
		).grid(row=0, column=3, sticky="w", padx="5", pady="3")

	# create green color button widget
	tk.Button(
		led_settings_frame,
		text="Red",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=bg_color,
		fg=green_fg,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		# ser.write("gg") # send color to Arduino
		# arduino.write("gg")  # Convert to bytes
    	# time.sleep(0.05)  # Optional delay
    	# l_color="gg",
    	command=greenLED
		).grid(row=0, column=4, sticky="w", padx="5", pady="3")

	# create blue color button widget
	tk.Button(
		led_settings_frame,
		text="Red",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=bg_color,
		fg=blue_fg,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		# ser.write("bb") # send color to Arduino
		# arduino.write("bb")  # Convert to bytes
    	# time.sleep(0.05)  # Optional delay
    	# l_color="bb",
    	command=blueLED
		).grid(row=0, column=5, sticky="w", padx="5", pady="3")

	# create purple color button widget
	tk.Button(
		led_settings_frame,
		text="Red",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=bg_color,
		fg=purple_fg,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		# command=openweb # send color to Arduino
		).grid(row=0, column=6, sticky="w", padx="5", pady="3")

	# create violet color button widget
	tk.Button(
		led_settings_frame,
		text="Red",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=bg_color,
		fg=violet_fg,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		# command=openweb # send color to Arduino
		).grid(row=0, column=7, sticky="w", padx="5", pady="3")

	# load led settings window
	led_settings_frame.grid(rowspan=3, columnspan=3, row=1, column=0, sticky="nesw")
	# command=lambda:load_led_settings_frame()
	print("LED settings loaded")


# open serial port
# ser = serial.Serial('COM3')

# check which port was really used
# print(ser.name)

# write a string
# ser.write(b'hello')

# close port
# ser.close()	


"""
# Create object 
root = Tk() 
  
# Adjust size 
root.geometry( "200x200" ) 
  
# Change the label text 
def show(): 
    label.config( text = clicked.get() ) 

# Dropdown menu options 
options = [ 
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday", 
    "Saturday", 
    "Sunday"
] 
  
# datatype of menu text 
clicked = StringVar() 
  
# initial menu text 
clicked.set( "Monday" ) 
  
# Create Dropdown menu 
drop = OptionMenu( root , clicked , *options ) 
drop.pack() 
  
# Create button, it will change label text 
button = Button( root , text = "click Me" , command = show ).pack() 
  
# Create Label 
label = Label( root , text = " " ) 
label.pack() 
  
# Execute tkinter 
root.mainloop() 
>>>>>>> 166714e53ff6049772b27556e12ad84e35987ea2
"""

# load the first frame and button bar
load_menu()
load_settings_frame()

# run app
root.mainloop()