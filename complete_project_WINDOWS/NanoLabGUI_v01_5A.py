
# Code writen by Asher Powell at Warren Tech North
# Version 1.5 Alpha

import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from numpy import random
import pyglet
import webbrowser
import serial
import sys
import time
import random
from tkcalendar import Calendar
from datetime import date 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 

# load custom fonts
pyglet.font.add_file("fonts/Ubuntu-Bold.ttf")
pyglet.font.add_file("fonts/Shanti-Regular.ttf")

# set normal colours
menu_bg_color = "#000000"
menu_fg_color = "#ffffff"
menu_act_bg_color = "#000000"
menu_act_fg_color = "#808080"
bg_color = "#ffffff"
fg_color = "#000000" # normal

# set LED screen colors
led_bg = "#ECECEC"
red_fg = "red"
orange_fg = "orange"
yellow_fg = "yellow"
green_fg = "green"
blue_fg = "blue"
purple_fg = "purple"

act_bg_color = "#ffffff"
act_fg_color = "#808080"

dev_mode = True


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

# creating the date object of today's date 
todays_date = date.today() 
  
# printing todays date 
print("Current date: ", todays_date) 

cur_month = todays_date.month
cur_day = todays_date.day
cur_year = todays_date.year

# lists
w_pump_set = ["50mL", "5d/w"]
LED_set = ["red", "105"]
fan_set = ["90%", "30m/3d/w"]
cam_set = ["1/w"]
atmos_sen_set = ["2/d"]
all_set = [w_pump_set, LED_set, fan_set, cam_set, atmos_sen_set]

# initiallize app with basic settings
root = Tk() # root is the main window name
root.title("Universal NanoLab Settings")
root.configure(bg="white")

# getting screen dimentions of display
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# setting tk window size
root.geometry("%dx%d" % (width, height))
# root.eval("tk::PlaceWindow . center")

# create main frame widgets
menu = tk.Frame(root, width=width, height="45", bg=menu_bg_color)
settings_frame = tk.Frame(root, highlightbackground="grey", highlightthickness=1, width=width, height=height - int(45), bg=bg_color)
data_results_frame = tk.Frame(root, highlightbackground="grey", highlightthickness=1, width=width, height=height - int(45), bg=bg_color)
w_pump_settings_frame = tk.Frame(root, highlightbackground="grey", highlightthickness=1, width=width, height=height - int(45), bg=bg_color)
led_settings_frame = tk.Frame(root, highlightbackground="grey", highlightthickness=1, width=width, height=height - int(45), bg=bg_color)
fan_settings_frame = tk.Frame(root, highlightbackground="grey", highlightthickness=1, width=width, height=height - int(45), bg=bg_color)
camera_settings_frame = tk.Frame(root, highlightbackground="grey", highlightthickness=1, width=width, height=height - int(45), bg=bg_color)
atmos_sensor_frame = tk.Frame(root, highlightbackground="grey", highlightthickness=1, width=width, height=height - int(45), bg=bg_color)

# place main frame widgets in window
menu.grid(row=0, column=0, sticky="nsew")
menu.grid_rowconfigure(0, minsize=35)
settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
data_results_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
w_pump_settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
led_settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
fan_settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
camera_settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
atmos_sensor_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")


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

def show_graph_opt(): 
    print(clicked.get()) 

def get_current_value():
    return '{:.2f}'.format(current_value.get())

def send_settings():
	print(repr(all_set))
	arduino.write(bytes(str(repr(all_set)), 'utf-8'))

def take_picture():
	print("*click*")
	# arduino.write(bytes(str(repr(all_set)), 'utf-8')) #take picture and save it

def take_atmos_reading():
	print("read atmos")
	# arduino.write(bytes(str(repr(all_set)), 'utf-8')) #take atmos reading and save it

def test_pump():
	print("pump")
	# arduino.write(bytes(str(repr(all_set)), 'utf-8')) #pump some water

def clear_widgets(root):
	# select all frame widgets and delete them
	for frame in root.winfo_children():
		frame.destroy()

def load_menu(): # button bar on top
	# clear_widgets()
	menu.tkraise()
	# prevent widgets from modifying the frame
	menu.grid_propagate(False)

	# create back button widget
	tk.Button(
		menu,
		text="Back",
		font=("Ubuntu", 12),
		height=("1"),
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
		height=("1"),
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

	# print("loaded menu")
	
def load_settings_frame():
	# clear_widgets(data_results_frame)
	# clear_widgets(w_pump_settings_frame)
	# clear_widgets(led_settings_frame)
	# clear_widgets(fan_settings_frame)
	# clear_widgets(camera_settings_frame)
	# clear_widgets(atmos_sensor_frame)
	# raise settings frame to the top
	settings_frame.tkraise()
	# prevent widgets from modifying the frame
	settings_frame.grid_propagate(False)

	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(settings_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	settings_title = Label(settings_frame, bg="white", text = "Main Settings", font=("Ubuntu", 30))
	settings_title.grid(row=0, column=2, padx="8", pady="5")

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
		command=send_settings # command to send settings to NanoLab
		).grid(row=4, column=3, columnspan=2, sticky="w", padx="8", pady="5")

	# load settings window
	# command=lambda:load_settings_frame()
	# print("settings loaded")


def load_data_results_frame(): 
	# clear_widgets(settings_frame)
	# raise data results frame to the top
	data_results_frame.tkraise()
	# prevent widgets from modifying the frame
	data_results_frame.grid_propagate(False)


# graph
	def load_plot1(): 

	    # the figure that will contain the plot 
	    fig = Figure(figsize = (6, 4), 
	                dpi = 100) 

	    # list of squares 
	    y = [i**2 for i in range(101)] 

	    # adding the subplot 
	    plot1 = fig.add_subplot(111) 

	    # plotting the graph 
	    plot1.plot(y) 

	    # creating the Tkinter canvas 
	    # containing the Matplotlib figure 
	    canvas = FigureCanvasTkAgg(fig, 
	                            master = data_results_frame) 
	    canvas.draw() 

	    # placing the canvas on the Tkinter window 
	    canvas.get_tk_widget().grid(row=3, columnspan=4, column=1) 

	    # creating the Matplotlib toolbar 
	    # toolbar = NavigationToolbar2Tk(canvas, data_results_frame) 
	    # toolbar.update() 

	    # placing the toolbar on the Tkinter window 
	    # canvas.get_tk_widget().grid(row=2, columnspan=4, column=1)


	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(data_results_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	data_r_title = Label(data_results_frame, bg="white", text = "Data Results", font=("Ubuntu", 30))
	data_r_title.grid(row=0, columnspan=6, column=1, padx="8", pady="5")

	# create update button widget
	tk.Button(
		data_results_frame,
		text="Update",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=bg_color,
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		command = load_plot1(), # update the graph
		).grid(row=1, column=1, sticky="w", padx="5", pady="3")

	# create export button widget
	tk.Button(
		data_results_frame,
		text="Export",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=bg_color,
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		# command=lambda:load_menu() # export the graph
		).grid(row=1, column=1, sticky="e", padx="5", pady="3")

	# Dropdown to choose kind of graph
	# Dropdown menu options 
	options = [ 
	    "Graph", 
	    "Line Graph", 
	    "Bar Graph", 
	] 

	clicked = StringVar()

	# initial menu text 
	clicked.set("Graph")

	# Create Dropdown menu 
	drop = OptionMenu(data_results_frame, clicked, *options) 
	drop.grid(row=1, column=3, sticky="e")

	# Create button, it will print port 
	button = Button(data_results_frame, text = "Choose", font=("Ubuntu", 12), height=("0"), width=("7"), bg=bg_color, fg=fg_color, activebackground=act_bg_color, activeforeground=act_fg_color, command = show_graph_opt)
	button.grid(row=1, column=4, sticky="w")
	
	# load window
	print("data results loaded")

def load_w_pump_settings_frame(): 
	# clear_widgets(settings_frame)
	# raise water pump frame to the top
	w_pump_settings_frame.tkraise()
	# prevent widgets from modifying the frame
	w_pump_settings_frame.grid_propagate(False)

	# set the hardware of the current screen
	hardware = "water pump"

	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(w_pump_settings_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	w_pump_title = Label(w_pump_settings_frame, bg="white", text = "Water Pump Settings", font=("Ubuntu", 30))
	w_pump_title.grid(row=0, columnspan=5, column=1, padx="8", pady="5")

	if dev_mode == True:
		Button(w_pump_settings_frame, text='Test', bg=bg_color,
			fg=fg_color,
			cursor="hand2",
			activebackground=act_bg_color,
			activeforeground=act_fg_color, 
			command=test_pump #pump some water
			).grid(row=1, columnspan=1, column=1, padx="8", pady="5", sticky="w")
		

	# Add start and end calendars
	start_label = Label(w_pump_settings_frame, text = "Start Date:")
	start_label.grid(row=1, column=1, padx="8", pady="5")

	start_cal = Calendar(w_pump_settings_frame, selectmode = 'day',
			year = cur_year, month = cur_month,
			day = cur_day)

	start_cal.grid(row=2, column=1, padx="8", pady="5")

	end_label = Label(w_pump_settings_frame, text = "End Date:")
	end_label.grid(row=1, column=2, padx="8", pady="5")

	end_cal = Calendar(w_pump_settings_frame, selectmode = 'day',
			year = cur_year, month = cur_month,
			day = cur_day)

	end_cal.grid(row=2, column=2, padx="8", pady="5")

	# Add Button and Label
	start_date = start_cal.get_date()
	end_date = end_cal.get_date()
	def grad_date():
		date.config(text = "" + start_cal.get_date() + "-" + end_cal.get_date())

	Button(w_pump_settings_frame, text = "Selected dates are: ", command = grad_date).grid(row=3, columnspan=1, column=1, padx="8", pady="5", sticky="e")

	date = Label(w_pump_settings_frame, text = "")
	date.grid(row=3, columnspan=1, column=2, padx="8", pady="5", sticky="w")


	# frequency stuff
	# declaring string variables for storing frequencys
	fre1_in = tk.StringVar()
	fre2_in = tk.StringVar()
	 
	# defining a function that will get the two frequencys and print them
	def fre_set(): # eventually set to take all values of screen/component and save those

	    fre1 = fre1_in.get()
	    fre2 = fre2_in.get()
	    
	    print(hardware + " will run from: " + start_date + "-" + end_date + " " + fre1 + " times/ " + fre2)
	    
	    fre1_in.set("")
	    
	    
	# creating a label for frequency input using widget Label
	fre_label = tk.Label(w_pump_settings_frame, text = 'Frequency of ' + hardware + ": ", font=('calibre', 10, 'bold'))
	fre_label.grid(row=5, column=1, sticky="w")

	# creating a entry for input
	fre1_entry = tk.Entry(w_pump_settings_frame,textvariable = fre1_in, font=('calibre', 10, 'normal'))
	fre1_entry.grid(row=5, columnspan=2, column=1)

	# creating a dropdown for frequency2
	# Dropdown menu options 
	fre2_options = [ 
	    "hour", 
	    "day", 
	    "week", 
	    "month"
	] 

	# initial menu text 
	fre2_in.set("day")

	# Create Dropdown menu 
	fre2_drop = tk.OptionMenu(w_pump_settings_frame, fre2_in, *fre2_options) 
	fre2_drop.grid(row=5, column=2)
	 
	# creating a button that will call the fre_set function  
	sub_btn=tk.Button(w_pump_settings_frame,text = 'Save', command = fre_set)
	sub_btn.grid(row=5, column=2, padx="7", pady="5", sticky="e")

	# load window
	print("w pump settings loaded")


# LED settings stuff
# slider current value
current_value = tk.DoubleVar()
value_label=0

"""
def get_current_value():
    return '{:.2f}'.format(current_value.get())
"""

def slider_changed():
    # value_label.configure(text=get_current_value())
    # ser.write(get_current_value()) # relace with send brightness to Arduino
	# arduino.write(bytes(get_current_value(), 'utf-8'))  # Convert to bytes
	print('brightness', get_current_value())

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
	# clear_widgets(settings_frame)
	# raise LED settings frame to the top
	led_settings_frame.tkraise()
	# prevent widgets from modifying the frame
	led_settings_frame.grid_propagate(False)

	# set the hardware of the current screen
	hardware = "LED"

	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(led_settings_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	led_settings_title = Label(led_settings_frame, bg="white", text = "LED Settings", font=("Ubuntu", 30))
	led_settings_title.grid(row=0, columnspan=8, column=1, padx="8", pady="5")

	# create red color button widget
	tk.Button(
		led_settings_frame,
		text="Red",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=led_bg,
		fg=red_fg,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
    	command=redLED
		).grid(row=2, column=10, sticky="w", padx="5", pady="3")

	# create orange color button widget
	tk.Button(
		led_settings_frame,
		text="Orange",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=led_bg,
		fg=orange_fg,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		command=orangeLED
		).grid(row=2, column=11, sticky="w", padx="5", pady="3")

	# create yellow color button widget
	tk.Button(
		led_settings_frame,
		text="Yellow",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=led_bg,
		fg=yellow_fg,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		command=yellowLED
		).grid(row=2, column=12, sticky="w", padx="5", pady="3")

	# create green color button widget
	tk.Button(
		led_settings_frame,
		text="Green",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=led_bg,
		fg=green_fg,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
    	command=greenLED
		).grid(row=2, column=13, sticky="w", padx="5", pady="3")

	# create blue color button widget
	tk.Button(
		led_settings_frame,
		text="Blue",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=led_bg,
		fg=blue_fg,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
    	command=blueLED
		).grid(row=2, column=14, sticky="w", padx="5", pady="3")

	# create purple color button widget
	tk.Button(
		led_settings_frame,
		text="Purple",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=led_bg,
		fg=purple_fg,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		command=purpleLED
		).grid(row=2, column=15, sticky="w", padx="5", pady="3")

	# create no color button widget
	tk.Button(
		led_settings_frame,
		text="Clear",
		font=("Ubuntu", 12),
		height=("0"),
		width=("7"),
		bg=led_bg,
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		command=noLED
		).grid(row=2, column=16, sticky="w", padx="5", pady="3")

	# create PARTY color button widget
	tk.Button(
		led_settings_frame,
		text="PARTY",
		font=("Ubuntu", 1),
		height=("0"),
		width=("4"),
		bg=bg_color,
		fg=PARTY_fg,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		command=PARTYLED
		).grid(row=3, columnspan=3, column=11, sticky="n", padx="5", pady="3")

	# label for the slider
	slider_label = ttk.Label(
    	led_settings_frame,
    	text='Dimming Slider',
    	font=("Ubuntu", 12),
	).grid(row=3, columnspan=8, column=10, sticky="n",)

	led_slider = Scale(led_settings_frame, from_=0, to=255, length=570, orient=HORIZONTAL, variable=current_value, bg=bg_color, fg=fg_color)
	led_slider.set(200)
	led_slider.grid(row=3, columnspan=8, column=10, sticky="s",)
	if dev_mode == True:
		Button(led_settings_frame, text='Test', bg=bg_color,
			fg=fg_color,
			cursor="hand2",
			activebackground=act_bg_color,
			activeforeground=act_fg_color, command=slider_changed).grid(row=4, columnspan=8, column=10, sticky="n",)

	# Add start and end calendars
	start_label = Label(led_settings_frame, text = "Start Date:")
	start_label.grid(row=1, columnspan=4, column=1, padx="8", pady="5")

	start_cal = Calendar(led_settings_frame, selectmode = 'day',
			year = cur_year, month = cur_month,
			day = cur_day)

	start_cal.grid(rowspan=4, row=2, columnspan=4, column=1, padx="8", pady="5")

	end_label = Label(led_settings_frame, text = "End Date:")
	end_label.grid(row=1, columnspan=4, column=5, padx="8", pady="5")

	end_cal = Calendar(led_settings_frame, selectmode = 'day',
			year = cur_year, month = cur_month,
			day = cur_day)

	end_cal.grid(rowspan=4, row=2, columnspan=4, column=5, padx="8", pady="5", sticky="e")

	# Add Button and Label
	start_date = start_cal.get_date()
	end_date = end_cal.get_date()
	def grad_date():
		date.config(text = "" + start_cal.get_date() + "-" + end_cal.get_date())

	Button(led_settings_frame, text = "Selected dates are: ", command = grad_date).grid(row=9, columnspan=4, column=1, padx="8", pady="5", sticky="e")

	date = Label(led_settings_frame, text = "")
	date.grid(row=9, columnspan=4, column=5, padx="8", pady="5", sticky="w")

	# """
	# frequency stuff
	# declaring string variables for storing frequencys
	fre1_in = tk.StringVar()
	fre2_in = tk.StringVar()
	 
	# defining a function that will get the two frequencys and print them
	def fre_set(): # eventually set to take all values of screen/component and save those

	    fre1 = fre1_in.get()
	    fre2 = fre2_in.get()
	    
	    print(hardware + " will run from: " + start_date + "-" + end_date + " " + fre1 + " times/ " + fre2)
	    
	    fre1_in.set("")
	    
	    
	# creating a label for frequency input using widget Label
	fre_label = tk.Label(led_settings_frame, text = 'Frequency of ' + hardware + ": ", font=('calibre', 10, 'bold'))
	fre_label.grid(row=10, columnspan=1, column=2, sticky="w")

	# creating a entry for input
	fre1_entry = tk.Entry(led_settings_frame,textvariable = fre1_in, font=('calibre', 10, 'normal'))
	fre1_entry.grid(row=10, columnspan=1, column=4, padx="7", pady="5", sticky="w")

	# creating a dropdown for frequency2
	# Dropdown menu options 
	fre2_options = [ 
	    "hour", 
	    "day", 
	    "week", 
	    "month"
	] 

	# initial menu text 
	fre2_in.set("day")

	# Create Dropdown menu 
	fre2_drop = tk.OptionMenu(led_settings_frame, fre2_in, *fre2_options) 
	fre2_drop.grid(row=10, columnspan=1, column=5, padx="7", pady="5", sticky="w")
	 
	# creating a button that will call the fre_set function  
	sub_btn=tk.Button(led_settings_frame,text = 'Save', command = fre_set)
	sub_btn.grid(row=10, columnspan=1, column=5, padx="7", pady="5", sticky="e")
	# """

	# load window
	print("LED settings loaded")

def load_fan_settings_frame(): 
	# clear_widgets(settings_frame)
	# raise fan settings frame to the top
	fan_settings_frame.tkraise()
	# prevent widgets from modifying the frame
	fan_settings_frame.grid_propagate(False)

	# set the hardware of the current screen
	hardware = "fan"

	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(fan_settings_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	fan_settings_title = Label(fan_settings_frame, bg="white", text = "Fan Settings", font=("Ubuntu", 30))
	fan_settings_title.grid(row=0, columnspan=5, column=1, padx="8", pady="5")

	# slider current value
	current_value = tk.DoubleVar()
	value_label=0

	def get_current_value():
		return '{:.2f}'.format(current_value.get())

	def slider_changed():
	    # value_label = text=get_current_value()
	    # ser.write(get_current_value()) # relace with send brightness to Arduino
		# arduino.write(bytes(get_current_value(), 'utf-8'))  # Convert to bytes
		# return '{:.2f}'.format(current_value.get())
		print('fan strength', str(get_current_value()))

	# label for the slider
	slider_label = ttk.Label(
    	fan_settings_frame,
    	text='Fan Strength',
    	font=("Ubuntu", 12)
	).grid(row=1, columnspan=3, column=1)

	fan_strength_slider = Scale(fan_settings_frame, from_=0, to=100, length=250, orient=HORIZONTAL, variable=current_value, bg=bg_color, fg=fg_color)
	fan_strength_slider.set(70)
	fan_strength_slider.grid(row=2, columnspan=8, column=1)

	if dev_mode == True:
		Button(fan_settings_frame, text='Test', bg=bg_color,
			fg=fg_color,
			cursor="hand2",
			activebackground=act_bg_color,
			activeforeground=act_fg_color, 
			command=slider_changed
			).grid(row=1, columnspan=3, column=1, padx="8", pady="5", sticky="w")

	# Add start and end calendars
	start_label = Label(fan_settings_frame, text = "Start Date:")
	start_label.grid(row=3, column=1, padx="8", pady="5")

	start_cal = Calendar(fan_settings_frame, selectmode = 'day',
			year = cur_year, month = cur_month,
			day = cur_day)

	start_cal.grid(row=4, column=1, padx="8", pady="5")

	end_label = Label(fan_settings_frame, text = "End Date:")
	end_label.grid(row=3, column=2, padx="8", pady="5")

	end_cal = Calendar(fan_settings_frame, selectmode = 'day',
			year = cur_year, month = cur_month,
			day = cur_day)

	end_cal.grid(row=4, column=2, padx="8", pady="5")

	# Add Button and Label
	start_date = start_cal.get_date()
	end_date = end_cal.get_date()
	def grad_date():
		date.config(text = "" + start_cal.get_date() + "-" + end_cal.get_date())

	Button(fan_settings_frame, text = "Selected dates are: ", command = grad_date).grid(row=5, columnspan=1, column=1, padx="8", pady="5", sticky="e")

	date = Label(fan_settings_frame, text = "")
	date.grid(row=5, columnspan=1, column=2, padx="8", pady="5", sticky="w")


	# frequency stuff
	# declaring string variables for storing frequencys
	fre1_in = tk.StringVar()
	fre2_in = tk.StringVar()
	 
	# defining a function that will get the two frequencys and print them
	def fre_set(): # eventually set to take all values of screen/component and save those

	    fre1 = fre1_in.get()
	    fre2 = fre2_in.get()
	    
	    print(hardware + " will run from: " + start_date + "-" + end_date + " " + fre1 + " times/ " + fre2)
	    
	    fre1_in.set("")
	    
	    
	# creating a label for frequency input using widget Label
	fre_label = tk.Label(fan_settings_frame, text = 'Frequency of ' + hardware + ": ", font=('calibre', 10, 'bold'))
	fre_label.grid(row=6, column=1, sticky="w")

	# creating a entry for input
	fre1_entry = tk.Entry(fan_settings_frame,textvariable = fre1_in, font=('calibre', 10, 'normal'))
	fre1_entry.grid(row=6, columnspan=2, column=1)

	# creating a dropdown for frequency2
	# Dropdown menu options 
	fre2_options = [ 
	    "hour", 
	    "day", 
	    "week", 
	    "month"
	] 

	# initial menu text 
	fre2_in.set("day")

	# Create Dropdown menu 
	fre2_drop = tk.OptionMenu(fan_settings_frame, fre2_in, *fre2_options) 
	fre2_drop.grid(row=6, column=2)
	 
	# creating a button that will call the fre_set function  
	sub_btn=tk.Button(fan_settings_frame,text = 'Save', command = fre_set)
	sub_btn.grid(row=6, column=2, padx="7", pady="5", sticky="e")

	# load window
	print("fan settings loaded")

def load_camera_settings_frame(): 
	# clear_widgets(settings_frame)
	# raise camera settings frame to the top
	camera_settings_frame.tkraise()
	# prevent widgets from modifying the frame
	camera_settings_frame.grid_propagate(False)

	# set the hardware of the current screen
	hardware = "camera"

	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(camera_settings_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	cam_settings_title = Label(camera_settings_frame, bg="white", text = "Camera Settings", font=("Ubuntu", 30))
	cam_settings_title.grid(row=0, columnspan=5, column=1, padx="8", pady="5")
	
	if dev_mode == True:
		Button(camera_settings_frame, text='Test', bg=bg_color,
			fg=fg_color,
			cursor="hand2",
			activebackground=act_bg_color,
			activeforeground=act_fg_color, 
			command=take_picture
			).grid(row=2, columnspan=1, column=1, padx="8", pady="5", sticky="w")

	# Add start and end calendars
	start_label = Label(camera_settings_frame, text = "Start Date:")
	start_label.grid(row=2, column=1, padx="8", pady="5")

	start_cal = Calendar(camera_settings_frame, selectmode = 'day',
			year = cur_year, month = cur_month,
			day = cur_day)

	start_cal.grid(row=3, column=1, padx="8", pady="5")

	end_label = Label(camera_settings_frame, text = "End Date:")
	end_label.grid(row=2, column=2, padx="8", pady="5")

	end_cal = Calendar(camera_settings_frame, selectmode = 'day',
			year = cur_year, month = cur_month,
			day = cur_day)

	end_cal.grid(row=3, column=2, padx="8", pady="5")

	# Add Button and Label
	start_date = start_cal.get_date()
	end_date = end_cal.get_date()
	def grad_date():
		date.config(text = "" + start_cal.get_date() + "-" + end_cal.get_date())

	Button(camera_settings_frame, text = "Selected dates are: ", command = grad_date).grid(row=4, columnspan=1, column=1, padx="8", pady="5", sticky="e")

	date = Label(camera_settings_frame, text = "")
	date.grid(row=4, columnspan=1, column=2, padx="8", pady="5", sticky="w")


	# frequency stuff
	# declaring string variables for storing frequencys
	fre1_in = tk.StringVar()
	fre2_in = tk.StringVar()
	 
	# defining a function that will get the two frequencys and print them
	def fre_set(): # eventually set to take all values of screen/component and save those

	    fre1 = fre1_in.get()
	    fre2 = fre2_in.get()
	    
	    print(hardware + " will run from: " + start_date + "-" + end_date + " " + fre1 + " times/ " + fre2)
	    
	    fre1_in.set("")
	    
	    
	# creating a label for frequency input using widget Label
	fre_label = tk.Label(camera_settings_frame, text = 'Frequency of ' + hardware + ": ", font=('calibre', 10, 'bold'))
	fre_label.grid(row=5, column=1, sticky="w")

	# creating a entry for input
	fre1_entry = tk.Entry(camera_settings_frame,textvariable = fre1_in, font=('calibre', 10, 'normal'))
	fre1_entry.grid(row=5, columnspan=2, column=1)

	# creating a dropdown for frequency2
	# Dropdown menu options 
	fre2_options = [ 
	    "hour", 
	    "day", 
	    "week", 
	    "month"
	] 

	# initial menu text 
	fre2_in.set("day")

	# Create Dropdown menu 
	fre2_drop = tk.OptionMenu(camera_settings_frame, fre2_in, *fre2_options) 
	fre2_drop.grid(row=5, column=2)
	 
	# creating a button that will call the fre_set function  
	sub_btn=tk.Button(camera_settings_frame,text = 'Save', command = fre_set)
	sub_btn.grid(row=5, column=2, padx="7", pady="5", sticky="e")

	# load window
	print("camera settings loaded")

def load_atmos_sensor_frame(): 
	# clear_widgets(settings_frame)
	# raise atmospheric sensor frame to the top
	atmos_sensor_frame.tkraise()
	# prevent widgets from modifying the frame
	atmos_sensor_frame.grid_propagate(False)

	# set the hardware of the current screen
	hardware = "atmospheric sensor"

	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(atmos_sensor_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	atmos_sensor_title = Label(atmos_sensor_frame, bg="white", text = "Atmospheric Sensor Settings", font=("Ubuntu", 30))
	atmos_sensor_title.grid(row=0, columnspan=5, column=1, padx="8", pady="5")

	if dev_mode == True:
		Button(atmos_sensor_frame, text='Test', bg=bg_color,
			fg=fg_color,
			cursor="hand2",
			activebackground=act_bg_color,
			activeforeground=act_fg_color, 
			command=take_atmos_reading
			).grid(row=2, columnspan=1, column=1, padx="8", pady="5", sticky="w")

	# Add start and end calendars
	start_label = Label(atmos_sensor_frame, text = "Start Date:")
	start_label.grid(row=2, columnspan=2, column=1, padx="8", pady="5")

	start_cal = Calendar(atmos_sensor_frame, selectmode = 'day',
			year = cur_year, month = cur_month,
			day = cur_day)
	start_cal.grid(row=3, columnspan=2, column=1, padx="8", pady="5", sticky="w")

	end_label = Label(atmos_sensor_frame, text = "End Date:")
	end_label.grid(row=2, columnspan=2, column=3, padx="8", pady="5")

	end_cal = Calendar(atmos_sensor_frame, selectmode = 'day',
			year = cur_year, month = cur_month,
			day = cur_day)
	end_cal.grid(row=3, columnspan=2, column=3, padx="8", pady="5", sticky="w")

	# Add Button and Label
	start_date = ""
	end_date = ""
	def grad_date():
		date.config(text = "" + start_cal.get_date() + "-" + end_cal.get_date())
		# start_date = start_cal.get_date()
		# end_date = end_cal.get_date()
		print('next_date="{}"'.format(end_cal.selection_get()))

	Button(atmos_sensor_frame, text = "Selected dates are: ", command = grad_date).grid(row=4, columnspan=2, column=1, padx="8", pady="5", sticky="e")

	date = Label(atmos_sensor_frame, text = "")
	date.grid(row=4, columnspan=2, column=3, padx="8", pady="5", sticky="w")


	# frequency stuff
	# declaring string variables for storing frequencys
	fre1_in = tk.StringVar()
	fre2_in = tk.StringVar()
	 
	# defining a function that will get the two frequencys and print them
	def fre_set(): # eventually set to take all values of screen/component and save those

	    fre1 = fre1_in.get()
	    fre2 = fre2_in.get()
	    
	    print(hardware + " will run from: " + start_date + "-" + end_date + " " + fre1 + " times/ " + fre2)
	    
	    fre1_in.set("")
	    
	    
	# creating a label for frequency input using widget Label
	fre_label = tk.Label(atmos_sensor_frame, text = 'Frequency of ' + hardware + ": ", font=('calibre', 10, 'bold'))
	fre_label.grid(row=5, column=1, sticky="w")

	# creating a entry for input
	fre1_entry = tk.Entry(atmos_sensor_frame,textvariable = fre1_in, font=('calibre', 10, 'normal'))
	fre1_entry.grid(row=5, columnspan=1, column=2, padx="7", pady="5", sticky="w")

	# creating a dropdown for frequency2
	# Dropdown menu options 
	fre2_options = [ 
	    "hour", 
	    "day", 
	    "week", 
	    "month"
	] 

	# initial menu text 
	fre2_in.set("day")

	# Create Dropdown menu 
	fre2_drop = tk.OptionMenu(atmos_sensor_frame, fre2_in, *fre2_options) 
	fre2_drop.grid(row=5, columnspan=3, column=2, padx="7", pady="5", sticky="")
	 
	# creating a button that will call the fre_set function  
	sub_btn=tk.Button(atmos_sensor_frame,text = 'Save', command = fre_set)
	sub_btn.grid(row=5, columnspan=2, column=3, padx="7", pady="5", sticky="")

	# load window
	print("atmos sensor frame loaded")

# load the first frame and button bar
load_menu()
load_settings_frame()

# run app
root.mainloop()