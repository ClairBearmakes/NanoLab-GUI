
# Code writen by Asher Powell at Warren Tech North
# Version 1.6a

# import dependencies
import tkinter as tk
from tkinter import *
from tkinter import colorchooser
from PIL import Image, ImageTk
from numpy import random
import pyglet
import webbrowser
import serial
import sys
import time
import random
from tkcalendar import Calendar
import datetime
from datetime import date 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import array 

# set fonts
pyglet.font.add_file("fonts/Ubuntu-Bold.ttf")
normal_font= ("Ubuntu", 12)
big_font= ("Ubuntu", 24)
title_font= ("Ubuntu", 46)
calender_font= ("Arial", 10)

"""
# Arduino Stuff
# open serial port
arduino = serial.Serial(port="COM4", baudrate=9600, timeout=0.1)
# check which port was really used
print(arduino.name)

# close serial port from https://stackoverflow.com/questions/35235436/python-arduino-prototyping-api-v2-closing-serial-port
def closeport(): #Closes port if currently open
    ser = serial.Serial(usbport) 
    if ser.isOpen() == True:
        ser.close()

# closeport() #make sure port is available
"""

# set starting variables
dev_mode = True # if True will show log button and test buttons
beta = True # enable beta testing form button
dark_mode = False
comp_count = 5 # number of components
type_selected = False
box_type = ""

if dark_mode == False: # fix these
	# set normal colors
	menu_bg_color = "#000000"
	menu_fg_color = "#ffffff"
	menu_act_bg_color = "#000000"
	bg_color = "#ffffff"
	fg_color = "#000000"
	act_bg_color = "#ffffff"
	act_fg_color = "#808080"
else:
	# set dark mode colors
	menu_bg_color = "#ffffff"
	menu_fg_color = "#000000"
	menu_act_bg_color = "#ffffff"
	bg_color = "#000000"
	fg_color = "#ffffff"
	act_bg_color = "#808080"
	act_fg_color = "#ffffff"


#"""
# =======================
# setup window stuff

# create object
setup_root = tk.Tk()
setup_root.title("Universal NanoLab Setup")
setup_root.configure(bg=bg_color)

# set logo
setup_root.iconbitmap("assets/Universal logo.ico")
# small_icon = tk.PhotoImage(file="assets/NanoLabs_logo.png") #16
# large_icon = tk.PhotoImage(file="assets/NanoLabs_logo.png") #32
# setup_root.iconphoto(False, large_icon, small_icon)

# adjust size
setup_root.geometry("600x550") # width by height 
su_width = 600
su_height = 550

setup_root.tkraise()

# create setup frames
setup1_frame = tk.Frame(setup_root, highlightbackground="grey", highlightthickness=1, width=su_width, height=su_height, bg=bg_color)
setup2_frame = tk.Frame(setup_root, highlightbackground="grey", highlightthickness=1, width=su_width, height=su_height, bg=bg_color)

# place frames into setup window
setup1_frame.grid(rowspan=4, columnspan=10, row=0, column=0, sticky="nesw")
setup2_frame.grid(rowspan=4, columnspan=10, row=0, column=0, sticky="nesw")

def type_hydro():
	box_type = "HydroFuge"
	print(box_type + " selected")
	type_selected = True

def type_uni():
	box_type = "Universal"
	print(box_type + " selected")
	type_selected = True

"""
def goto_main():
	if selected == True:
		setup_root.destroy
"""

def load_setup1():
	setup1_frame.tkraise()
	# prevent widgets from modifying the frame
	setup1_frame.grid_propagate(False)

	# Set Label
	welcome_label = Label(setup1_frame, text="Welcome to your NanoLab!", font=("Ubuntu-Bold", 20), bg=bg_color)
	welcome_label.grid(row=0, columnspan=8, column=0, sticky="")

	welcome_label = Label(setup1_frame, text="Pick Your Version", font=("Ubuntu-Bold", 18), bg=bg_color)
	welcome_label.grid(row=1, columnspan=8, column=0, sticky="")


	# add image button of HydroFuge and "coming soon" for Universal

	# HydroFuge
	# Read the Image
	image = Image.open("assets/Universal NanoLab.png")
	# Resize the image using resize() method
	resize_image = image.resize((270, 320))
	logo_img = ImageTk.PhotoImage(resize_image)
	hydro_logo_widget = tk.Button(setup1_frame, image=logo_img, bg=bg_color, highlightcolor="gray", command=type_hydro)
	hydro_logo_widget.image = logo_img
	hydro_logo_widget.grid(row=2, columnspan=3, column=1, sticky="", padx="8", pady="5")

	# add HydroFuge label under button
	hydrofuge_label = Label(setup1_frame, text="HydroFuge", font=normal_font, bg=bg_color)
	hydrofuge_label.grid(row=3, columnspan=3, column=1, sticky="", padx="5", pady="3")

	# Universal
	# Read the Image
	image = Image.open("assets/Coming Soon.png")
	# Resize the image using resize() method
	resize_image = image.resize((270, 320))
	logo_img = ImageTk.PhotoImage(resize_image)
	uni_logo_widget = tk.Button(setup1_frame, image=logo_img, bg=bg_color, state='disabled', command=type_uni)
	uni_logo_widget.image = logo_img
	uni_logo_widget.grid(row=2, columnspan=3, column=4, sticky="", padx="8", pady="5")

	# add Universal label under button
	hydrofuge_label = Label(setup1_frame, text="Universal (Coming Soon)", font=normal_font, bg=bg_color)
	hydrofuge_label.grid(row=3, columnspan=3, column=4, sticky="", padx="5", pady="3")

	# Finish setup or go to next frame
	tk.Button(
		setup1_frame,
		text="Done", # Next
		font=normal_font,
		height=("1"),
		width=("7"),
		bg=bg_color,
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		command=setup_root.destroy # lambda:load_setup2()
		).grid(row=4, columnspan=2, column=3, sticky="", padx="5", pady="3")

	# print("first screen loaded")

"""
def load_setup2():
	setup2_frame.tkraise()
	# prevent widgets from modifying the frame
	setup2_frame.grid_propagate(False)

	# Set Label
	welcome2_label = Label(setup2_frame, text="Pick Your Version", font=("Ubuntu", 20), bg=bg_color)
	welcome2_label.grid(row=0, columnspan=4, column=3, sticky="")

	# go back a frame
	tk.Button(
		setup2_frame,
		text="Back",
		font=normal_font,
		height=("1"),
		width=("7"),
		bg=bg_color,
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		command=lambda:load_setup1()
		).grid(row=5, column=5, sticky="", padx="5", pady="3")

	# finish setup
	tk.Button(
		setup2_frame,
		text="Done",
		font=normal_font,
		height=("1"),
		width=("7"),
		bg=bg_color,
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		command=setup_root.destroy
		).grid(row=5, column=6, sticky="", padx="5", pady="3")

	# print("second screen loaded")
"""

# run setup screen
load_setup1()
setup_root.mainloop()

# setup end
# =======================
#"""


# =======================
# main window stuff
# =======================

# creating the date object of today's date 
todays_date = date.today() 
  
# printing todays date 
print("Current date: ", todays_date) 

cur_month = todays_date.month
cur_day = todays_date.day
cur_year = todays_date.year

# lists # move to respective places
w_pump_set = [] #"50mL", "5d/w"
LED_set = [] #"red", "105"
fan_set = [] #"90%", "30m/3d/w"
cam_set = [] #"1/w"
atmos_sen_set = [] #"2/d"
all_set = f"{w_pump_set = } {LED_set = } {fan_set = } {cam_set = } {atmos_sen_set = }"

with open("data/variablesfile.txt", 'w') as f:
	f.write(all_set + '\n')
	#f.write(str(all_set1))

# initiallize app with basic settings
root = Tk() # root is the main window name
root.title("Universal NanoLab Settings")
root.configure(bg="white")
# set logo
root.iconbitmap("assets/Universal logo.ico")
# small_icon = tk.PhotoImage(file="assets/NanoLabs_logo.png") #16
# large_icon = tk.PhotoImage(file="assets/NanoLabs_logo.png") #32
# root.iconphoto(True, large_icon, small_icon)

# getting screen dimentions of display
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# setting tk window size
root.geometry("%dx%d" % (width, height))
# root.eval("tk::PlaceWindow . center")

menu_height = 55

# create main frame widgets
menu = tk.Frame(root, width=width, height=menu_height, bg=menu_bg_color)
settings_frame = tk.Frame(root, highlightbackground="grey", highlightthickness=1, width=width, height=height - menu_height, bg=bg_color)
w_pump_settings_frame = tk.Frame(root, highlightbackground="grey", highlightthickness=1, width=width, height=height - menu_height, bg=bg_color)
led_settings_frame = tk.Frame(root, highlightbackground="grey", highlightthickness=1, width=width, height=height - menu_height, bg=bg_color)
fan_settings_frame = tk.Frame(root, highlightbackground="grey", highlightthickness=1, width=width, height=height - menu_height, bg=bg_color)
camera_settings_frame = tk.Frame(root, highlightbackground="grey", highlightthickness=1, width=width, height=height - menu_height, bg=bg_color)
atmos_sensor_frame = tk.Frame(root, highlightbackground="grey", highlightthickness=1, width=width, height=height - menu_height, bg=bg_color)
set_preview_frame = tk.Frame(root, highlightbackground="grey", highlightthickness=1, width=width, height=height - menu_height, bg=bg_color)
data_results_frame = tk.Frame(root, highlightbackground="grey", highlightthickness=1, width=width, height=height - menu_height, bg=bg_color)
log_frame = tk.Frame(root, highlightbackground="grey", highlightthickness=1, width=width, height=height - menu_height, bg=bg_color)
error_404_frame = tk.Frame(root, highlightbackground="red", highlightthickness=1, width=width, height=height, bg="grey")

# place main frame widgets in window
menu.grid(row=0, column=0, sticky="nsew")
menu.grid_rowconfigure(0, minsize=35)
# settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
# error_404_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")

# set websites
nano_site = "https://sites.google.com/jeffcoschools.us/universal-nanolab/project-home-page"
github = "https://github.com/ClairBearmakes/NanoLab-GUI"
betaform = "https://docs.google.com/forms/d/e/1FAIpQLScn_A1m8JzfphVgT83yOyETZGsvzdgrhsZ03veFijbZWohrrg/viewform"

# set classes
# buttons for main settings screen
class MyButton: # text, font, height, width, row, column, columnspan, sticky, command
	# class variables (attributes)
	master = settings_frame # change with MyButton.master = whatever_frame

	def __init__(self, btntext, font, btnheight, btnwidth, rownum, columnnum, colspan, stickdir, command):	
		self.btntext = btntext
		self.font = font
		self.btnheight = btnheight
		self.btnwidth = btnwidth
		self.command = command
		self.btn = tk.Button(self.master, 
		text=self.btntext, font=font,
		height = btnheight,  width = btnwidth,
		bg = bg_color, fg = fg_color,
		activebackground = act_bg_color, activeforeground = act_fg_color,
		cursor = "hand2", command=self.command)
		self.btn.config(padx=0, pady=0)
		self.rownum = rownum
		self.columnnum = columnnum
		self.colspan = colspan
		self.stickdir = stickdir
		self.btn.grid(row=self.rownum, column=self.columnnum, columnspan=self.colspan, padx="8", pady="5", sticky=stickdir)

	# def on_change(self):
		# print(f"Record {self.checktext} = {self.checkbox_value.get()}") 

# test buttons
class TestButton: # master, rownum, columnnum, colspan, stickdir, command
	# class variables (attributes)

	def __init__(self, master, rownum, columnnum, colspan, stickdir, command):
		self.master = master
		self.rownum = rownum
		self.columnnum = columnnum
		self.colspan = colspan
		self.stickdir = stickdir
		self.command = command

		self.btn = tk.Button(self.master, text='Test', 
			bg=bg_color, fg=fg_color,
			activebackground=act_bg_color, activeforeground=act_fg_color,
			font=normal_font,
			cursor="hand2",  
			command=self.command)
		self.btn.grid(row=self.rownum, column=self.columnnum, columnspan=self.colspan, padx="8", pady="5", sticky=stickdir)

	# def on_change(self):
		# print(f"Record {self.checktext} = {self.checkbox_value.get()}") 


# set functions
# functions for website buttons
def opennanosite():
    webbrowser.open_new(nano_site)

def opengithub():
	webbrowser.open_new(github)

def openbetaform():
	webbrowser.open_new(betaform)

def open_files():
    webbrowser.open_new("C:") # replace with txt file with list of sd cards files

# test functions
def take_picture():
	print("*click*")
	# arduino.write(bytes(str(repr(all_set)), 'utf-8')) # take picture and save it

def take_atmos_reading():
	print("read atmos")
	# arduino.write(bytes(str(repr(all_set)), 'utf-8')) # take atmos reading and save it

def test_pump():
	print("pump")
	# arduino.write(bytes(str(repr(all_set)), 'utf-8')) # pump some water and shake leaves

def test_fan():
	print("fan running")
	# arduino.write(bytes(str(repr(all_set)), 'utf-8')) # turn on the fan for a little bit

# LED test = test_LED()

def send_settings():
	print(repr(all_set))
	# arduino.write(bytes(str(repr(all_set)), 'utf-8'))
	# something to check Arduino got it
	print("experiment started")

def clear_widgets(root):
	# select all frame widgets and delete them
	for frame in root.winfo_children():
		frame.destroy()

# defining button bar on top
def load_menu(): 
	# clear_widgets()
	menu.tkraise()
	# prevent widgets from modifying the frame
	menu.grid_propagate(False)

	# create back button widget
	tk.Button(
		menu,
		text="Back",
		font=normal_font,
		height=("1"),
		width=("5"),
		bg=menu_bg_color,
		fg=menu_fg_color,
		cursor="hand2",
		activebackground=menu_act_bg_color,
		activeforeground=act_fg_color, 
		command=lambda:load_settings_frame()
		).grid(row=0, column=0, sticky="w", padx="5", pady="3") # row==up and down, column==left and right

	# create about button widget
	tk.Button(
		menu,
		text="About",
		font=normal_font,
		height=("1"),
		width=("6"),
		bg=menu_bg_color,
		fg=menu_fg_color,
		cursor="hand2",
		activebackground=menu_act_bg_color,
		activeforeground=act_fg_color,
		command=opennanosite
		).grid(row=0, column=1, sticky="w", padx="5", pady="3")

	# create updates button widget
	tk.Button(
		menu,
		text="Updates",
		font=normal_font,
		height=("0"),
		width=("8"),
		bg=menu_bg_color,
		fg=menu_fg_color,
		cursor="hand2",
		activebackground=menu_act_bg_color,
		activeforeground=act_fg_color,
		command=opengithub
		).grid(row=0, column=2, sticky="w", padx="5", pady="3")

	# create storage button widget
	tk.Button(
		menu,
		text="Storage",
		font=normal_font,
		height=("0"),
		width=("8"),
		bg=menu_bg_color,
		fg=menu_fg_color,
		cursor="hand2",
		activebackground=menu_act_bg_color,
		activeforeground=act_fg_color,
		command=open_files # open file explorer to microSD card on NanoLab
		).grid(row=0, column=3, sticky="w", padx="5", pady="3")

	if comp_count >= 6:
		# create data results button widget
		tk.Button(
			menu,
			text="Data Results",
			font=normal_font,
			height=("0"),
			width=("12"),
			bg=menu_bg_color,
			fg=menu_fg_color,
			cursor="hand2",
			activebackground=menu_act_bg_color,
			activeforeground=act_fg_color,
			command=lambda:load_data_results_frame() # data results frame
			).grid(row=0, column=5, sticky="w", padx="5", pady="3")

	if dev_mode == True:
		# create log button widget
		tk.Button(
			menu,
			text="Log",
			font=normal_font,
			height=("0"),
			width=("4"),
			bg=menu_bg_color,
			fg=menu_fg_color,
			cursor="hand2",
			activebackground=menu_act_bg_color,
			activeforeground=act_fg_color,
			command=lambda:load_log_frame() # open a log of what is happening right now on the Arduino
			).grid(row=0, column=6, sticky="w", padx="5", pady="3")

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

	settings_title = Label(settings_frame, bg="white", text = "Main Settings", font=title_font)
	settings_title.grid(row=0, columnspan=3, column=1, padx="8", pady="5")

	# Add start and end calendars
	start_date = ""
	end_date = ""
	dates = []
	def sel_date():
		dates.append(end_cal.get_date())
		dates.append(start_cal.get_date())
		print(f"Experiment will run from {dates[1]} - {dates[0]}")
		"""
		# date.config(text = "" + start_cal.get_date() + "-" + end_cal.get_date())
		start_date = start_cal.get_date()
		end_date = end_cal.get_date()
		return start_date
		return end_date
		print(start_date)
		print(end_date)
		print(f"Experiment will run from {start_date} - {end_date}")
		"""

	schedule_label = Label(settings_frame, text="Schedule", font=("Ubuntu", 18), bg=bg_color, fg=fg_color)
	schedule_label.grid(row=1, columnspan=1, column=2, sticky="n", padx="8", pady="5")

	start_label = Label(settings_frame, text="Start Date:", font=normal_font, bg=bg_color, fg=fg_color)
	start_label.grid(row=1, columnspan=2, column=1, padx="8", pady="5")

	start_cal = Calendar(settings_frame, selectmode='day',
			year=cur_year, month=cur_month,
			day=cur_day, mindate=datetime.date(year=cur_year, month=cur_month, day=cur_day), font=calender_font) #date yyyy/mm/dd (no starting zeros)
	start_cal.grid(row=2, columnspan=2, column=1, padx="8", pady="5")

	end_label = Label(settings_frame, text="End Date:", font=normal_font, bg=bg_color, fg=fg_color)
	end_label.grid(row=1, columnspan=2, column=2, padx="8", pady="5")

	end_cal = Calendar(settings_frame, selectmode='day',
			year=cur_year, month=cur_month,
			day=cur_day, mindate=datetime.date(year=cur_year, month=cur_month, day=cur_day), font=calender_font)
	end_cal.grid(row=2, columnspan=2, column=2, padx="8", pady="5")

	tk.Button(
			settings_frame,
			text="Select Schedule",
			font=normal_font,
			height=("0"),
			width=("15"),
			bg=bg_color,
			fg=fg_color,
			cursor="hand2",
			activebackground=act_bg_color,
			activeforeground=act_fg_color,
			command=lambda:sel_date() # print select dates
			).grid(row=3, columnspan=1, column=2, sticky="", padx="5", pady="3")

	# text, font, height, width, row, column, columnspan, sticky, command
	w_pump_btn = MyButton("Water Pump Settings", big_font, 1, 19, 4, 1, 1, "sw", lambda:load_w_pump_settings_frame())
	led_set_btn = MyButton("LED Settings", big_font, 1, 19, 4, 2, 1, "sw", lambda:load_led_settings_frame())
	fan_set_btn = MyButton("Fan Settings", big_font, 1, 19, 4, 3, 1, "sw", lambda:load_fan_settings_frame())
	cam_set_btn = MyButton("Camera Intervals", big_font, 1, 19, 5, 1, 1, "sw", lambda:load_camera_settings_frame())
	atmos_set_btn = MyButton("Atmospheric Sensor", big_font, 1, 19, 5, 2, 1, "sw", lambda:load_atmos_sensor_frame())
	if comp_count <= 5:
		data_res_btn = MyButton("Data Results", big_font, 1, 19, 5, 3, 1, "sw", lambda:load_data_results_frame())
	set_preview_btn = MyButton("Send settings to your NanoLab", ("Ubuntu", 22), 0, 24, 6, 3, 2, "sw", lambda:load_set_preview_frame())
	if beta == True:
		beta_btn = MyButton("Rate your experience", ("Ubuntu", 10), 0, 19, 7, 0, 2, "sw", lambda:openbetaform())


	settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
	# print("settings loaded")

def load_w_pump_settings_frame(): 
	# clear_widgets(settings_frame)
	# raise water pump frame to the top
	w_pump_settings_frame.tkraise()
	# prevent widgets from modifying the frame
	w_pump_settings_frame.grid_propagate(False)

	# set the hardware of the current screen
	hardware = "water pump"

	# set list of settings
	w_pump_set = [] #"50mL", "5d/w"

	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(w_pump_settings_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	w_pump_title = Label(w_pump_settings_frame, bg="white", text = "Water Pump Settings", font=title_font)
	w_pump_title.grid(row=0, columnspan=8, column=1, padx="8", pady="5")

	if dev_mode == True:
		# master, rownum, columnnum, colspan, stickdir, command
		testbtn1 = TestButton(w_pump_settings_frame, 1, 1, 1, "w", lambda:test_pump())

	# frequency stuff
	# declaring string variables for storing frequencys
	fre1_in = tk.StringVar()
	fre2_in = tk.StringVar()
	 
	# defining a function that will get the two frequencys and print them
	def fre_set(): # eventually set to take all values of screen/component and save those

	    fre1 = fre1_in.get()
	    fre2 = fre2_in.get()
	    
	    print(hardware + " will run from: " + start_cal.get_date() + "-" + end_cal.get_date() + " " + fre1 + " times/ " + fre2)	    
	    fre1_in.set("")
	    
	    
	# creating a label for frequency input using widget Label
	fre_label = tk.Label(w_pump_settings_frame, text = 'Frequency of ' + hardware + ": ", font=normal_font, bg=bg_color, fg=fg_color)
	fre_label.grid(row=5, column=1, sticky="w")

	# creating a entry for input
	fre1_entry = tk.Entry(w_pump_settings_frame, textvariable = fre1_in, font=normal_font, bg=bg_color, fg=fg_color, width=3)
	fre1_entry.grid(row=5, columnspan=1, column=1, sticky="e")

	def character_limit(fre1_in):
		if len(fre1_in.get()) > 1:
			fre1_in.set(fre1_in.get()[-1])

	fre1_in.trace("w", lambda *args: character_limit(fre1_in))

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
	fre2_drop.config(font=normal_font, bg=bg_color, fg=fg_color)
	fre2_drop.grid(row=5, columnspan=1, column=2, sticky="", padx="7", pady="5")
	 
	# creating a button that will call the fre_set function  
	sub_btn=tk.Button(w_pump_settings_frame,text = 'Save', font=normal_font, bg=bg_color, fg=fg_color, command = fre_set)
	sub_btn.grid(row=5, columnspan=1, column=3, padx="7", pady="5", sticky="w")

	# set frame in window
	w_pump_settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")

	# print("H2O pump settings loaded")


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
	print('brightness', get_current_value())

# set LED screen colors
led_bg = "#ECECEC"
red_fg = "red"
orange_fg = "#834e02"
yellow_fg = "#787934"
green_fg = "green"
blue_fg = "blue"
purple_fg = "purple"

def test_LED():
	arduino.write(bytes('I', 'utf-8'))

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

def PARTYLED():
	# arduino.write(bytes("ROYGBPROYGBPROYGBPROYGBP", 'utf-8'))
	time.sleep(0.05)
	load_error()

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

	# set list of settings
	LED_set = [] #"red", "105"

	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(led_settings_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	led_settings_title = Label(led_settings_frame, bg="white", text = "LED Settings", font=title_font)
	led_settings_title.grid(row=0, columnspan=12, column=1, padx="8", pady="5")

	# create red color button widget
	tk.Button(
		led_settings_frame,
		text="Red",
		font=normal_font,
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
		font=normal_font,
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
		font=normal_font,
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
		font=normal_font,
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
		font=normal_font,
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
		font=normal_font,
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
		font=normal_font,
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
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		command=PARTYLED
		).grid(row=2, columnspan=3, column=11, sticky="s", padx="5", pady="3")

	rgb_code = ""

	# RGB color picker
	def choose_color():
		# variable to store hexadecimal code of color
		color_code = colorchooser.askcolor(title ="Choose color", initialcolor="#7714b9")
		rgb_code = color_code[0]
		print(rgb_code)
	
	print(rgb_code)

	# button to open color picker
	color_btn = tk.Button(led_settings_frame,text = 'Select precise color', font=normal_font, bg=bg_color, fg=fg_color, command = choose_color)
	color_btn.grid(row=3, columnspan=3, column=12, padx="7", pady="5", sticky="")

	# label for the slider
	slider_label = tk.Label(
    	led_settings_frame,
    	text='Brightness',
    	font=normal_font,
    	bg=bg_color,
		fg=fg_color
	).grid(row=4, columnspan=8, column=10, sticky="n", padx="0", pady="0")

	led_slider = Scale(led_settings_frame, from_=0, to=250, length=570, resolution=10, orient=HORIZONTAL, variable=current_value, bg=bg_color, fg=fg_color)
	led_slider.set(200)
	led_slider.grid(row=5, columnspan=8, column=10, sticky="n")

	if dev_mode == True:
		# master, rownum, columnnum, colspan, stickdir, command
		testbtn2 = TestButton(led_settings_frame, 1, 1, 1, "w", lambda:test_LED())

	# frequency stuff
	# declaring string variables for storing frequencys
	fre1_in = tk.StringVar()
	fre2_in = tk.StringVar()
	time_in = tk.StringVar()
	 
	# defining a function that will get the two frequencys and print them
	def fre_set(): # eventually set to take all values of screen/component and save those

	    fre1 = fre1_in.get()
	    fre2 = fre2_in.get()
	    time = time_in.get()
	    
	    print(hardware + " will run from: " + start_cal.get_date() + "-" + end_cal.get_date() + "" + " for " + time + " hours " + fre1 + " times/ " + fre2 + " with RGB value of " + rgb_code)
	    
	    fre1_in.set("")
	    time_in.set("")
	    

	# creating a label for frequency input using widget Label
	fre_label = tk.Label(led_settings_frame, text = 'Frequency of ' + hardware + ": ", font=normal_font, bg=bg_color, fg=fg_color)
	fre_label.grid(row=10, columnspan=1, column=1, sticky="w")

	# creating a entry for input
	fre1_entry = tk.Entry(led_settings_frame, textvariable = fre1_in, font=normal_font, bg=bg_color, fg=fg_color, width=3)
	fre1_entry.grid(row=10, columnspan=1, column=2, padx="5", pady="5", sticky="w")

	def character_limit(fre1_in):
		if len(fre1_in.get()) > 1:
			fre1_in.set(fre1_in.get()[-1])

	fre1_in.trace("w", lambda *args: character_limit(fre1_in))

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
	fre2_drop.config(font=normal_font, bg=bg_color, fg=fg_color)
	fre2_drop.grid(row=10, columnspan=2, column=3, padx="5", pady="5", sticky="e")

	time_label = tk.Label(led_settings_frame, text = 'Time (in hours) that ' + hardware + "s will run for: ", font=normal_font, bg=bg_color, fg=fg_color)
	time_label.grid(row=11, columnspan=4, column=1, sticky="w")

	time_entry = tk.Entry(led_settings_frame,textvariable = time_in, font=normal_font, bg=bg_color, fg=fg_color, width=3)
	time_entry.grid(row=11, columnspan=1, column=5, padx="7", pady="5", sticky="")

	def character_limit(time_in):
		if len(time_in.get()) > 1:
			time_in.set(time_in.get()[-1])

	time_in.trace("w", lambda *args: character_limit(time_in))

	# creating a button that calls the fre_set function
	sub_btn = tk.Button(led_settings_frame,text = 'Save', font=normal_font, bg=bg_color, fg=fg_color, command = fre_set)
	sub_btn.grid(row=12, columnspan=1, column=1, padx="7", pady="5", sticky="w")

	# set frame in window
	led_settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")

	# print("LED settings loaded")

def load_fan_settings_frame(): 
	# clear_widgets(settings_frame)
	# raise fan settings frame to the top
	fan_settings_frame.tkraise()
	# prevent widgets from modifying the frame
	fan_settings_frame.grid_propagate(False)

	# set the hardware of the current screen
	hardware = "fan"

	# set list of settings
	fan_set = [] #"90%", "30m/3d/w"

	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(fan_settings_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	fan_settings_title = Label(fan_settings_frame, bg="white", text = "Fan Settings", font=title_font)
	fan_settings_title.grid(row=0, columnspan=8, column=1, padx="8", pady="5")

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
	slider_label = tk.Label(
    	fan_settings_frame,
    	text='Fan Strength (%)',
    	font=normal_font, 
		bg=bg_color,
		fg=fg_color
	).grid(row=1, columnspan=3, column=1, sticky="n")

	fan_strength_slider = Scale(fan_settings_frame, from_=0, to=100, length=755, resolution=10, orient=HORIZONTAL, variable=current_value, bg=bg_color, fg=fg_color)
	fan_strength_slider.set(70)
	fan_strength_slider.grid(row=2, columnspan=8, column=1, sticky="n")

	if dev_mode == True:
		# master, rownum, columnnum, colspan, stickdir, command
		testbtn3 = TestButton(fan_settings_frame, 1, 1, 3, "w", lambda:test_fan())

	# frequency stuff
	# declaring string variables for storing frequencys
	fre1_in = tk.StringVar()
	fre2_in = tk.StringVar()
	 
	# defining a function that will get the two frequencys and print them
	def fre_set(): # eventually set to take all values of screen/component and save those

	    fre1 = fre1_in.get()
	    fre2 = fre2_in.get()
	    
	    print(hardware + " will run from: " + start_cal.get_date() + "-" + end_cal.get_date() + " with " + str(current_value.get()) + "% power")
	    
	    fre1_in.set("")
	    
	"""
	# creating a label for frequency input using widget Label
	fre_label = tk.Label(fan_settings_frame, text = 'Frequency of ' + hardware + ": ", font=normal_font, bg=bg_color, fg=fg_color)
	fre_label.grid(row=6, column=1, sticky="w")

	# creating a entry for input
	fre1_entry = tk.Entry(fan_settings_frame,textvariable = fre1_in, font=normal_font, bg=bg_color, fg=fg_color, width=18)
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
	fre2_drop.config(font=normal_font, bg=bg_color, fg=fg_color)
	fre2_drop.grid(row=6, column=2)
	"""

	# creating a button that will call the fre_set function  
	sub_btn=tk.Button(fan_settings_frame,text = 'Save', font=normal_font, bg=bg_color, fg=fg_color, command = fre_set)
	sub_btn.grid(row=6, columnspan=2, column=2, padx="7", pady="5", sticky="")

	# set frame in window
	fan_settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
	
	# print("fan settings loaded")

def load_camera_settings_frame(): 
	# clear_widgets(settings_frame)
	# raise camera settings frame to the top
	camera_settings_frame.tkraise()
	# prevent widgets from modifying the frame
	camera_settings_frame.grid_propagate(False)

	# set the hardware of the current screen
	hardware = "camera"

	# set list of settings
	cam_set = [] #"1/w"

	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(camera_settings_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	cam_settings_title = Label(camera_settings_frame, bg="white", text = "Camera Intervals", font=title_font)
	cam_settings_title.grid(row=0, columnspan=8, column=1, padx="8", pady="5")
	
	if dev_mode == True:
		# master, rownum, columnnum, colspan, stickdir, command
		testbtn4 = TestButton(camera_settings_frame, 2, 1, 1, "w", lambda:take_picture())

	# frequency stuff
	# declaring string variables for storing frequencys
	fre1_in = tk.StringVar()
	fre2_in = tk.StringVar()
	 
	# defining a function that will get the two frequencys and print them
	def fre_set(): # eventually set to take all values of screen/component and save those

	    fre1 = fre1_in.get()
	    fre2 = fre2_in.get()
	    
	    print(hardware + " will run from: " + start_cal.get_date() + "-" + end_cal.get_date() + " " + fre1 + " times/ " + fre2)
	    
	    fre1_in.set("")
	    
	    
	# creating a label for frequency input using widget Label
	fre_label = tk.Label(camera_settings_frame, text = 'Frequency of ' + hardware + ": ", font=normal_font, bg=bg_color, fg=fg_color)
	fre_label.grid(row=5, columnspan=2, column=1, sticky="w")

	# creating a entry for input
	fre1_entry = tk.Entry(camera_settings_frame,textvariable = fre1_in, font=normal_font, bg=bg_color, fg=fg_color, width=4)
	fre1_entry.grid(row=5, columnspan=1, column=2, sticky="")

	def character_limit(fre1_in):
		if len(fre1_in.get()) > 1:
			fre1_in.set(fre1_in.get()[-1])

	fre1_in.trace("w", lambda *args: character_limit(fre1_in))

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
	fre2_drop.config(font=normal_font, bg=bg_color, fg=fg_color) 
	fre2_drop.grid(row=5, columnspan=2, column=2, padx="7", pady="5", sticky="")
	 
	# creating a button that will call the fre_set function  
	sub_btn=tk.Button(camera_settings_frame,text = 'Save', font=normal_font, bg=bg_color, fg=fg_color, command = fre_set)
	sub_btn.grid(row=5, columnspan=1, column=3, padx="7", pady="5", sticky="")

	# set frame in window
	camera_settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")

	# print("camera settings loaded")

def load_atmos_sensor_frame(): 
	# clear_widgets(settings_frame)
	# raise atmospheric sensor frame to the top
	atmos_sensor_frame.tkraise()
	# prevent widgets from modifying the frame
	atmos_sensor_frame.grid_propagate(False)

	# set the hardware of the current screen
	hardware = "atmospheric sensor"

	# set list of settings
	atmos_sen_set = [] #"2/d"

	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(atmos_sensor_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	atmos_sensor_title = Label(atmos_sensor_frame, bg="white", text = "Atmospheric Sensor Settings", font=title_font)
	atmos_sensor_title.grid(row=0, columnspan=8, column=1, padx="8", pady="5")

	if dev_mode == True:
		# master, rownum, columnnum, colspan, stickdir, command
		testbtn5 = TestButton(atmos_sensor_frame, 2, 1, 1, "w", lambda:take_atmos_reading())

	# frequency stuff
	# declaring string variables for storing frequencys
	fre1_in = tk.StringVar()
	fre2_in = tk.StringVar()
	 
	# defining a function that will get the two frequencys and print them
	def fre_set(): # eventually set to take all values of screen/component and save those

	    fre1 = fre1_in.get()
	    fre2 = fre2_in.get()
	    
	    print(hardware + " will run from: " + start_cal.get_date() + "-" + end_cal.get_date() + " " + fre1 + " times/ " + fre2)
	    
	    fre1_in.set("")
	    
	    
	# creating a label for frequency input using widget Label
	fre_label = tk.Label(atmos_sensor_frame, text = 'Frequency of ' + hardware + ": ", font=normal_font, bg=bg_color, fg=fg_color)
	fre_label.grid(row=5, columnspan=2, column=1, sticky="w")

	# creating a entry for input
	fre1_entry = tk.Entry(atmos_sensor_frame,textvariable = fre1_in, font=normal_font, bg=bg_color, fg=fg_color, width=8)
	fre1_entry.grid(row=5, columnspan=1, column=3, padx="7", pady="5", sticky="w")

	def character_limit(fre1_in):
		if len(fre1_in.get()) > 1:
			fre1_in.set(fre1_in.get()[-1])

	fre1_in.trace("w", lambda *args: character_limit(fre1_in))

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
	fre2_drop.config(font=normal_font, bg=bg_color, fg=fg_color)
	fre2_drop.grid(row=5, columnspan=2, column=3, padx="7", pady="5", sticky="")
	 
	# creating a button that will call the fre_set function  
	sub_btn = tk.Button(atmos_sensor_frame,text = 'Save', font=normal_font, bg=bg_color, fg=fg_color, command = fre_set)
	sub_btn.grid(row=5, columnspan=2, column=4, padx="7", pady="5", sticky="e")

	# checkbox made with class
	class MyCheckbox:
		def __init__(self, master, checktext, rownum, columnnum, stickdir):
			self.master = master
			self.checkbox_value = tk.BooleanVar()
			self.checktext = checktext
			self.checkbox = tk.Checkbutton(master, text=self.checktext, variable=self.checkbox_value, command=self.on_change)
			self.checkbox.config(bg=bg_color, fg=fg_color, font=normal_font, selectcolor="white", relief="raised", padx=10, pady=5)
			self.rownum = rownum
			self.columnnum = columnnum
			self.stickdir = stickdir
			self.checkbox.grid(row=self.rownum, column=self.columnnum, padx="7", pady="5", sticky=stickdir)

		def on_change(self):
			print(f"Record {self.checktext} = {self.checkbox_value.get()}")

	gas_checkbox = MyCheckbox(atmos_sensor_frame, "Gas (VOCs)", 1, 6, "")
	temp_checkbox = MyCheckbox(atmos_sensor_frame, "Temperature", 2, 6, "")
	humid_checkbox = MyCheckbox(atmos_sensor_frame, "Humidity", 3, 6, "n")
	press_checkbox = MyCheckbox(atmos_sensor_frame, "Barometric pressure", 3, 6, "")

	# set frame in window
	atmos_sensor_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")

	# print("atmos sensor frame loaded")

def load_data_results_frame(): 
	# clear_widgets(settings_frame)
	# raise data results frame to the top
	data_results_frame.tkraise()
	# prevent widgets from modifying the frame
	data_results_frame.grid_propagate(False)

	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(data_results_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	data_r_title = Label(data_results_frame, bg="white", text = "Data Results", font=title_font)
	data_r_title.grid(row=0, columnspan=8, column=1, padx="8", pady="5")

	# graph
	def load_graph(): 

	    # the figure that will contain the plot 
	    fig = Figure(figsize = (6, 4), 
	                dpi = 100) 

	    # list of squares 
	    y = [i**2 for i in range(101)] 

	    # adding the subplot 
	    plot1 = fig.add_subplot(111) 

	    # plotting the graph 
	    plot1.plot(y) 

	    # creating the Tkinter canvas containing the Matplotlib figure
	    canvas = FigureCanvasTkAgg(fig, master = data_results_frame)    
	    canvas.draw() 

	    # placing the canvas on the Tkinter window 
	    canvas.get_tk_widget().grid(row=2, columnspan=4, column=1) 

	    # creating the Matplotlib toolbar 
	    toolbar = NavigationToolbar2Tk(canvas, data_results_frame)
	    toolbar.config() 
	    toolbar.update() 

	    # placing the toolbar on the Tkinter window 
	    toolbar.grid(row=1, columnspan=1, column=2, sticky="w")

	# create update button widget
	tk.Button(
		data_results_frame,
		text="Update",
		font=normal_font,
		height=("0"),
		width=("7"),
		bg=bg_color,
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		command=load_graph(), # update the graph
		).grid(row=1, column=1, sticky="w", padx="5", pady="3")

	"""
	# Dropdown to choose kind of graph
	def show_graph_new(): 
		print(clicked.get())

	# Dropdown menu options 
	options = [ 
	    "Graph", 
	    "Line Graph", 
	    "Bar Graph" 
	] 

	clicked = StringVar()

	# initial menu text 
	clicked.set("Graph")

	# Create Dropdown menu 
	drop = OptionMenu(data_results_frame, clicked, *options)
	drop.config(bg=bg_color, fg=fg_color, font=normal_font) 
	drop.grid(row=1, column=3, sticky="e")

	# Create button that updates graph
	button = Button(data_results_frame, text = "Choose", font=normal_font, height=("0"), width=("7"), 
	bg=bg_color, fg=fg_color, activebackground=act_bg_color, activeforeground=act_fg_color, command = show_graph_new)
	button.grid(row=1, column=4, sticky="w")
	"""


	# set frame in window
	data_results_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")

	# print("data results loaded")

def load_error():
	error_404_frame.tkraise()
	# prevent widgets from modifying the frame
	error_404_frame.pack_propagate(False)

	e404_title = Label(error_404_frame, bg="grey", text = "error_404", font=("Ubuntu", 60))
	e404_title.pack(fill="both", expand=True, side="top")

	# Read the Image
	image = Image.open("assets/error_404.png")
	# Resize the image using resize() method
	resize_image = image.resize((200, 200))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(error_404_frame, image=logo_img, bg="grey")
	logo_widget.image = logo_img
	logo_widget.pack()

	e404_title2 = Label(error_404_frame, bg="grey", text = "Sorry! That page doesn't exist.", font=("Ubuntu", 30))
	e404_title2.pack(fill="both", expand=True, side="bottom")


	error_404_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")

def load_log_frame(): # log of what is happening on Arduino right now
	# clear_widgets()
	log_frame.tkraise()
	# prevent widgets from modifying the frame
	log_frame.grid_propagate(False)

	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(log_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	log_title = Label(log_frame, bg="white", text = "Log", font=title_font)
	log_title.grid(row=0, columnspan=8, column=1, padx="8", pady="5")

	# Read the Image
	image = Image.open("assets/log.jpg")
	# Resize the image using resize() method
	resize_image = image.resize((1000, 700))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(log_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=1, column=1, sticky="nsew", padx="8", pady="5")

	# set frame in window
	log_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")

	# print("log loaded")

def load_set_preview_frame(): # preview of settings
	# clear_widgets()
	set_preview_frame.tkraise()
	# prevent widgets from modifying the frame
	set_preview_frame.grid_propagate(False)

	# Read the Image
	image = Image.open("assets/NanoLabs_logo.png")
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(set_preview_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	set_preview_title = Label(set_preview_frame, bg=bg_color, text = "Preview Your Settings", font=title_font)
	set_preview_title.grid(row=0, columnspan=8, column=1, padx="8", pady="5")

	w_pump_preview_title = Label(set_preview_frame, bg=bg_color, text = "Water Pump", font=("Ubuntu", 14))
	w_pump_preview_title.grid(row=1, columnspan=2, column=1, padx="8", pady="5")

	LED_preview_title = Label(set_preview_frame, bg=bg_color, text = "LED", font=("Ubuntu", 14))
	LED_preview_title.grid(row=1, columnspan=2, column=3, padx="8", pady="5")

	fan_preview_title = Label(set_preview_frame, bg=bg_color, text = "Fan", font=("Ubuntu", 14))
	fan_preview_title.grid(row=2, columnspan=2, column=1, padx="8", pady="5")

	camera_preview_title = Label(set_preview_frame, bg=bg_color, text = "Camera", font=("Ubuntu", 14))
	camera_preview_title.grid(row=2, columnspan=2, column=3, padx="8", pady="5")

	atmos_preview_title = Label(set_preview_frame, bg=bg_color, text = "Atmospheric Sensor", font=("Ubuntu", 14))
	atmos_preview_title.grid(row=3, columnspan=2, column=1, padx="8", pady="5")

	# create cancel button widget
	tk.Button(
		set_preview_frame,
		text="Cancel",
		font=("Ubuntu", 14),
		height=("2"),
		width=("17"),
		bg=bg_color,
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		command=lambda:load_settings_frame # command to go back to main screen
		).grid(row=3, columnspan=1, column=3, sticky="w", padx="5", pady="3")

	# create confirm button widget
	tk.Button(
		set_preview_frame,
		text="Confirm settings",
		font=("Ubuntu", 14),
		height=("2"),
		width=("17"),
		bg=bg_color,
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		command=send_settings # command to send settings to NanoLab
		).grid(row=3, columnspan=1, column=4, sticky="w", padx="5", pady="3")

	# set frame in window
	set_preview_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")

	# print("settings preview loaded")

# run main app
load_menu()
load_settings_frame()
root.mainloop()

# main window end
# =======================