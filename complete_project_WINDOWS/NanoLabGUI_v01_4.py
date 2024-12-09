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
import time
import random

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

act_bg_color = "#ffffff"
act_fg_color = "#808080"

# load custom fonts
pyglet.font.add_file("fonts/Ubuntu-Bold.ttf")
pyglet.font.add_file("fonts/Shanti-Regular.ttf")

"""
# =======================
# setup window stuff

# Create object
setup_root = tk.Tk()

# Adjust size
setup_root.geometry("500x500")

setup_root.tkraise()

def setup():
	# Create object
	# setup_root = Tk()

	# Adjust size
	# setup_root.geometry("500x500")

	# setup_root.tkraise()

	# create setup frame widgets
	home_frame = tk.Frame(setup_root, width="500", height="500", bg=bg_color)

	# place setup frame widgets into window
	home_frame.grid(rowspan=4, columnspan=4, row=1, column=0, sticky="nesw")

	# Set Label
	welcome_label = Label(home_frame, text="Welcome to your NanoLab", font=18)
	welcome_label.grid()

	# setup_root.after(8000, setup_root.destroy)

setup()

# setup_root.destroy
"""

# =======================
# main window stuff

# set about website
new = 1
url = "https://sites.google.com/jeffcoschools.us/universal-nanolab/project-home-page"
url1 = "https://github.com/ClairBearmakes/NanoLab-GUI"

# initiallize app with basic settings
root = Tk() # root is the main window name
root.title("Universal NanoLab Settings")

# getting screen dimentions of display
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# setting tk window size
root.geometry("%dx%d" % (width, height))
# root.eval("tk::PlaceWindow . center")

# create main frame widgets
menu = tk.Frame(root, highlightbackground="black", highlightthickness=1, width=width, height="50", bg=menu_bg_color)
settings_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1, width=width, height=height - int(50), bg=bg_color)
data_results_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1, width=width, height=height - int(50), bg=bg_color)
w_pump_settings_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1, width=width, height=height - int(50), bg=bg_color)
led_settings_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1, width=width, height=height - int(50), bg=bg_color)
fan_settings_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1, width=width, height=height - int(50), bg=bg_color)
camera_settings_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1, width=width, height=height - int(50), bg=bg_color)
atmos_sensor_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1, width=width, height=height - int(50), bg=bg_color)

# place main frame widgets in window
menu.grid(row=0, column=0, sticky=tk.E+tk.W)
settings_frame.grid(rowspan=4, columnspan=4, row=1, column=0, sticky="nesw")
data_results_frame.grid(rowspan=2, columnspan=1, row=1, column=0, sticky="nesw")
w_pump_settings_frame.grid(rowspan=4, columnspan=5, row=1, column=0, sticky="nesw")
led_settings_frame.grid(rowspan=4, columnspan=5, row=1, column=0, sticky="nesw")
fan_settings_frame.grid(rowspan=4, columnspan=5, row=1, column=0, sticky="nesw")
camera_settings_frame.grid(rowspan=4, columnspan=5, row=1, column=0, sticky="nesw")
atmos_sensor_frame.grid(rowspan=4, columnspan=5, row=1, column=0, sticky="nesw")


# Initialize serial connection
# arduino = serial.Serial(port="COM4", baudrate=9600, timeout=0.1)

# check which port was really used
# print(arduino.name)

# funtion for about button website
def openweb():
    webbrowser.open(url,new=new)

# function for update button website
def openweb1():
	webbrowser.open(url1,new=new)

def open_files():
    webbrowser.open_new("C:") # replace with NanoLab's internal storage

def clear_widgets(root):
	# select all frame widgets and delete them
	for widget in root.winfo_children():
		widget.destroy()

def load_menu(): # button bar on top
	# clear_widgets()
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
	resize_image = image.resize((125, 125))
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
		command=lambda:load_data_results_frame(), # data results frame
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
		command=lambda:load_w_pump_settings_frame(), # water pump settings frame
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
		command=lambda:load_fan_settings_frame(), # fan settings frame
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
		command=lambda:load_camera_settings_frame(), # camera settings frame
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
		command=lambda:load_atmos_sensor_frame(), # atmos sensor frame
		).grid(row=2, column=3, sticky="w", padx="8", pady="5")

	# create send to arduino button widget
	tk.Button(
		settings_frame,
		text="Send settings to your NanoLab",
		font=("Ubuntu", 20),
		height=("0"),
		width=("25"),
		bg=bg_color,
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		# command=lambda:load_atmos_sensor_frame(), # command to send settings to NanoLab
		).grid(row=4, column=3, columnspan=2, sticky="w", padx="8", pady="5")

	# load settings window
	command=lambda:load_settings_frame()
	print("settings loaded")


def load_data_results_frame(): 
	clear_widgets(settings_frame)
	# stack settings frame above frame 1
	data_results_frame.tkraise()
	# prevent widgets from modifying the frame
	data_results_frame.pack_propagate(False)

	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(data_results_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	# load settings window
	print("data results loaded")

def load_w_pump_settings_frame(): 
	clear_widgets(settings_frame)
	# stack settings frame above frame 1
	w_pump_settings_frame.tkraise()
	# prevent widgets from modifying the frame
	w_pump_settings_frame.pack_propagate(False)

	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(w_pump_settings_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	# load settings window
	print("w pump settings loaded")


# LED settings stuff

# slider current value
current_value = tk.DoubleVar()
value_label=0


def get_current_value():
    return '{:.2f}'.format(current_value.get())

def slider_changed():
    # value_label.configure(text=get_current_value())
    # ser.write(get_current_value()) # relace with send brightness to Arduino
	# arduino.write(bytes(get_current_value(), 'utf-8'))  # Convert to bytes
	print(get_current_value(), 'lol')

LED_color = "RR"

def redLED():
	arduino.write(bytes('RR', str(get_current_value()), 'utf-8'))
	time.sleep(0.05)

def orangeLED():
	arduino.write(bytes('OO', str(get_current_value()), 'utf-8'))
	time.sleep(0.05)

def yellowLED():
	arduino.write(bytes('YY', str(get_current_value()), 'utf-8'))
	time.sleep(0.05)

def greenLED():
	arduino.write(bytes('GG', str(get_current_value()), 'utf-8'))
	time.sleep(0.05)

def blueLED():
	arduino.write(bytes('BB', str(get_current_value()), 'utf-8'))
	time.sleep(0.05)

def purpleLED():
	arduino.write(bytes('PP', str(get_current_value()), 'utf-8'))
	time.sleep(0.05)

# randomize color of PARTY button
PARTY_list = ["red", "orange", "yellow", "green", "blue", "purple"]
count = 0
counter = random.random()
while (count < counter):
	for x in PARTY_list:
  		PARTY_fg = x
  		# print(x)
  		time.sleep(0.05)
	if count <= counter:
  		break


def PARTYLED():
	arduino.write(bytes("ROYGBPROYGBPROYGBPROYGBP", 'utf-8'))

def noLED():
	arduino.write(bytes('CC', 'utf-8'))

def load_led_settings_frame():
	clear_widgets(settings_frame)
	# stack settings frame above frame 1
	led_settings_frame.tkraise()
	# prevent widgets from modifying the frame
	led_settings_frame.pack_propagate(False)

	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(led_settings_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

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
    	command=redLED
		).grid(row=1, column=1, sticky="w", padx="5", pady="3")

	# create orange color button widget
	tk.Button(
		led_settings_frame,
		text="Orange",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=bg_color,
		fg=orange_fg,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		command=orangeLED
		).grid(row=1, column=2, sticky="w", padx="5", pady="3")

	# create yellow color button widget
	tk.Button(
		led_settings_frame,
		text="Yellow",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=bg_color,
		fg=yellow_fg,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		command=yellowLED
		).grid(row=1, column=3, sticky="w", padx="5", pady="3")

	# create green color button widget
	tk.Button(
		led_settings_frame,
		text="Green",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=bg_color,
		fg=green_fg,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
    	command=greenLED
		).grid(row=1, column=4, sticky="w", padx="5", pady="3")

	# create blue color button widget
	tk.Button(
		led_settings_frame,
		text="Blue",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=bg_color,
		fg=blue_fg,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
    	command=blueLED
		).grid(row=1, column=5, sticky="w", padx="5", pady="3")

	# create purple color button widget
	tk.Button(
		led_settings_frame,
		text="Purple",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=bg_color,
		fg=purple_fg,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		command=purpleLED
		).grid(row=1, column=6, sticky="w", padx="5", pady="3")

	# create no color button widget
	tk.Button(
		led_settings_frame,
		text="Clear",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=bg_color,
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		command=noLED
		).grid(row=1, column=7, sticky="w", padx="5", pady="3")

	# label for the slider
	slider_label = ttk.Label(
    	led_settings_frame,
    	text='Dimming Slider',
	).grid(row=3, columnspan=7, column=1)

	w1 = Scale(led_settings_frame, from_=0, to=255, length=300, orient=HORIZONTAL, variable=current_value, bg=bg_color, fg=fg_color)
	w1.set(200)
	w1.grid(row=4, columnspan=7, column=1)
	Button(led_settings_frame, text='Test', bg=bg_color,
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color, command=slider_changed).grid(row=5, columnspan=7, column=1)

	# create PARTY color button widget
	tk.Button(
		led_settings_frame,
		text="PARTY",
		font=("Ubuntu", 3),
		height=("0"),
		width=("7"),
		bg=bg_color,
		fg=PARTY_fg,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		command=PARTYLED
		).grid(row=3, columnspan=2, column=5, sticky="w", padx="5", pady="3")


def load_fan_settings_frame(): 
	clear_widgets(settings_frame)
	# stack settings frame above frame 1
	fan_settings_frame.tkraise()
	# prevent widgets from modifying the frame
	fan_settings_frame.pack_propagate(False)

	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(fan_settings_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	# load settings window
	print("fan settings loaded")

def load_camera_settings_frame(): 
	clear_widgets(settings_frame)
	# stack settings frame above frame 1
	camera_settings_frame.tkraise()
	# prevent widgets from modifying the frame
	camera_settings_frame.pack_propagate(False)

	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(camera_settings_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	# load settings window
	print("camera settings loaded")

def load_atmos_sensor_frame(): 
	clear_widgets(atmos_sensor_frame)
	# stack settings frame above frame 1
	atmos_sensor_frame.tkraise()
	# prevent widgets from modifying the frame
	atmos_sensor_frame.pack_propagate(False)

	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(atmos_sensor_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	# load settings window
	print("atmos sensor frame loaded")

# load the first frame and button bar
load_menu()
load_settings_frame()

# run app
root.mainloop()