
# Code writen by Asher Powell at Warren Tech North
# Version 1.3a
vernum = "1.3a"
dev_mode = True # if True will show log button and test buttons
beta = True # enable beta testing form button

# import dependencies
import tkinter as tk
# import tkinter.ttk as ttk
from tkinter import *
from tkinter import colorchooser
from PIL import Image, ImageTk
import pyglet
import webbrowser
import serial
import serial.tools.list_ports
import sys
import os
import time
from tkcalendar import Calendar
import datetime
from datetime import date 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from pathlib import Path

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# set fonts
pyglet.font.add_file(resource_path("fonts\\Ubuntu-Bold.ttf"))
normal_font = ("Ubuntu", 12)
big_font = ("Ubuntu", 24)
title_font = ("Ubuntu", 46)
calender_font = ("Arial", 10)

# open log file
logf = open('data\\log.txt', 'w+')
logf.write(f"GUI: Log opened\n")
print(chr(sum(range(ord(min(str(not())))))))
log_new = True


## Arduino Stuff ##

# Install drivers
#os.system('"drivers\\CH341SER.EXE"')

# stackoverflow.com/questions/24214643/python-to-automatically-select-serial-ports-for-arduino
# find live ports with Arduinos on them
serPort = ""
int1 = 0
ardname = ""
global port
port = "error"

def findard():
	serPort = ""
	int1 = 0
	ardname = ""
	global port
	port = "error"

	ports = list(serial.tools.list_ports.comports()) ## tell clair to make func to send if board flashed with correct code or not ##
	if len(ports) == 0:
		port = "not found"
	for p in ports: ## make func to check for serport info of ard ##
		print (p) # This causes each port's information to be printed out
				# To search this p data, use p[1]

		while int1 < 9:   # Loop checks "COM0" to "COM8" for Adruino Port Info

			if "CH340" in p[1]:  # Looks for "CH340" in P[1].
				port = str(int1) # Converts an Integer to a String, allowing:
				ardname = f"COM{port}" # add the strings together

			if "CH340" in p[1] and ardname in p[1]: # Looks for "CH340" and "COM#"
				print (f"Found Arduino on {ardname}")
				logf.write(f"GUI: Found Arduino on {ardname}\n")
				rfr_widget.grid(row=0, columnspan=1, column=2, sticky="se", padx="0", pady="0")
				int1 = 9 # Causes loop to end

			if int1 == 8:
				port = "not found"
				print ("Arduino not found!")
				rfr_widget.grid(row=0, columnspan=1, column=2, sticky="se", padx="0", pady="0")

			int1 = int1 + 1

	try:
		arduino = serial.Serial(ardname, 115200, timeout=10) # your Arduino speed and timeout values

		# This opens the serial port
		arduino.close()  # In case the port is already open this closes it.
		arduino.open()   # Reopen the port.

		arduino.flushInput()
		arduino.flushOutput()
	except: #fix this so if the ard not responding or smth do it
		#port = "not connected"
		print("exception found")
		logf.write("GUI: Arduino not found\n")
findard()

## End Arduino stuff ##

# set starting variables
global dark_mode
global components
dark_mode = False # changes color theme
comp_count = 5 # number of components
components = []
type_selected = False
box_type = ""

setup_root = tk.Tk()

def toggle_dark():
	global dark_mode
	dark_mode = not dark_mode
	print(f"{dark_mode}")
	logf.write(f"GUI: dark_mode = {dark_mode}\n")

def set_theme():
	global menu_bg_color, menu_fg_color, menu_act_bg_color, bg_color, fg_color, act_bg_color, act_fg_color
	if dark_mode:
		# set dark mode colors
		menu_bg_color = "#000000"
		menu_fg_color = "#ffffff"
		menu_act_bg_color = "#ffffff"
		bg_color = "#000000"
		fg_color = "#ffffff"
		act_bg_color = "#808080"
		act_fg_color = "#ffffff"
	else:
		# set normal colors
		menu_bg_color = "#000000"
		menu_fg_color = "#ffffff"
		menu_act_bg_color = "#000000"
		bg_color = "#ffffff"
		fg_color = "#000000"
		act_bg_color = "#ffffff"
		act_fg_color = "#808080"
set_theme()


# =======================
# setup window stuff
# =======================

# create object
#setup_root = tk.Tk()
setup_root.title("Universal NanoLab Setup")
setup_root.configure(bg=bg_color)

# set logo
setup_root.iconbitmap(resource_path("assets\\Universal logo.ico"))
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

def load_setup1():
	set_theme()

	setup1_frame.tkraise()
	# prevent widgets from modifying the frame
	setup1_frame.grid_propagate(False)

	def type_hydro():
		box_type = "HydroFuge"
		print(box_type + " selected")
		logf.write(f"GUI: {box_type} selected\n")
		hydro_logo_widget.config(bg="green")
		hydro_logo_widget.grid(row=2, columnspan=3, column=1, sticky="", padx="8", pady="5")
		uni_logo_widget.config(bg="#ffffff")
		uni_logo_widget.grid(row=2, columnspan=3, column=4, sticky="", padx="8", pady="5")
		saveBtn.config(state="normal")
		saveBtn.grid(row=4, columnspan=2, column=3, sticky="", padx="5", pady="3")
		global components
		components = ["Water Pump Settings", "LED Settings", "Fan Settings", "Timelapse Intervals", "Atmospheric Sensor", "Data Results"]
		comp_count = len(components)
		print(comp_count)
		global cmdlist
		cmdlist = [raise_wp_set, raise_led_set, raise_fan_set, raise_cam_set, raise_atmos_set, raise_data_results]
		type_selected = True

	def type_uni():
		box_type = "Universal"
		print(box_type + " selected")
		logf.write(f"GUI: {box_type} selected\n")
		#uni_logo_widget.config(bg="green")
		#uni_logo_widget.grid(row=2, columnspan=3, column=4, sticky="", padx="8", pady="5")
		uniops_frame.grid(row=2, columnspan=3, column=4, sticky="nsew", padx="8", pady="5")
		uniops_frame.tkraise()
		hydro_logo_widget.config(bg="#ffffff")
		hydro_logo_widget.grid(row=2, columnspan=3, column=1, sticky="", padx="8", pady="5")
		#saveBtn.config(state="normal")
		#saveBtn.grid(row=4, columnspan=2, column=3, sticky="", padx="5", pady="3")
		global components
		components = ["no", "um", "maybe", "112345678"]
		unichecks()
		comp_count = len(components)
		if comp_count <= 5:
			components.append("Data Results")
		global cmdlist
		cmdlist = []
		type_selected = True

	# Set Label
	welcome_label = Label(setup1_frame, text="Welcome to your NanoLab!", font=("Ubuntu-Bold", 20), bg=bg_color, fg=fg_color)
	welcome_label.grid(row=0, columnspan=8, column=0, sticky="")

	welcome_label = Label(setup1_frame, text="Pick Your Version", font=("Ubuntu-Bold", 18), bg=bg_color, fg=fg_color)
	welcome_label.grid(row=1, columnspan=8, column=0, sticky="")

	# add image button of HydroFuge and "coming soon" for Universal
	# HydroFuge
	# Read the Image
	image = Image.open(resource_path("assets\\Universal NanoLab.png"))
	# Resize the image using resize() method
	resize_image = image.resize((270, 320))
	logo_img = ImageTk.PhotoImage(resize_image)
	hydro_logo_widget = tk.Button(setup1_frame, image=logo_img, bg=bg_color, highlightcolor="gray", command=type_hydro)
	hydro_logo_widget.image = logo_img
	hydro_logo_widget.grid(row=2, columnspan=3, column=1, sticky="", padx="8", pady="5")

	# add HydroFuge label under button
	hydrofuge_label = Label(setup1_frame, text="HydroFuge", font=normal_font, bg=bg_color, fg=fg_color)
	hydrofuge_label.grid(row=3, columnspan=3, column=1, sticky="", padx="5", pady="3")

	# Universal
	# Read the Image
	image = Image.open(resource_path("assets\\Coming Soon.png"))
	# Resize the image using resize() method
	resize_image = image.resize((270, 320))
	logo_img = ImageTk.PhotoImage(resize_image)
	uni_logo_widget = tk.Button(setup1_frame, image=logo_img, bg=bg_color, state='normal', command=type_uni)
	uni_logo_widget.image = logo_img
	uni_logo_widget.grid(row=2, columnspan=3, column=4, sticky="", padx="8", pady="5")

	# add Universal label under button
	hydrofuge_label = Label(setup1_frame, text="Universal (Coming Soon)", font=normal_font, bg=bg_color, fg=fg_color)
	hydrofuge_label.grid(row=3, columnspan=3, column=4, sticky="", padx="5", pady="3")

	# setup for universal checkboxes
	uniops_frame = tk.Frame(setup1_frame, highlightbackground="grey", highlightthickness=1, width=270, height=320, bg=bg_color)
	uni_check_lbl = tk.Label(uniops_frame, text=f"What components \ndo you have?", font=normal_font, bg=bg_color, fg=fg_color, padx="2", pady="8")
	uni_check_lbl.grid(row=0, column=0, padx="2", pady="8", sticky="we")
	testbool = tk.BooleanVar()
	unibool = tk.BooleanVar()
	global components
	def on_change():
		print(f"{comp_chks[0]} = {testbool.get()}")
		#components.append(testbool.get())
		print(components)
	def unichecks():
		for c in components:
			comp_chks = components.copy()
			rownum = 2
			colnum = 0
			num = 1

			while comp_chks:
				unicheck = tk.Checkbutton(uniops_frame, text=comp_chks[0], variable=unibool, command=on_change)
				unicheck.grid(row=rownum, column=colnum)
				del comp_chks[0]
				rownum += 1
				num += 1

	# Finish setup or go to next frame
	saveBtn = tk.Button(setup1_frame,
		text="Done", # Next
		font=normal_font,
		height=("1"),
		width=("7"),
		bg=bg_color,
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		state='disabled',
		command=setup_root.destroy) # lambda:load_setup2()
	saveBtn.grid(row=4, columnspan=2, column=3, sticky="", padx="5", pady="3")

	version_label = Label(setup1_frame, text=f"v.{vernum}", font=("Ubuntu", 8), bg=bg_color, fg=fg_color)
	version_label.grid(row=4, columnspan=2, column=0, sticky="sw")

	## Dark Mode Button ##
	dark_mode = False
	# Define switch function
	def switch_theme():
		global dark_mode
		toggle_dark()
		# Determine if on or off
		if dark_mode:
			theme_switch.config(image = darkimg)
			theme_label.config(text = "Dark")
			theme_label.grid(rowspan=2, row=3, columnspan=1, column=2, sticky="", padx="1", pady="1")
			theme_switch.grid(rowspan=2, row=4, columnspan=1, column=2, sticky="s", padx="1", pady="1")
			set_theme()
		else:
			theme_switch.config(image = lightimg)
			theme_label.config(text = "Light")
			theme_label.grid(rowspan=2, row=3, columnspan=1, column=2, sticky="", padx="1", pady="1")
			theme_switch.grid(rowspan=2, row=4, columnspan=1, column=2, sticky="s", padx="1", pady="1")
			set_theme()

	theme_label = Label(setup1_frame, text="Light", font=("Ubuntu", 8), bg=bg_color, fg=fg_color)
	#theme_label.grid(rowspan=2, row=3, columnspan=1, column=2, sticky="", padx="1", pady="1")

	lightimg = PhotoImage(file = resource_path("assets\\light.png"))
	darkimg = PhotoImage(file = resource_path("assets\\dark.png"))

	theme_switch = tk.Button(setup1_frame, image=lightimg, bg=bg_color, width=48, height=28, command=lambda:switch_theme())
	#theme_switch.grid(rowspan=2, row=4, columnspan=1, column=2, sticky="s", padx="1", pady="1")

	if dark_mode == True:
		theme_switch.config(image = darkimg)
		theme_label.config(text = "Dark")
		theme_label.grid(rowspan=2, row=3, columnspan=1, column=2, sticky="", padx="1", pady="1")
		theme_switch.grid(rowspan=2, row=4, columnspan=1, column=2, sticky="s", padx="1", pady="1")
		dark_mode = False
		set_theme()
	if dark_mode == False:
		theme_switch.config(image = lightimg)
		theme_label.config(text = "Light")
		theme_label.grid(rowspan=2, row=3, columnspan=1, column=2, sticky="", padx="1", pady="1")
		theme_switch.grid(rowspan=2, row=4, columnspan=1, column=2, sticky="s", padx="1", pady="1")
		dark_mode = True
		set_theme()

	# print("first screen loaded")

"""
def load_setup2():
	setup2_frame.tkraise()
	# prevent widgets from modifying the frame
	setup2_frame.grid_propagate(False)

	# Set Label
	welcome2_label = Label(setup2_frame, text="Pick Your Version", font=("Ubuntu", 20), bg=bg_color)
	welcome2_label.grid(row=0, columnspan=4, column=3, sticky="")

	# print("second screen loaded")
"""

# run setup screen
load_setup1()
setup_root.mainloop()

# =======================
# setup end
# =======================


# =======================
# main window stuff
# =======================

# creating the date object of today's date 
todays_date = date.today() 
# printing todays date 
print("Current date: ", todays_date)
# date vars 
cur_month = todays_date.month
cur_day = todays_date.day
cur_year = todays_date.year

# changed bools
schedule_changed = False
wp_changed = False
led_changed = False
fan_changed = False
cam_changed = False
atmos_changed = False

# file stuff
curdir = Path.cwd()
homedir = Path.home()
parentdir = Path(__file__).parent
strtdir = Path(parentdir).parent
# print(strtdir) # C:.../NanoLab-GUI
file_path = Path((strtdir) / "Arduino\\basic_hydrofuge_schedule")
#f = Path(file_path / "array_for_arduino.h")
# f = open('Arduino\\basic_hydrofuge_schedule\\array_for_arduino.h', 'w')
f = open('data\\settings.txt', 'w')
print(f)
logf.write("GUI: Settings file opened\n")
#if f.is_file():
	#print(f.suffix)
#else:
	#print("not a file")
#f.open(mode="w")
# f.write_text(f"test \nlol \n{atmos_changed}")
# f.write_bytes(b"0")

# initiallize app with basic settings
root = Tk() # root is the main window name
root.title("Universal NanoLab Settings")
root.configure(bg=bg_color)
# set logo
root.iconbitmap(resource_path("assets\\Universal logo.ico"))
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
settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
w_pump_settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
led_settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
fan_settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
camera_settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
atmos_sensor_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
# error_404_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")

# set websites
nano_site = "https://sites.google.com/jeffcoschools.us/universal-nanolab/project-home-page"
github = "https://github.com/ClairBearmakes/NanoLab-GUI"
betaform = "https://docs.google.com/forms/d/e/1FAIpQLScn_A1m8JzfphVgT83yOyETZGsvzdgrhsZ03veFijbZWohrrg/viewform"

# set classes
# buttons
class MyButton: # text, font, height, width, row, column, columnspan, sticky, command
	# class variables (attributes)
	master = settings_frame # change with MyButton.master = whatever_frame
	bg_color = bg_color

	def __init__(self, btntext, font, btnheight, btnwidth, rownum, columnnum, colspan, stickdir, command):	
		self.btntext = btntext
		self.font = font
		self.btnheight = btnheight
		self.btnwidth = btnwidth
		self.command = command
		self.rownum = rownum
		self.columnnum = columnnum
		self.colspan = colspan
		self.stickdir = stickdir
		#self.state = state

		self.btn = tk.Button(self.master, 
		text=self.btntext, font=font,
		height = btnheight,  width = btnwidth,
		bg = self.bg_color, fg = fg_color,
		activebackground = act_bg_color, activeforeground = act_fg_color,
		cursor = "hand2", command=self.command)
		self.btn.config(padx=0, pady=0)
		self.btn.grid(row=self.rownum, column=self.columnnum, columnspan=self.colspan, padx="8", pady="5", sticky=stickdir)

	# def on_change(self):
		# print(f"Record {self.checktext} = {self.checkbox_value.get()}") 

# main buttons for main settings screen
class MainBtns: # btntext, rownum, columnnum, command
	# class variables (attributes)
	master = settings_frame # change with MyButton.master = whatever_frame
	bg_color = bg_color

	def __init__(self, btntext, rownum, columnnum, command):	
		self.btntext = btntext
		self.font = big_font
		self.btnheight = 2
		self.btnwidth = 19
		self.rownum = rownum
		self.columnnum = columnnum
		self.colspan = 1
		self.stickdir = "sw"
		self.command = command

		self.btn = tk.Button(self.master, 
		text=self.btntext, font=self.font,
		height = self.btnheight,  width = self.btnwidth,
		bg = self.bg_color, fg = fg_color,
		activebackground = act_bg_color, activeforeground = act_fg_color,
		cursor = "hand2", command=self.command)
		self.btn.config(padx=0, pady=0)
		self.btn.grid(row=self.rownum, column=self.columnnum, columnspan=self.colspan, padx="8", pady="5", sticky=self.stickdir)

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

# sliders
class Sliders: # master, hardware, rownum, colnum, stickdir, command
	# class variables (attributes) ## change with Sliders.durto ##
	dur_unit = "minutes" # unit of dur slider
	durto = 360 # defining run time limit
	freto = 24 # defining times it runs in 24h period
	delayto = 720 # defining delay limit
	dur_val = 0 # variables holding slider value
	fre_val = 0
	delay_val = 0
	durres = 10 # resolution of sliders
	freres = 1
	delayres = 10
	dur_true = True # bool defining to show slider or not
	fre_true = True
	delay_true = True

	def __init__(self, master, hardware, rownum, colnum, stickdir, command):
		self.master = master
		self.hardware = hardware
		self.label_txt = f"How long do you want {hardware} to run? ({self.dur_unit})"
		self.label_txt2 = f"How many times should {hardware} run? (24h period)"
		self.label_txt3 = f"How much delay do you want between runs? (minutes)"
		self.rownum = rownum
		self.colnum = colnum
		self.colspan = 3
		self.stickdir = stickdir
		self.command = command
		self.dur_value = tk.DoubleVar()
		self.fre_value = tk.DoubleVar()
		self.delay_value = tk.DoubleVar()

		self.durslider = Scale(self.master, from_=0, to=self.durto, length=700, resolution=self.durres, orient=HORIZONTAL, 
			variable=self.dur_value, label=self.label_txt, font=normal_font, bg=bg_color, fg=fg_color)
		self.durslider.set(10)
		if self.dur_true == True:
			self.durslider.grid(row=self.rownum, columnspan=self.colspan, column=self.colnum, sticky=self.stickdir, padx="0", pady="10")

		self.freslider = Scale(self.master, from_=0, to=self.freto, length=700, resolution=self.freres, orient=HORIZONTAL, 
			variable=self.fre_value, label=self.label_txt2, font=normal_font, bg=bg_color, fg=fg_color)
		self.freslider.set(10)
		if self.fre_true == True:
			self.freslider.grid(row=self.rownum+1, columnspan=self.colspan, column=self.colnum, sticky=self.stickdir, padx="0", pady="10")

		self.delayslider = Scale(self.master, from_=0, to=self.delayto, length=700, resolution=self.delayres, orient=HORIZONTAL, 
			variable=self.delay_value, label=self.label_txt3, font=normal_font, bg=bg_color, fg=fg_color)
		self.delayslider.set(10)
		if self.delay_true == True:
			self.delayslider.grid(row=self.rownum+2, columnspan=self.colspan, column=self.colnum, sticky=self.stickdir, padx="0", pady="10")

		if dev_mode and type_selected == True:
			self.showbtn = tk.Button(self.master, text='Show slider values', font=normal_font, bg=bg_color, fg=fg_color, command=self.show_values)
			self.showbtn.grid(row=self.rownum+3, columnspan=1, column=self.colnum, padx="7", pady="5", sticky="w")

	def show_values(self):
		# print(self.durslider.get(), self.freslider.get(), self.delayslider.get())
		# return(self.durslider.get(), self.freslider.get(), self.delayslider.get())
		global dur_val, fre_val, delay_val
		dur_val = self.durslider.get()
		fre_val = self.freslider.get()
		delay_val = self.delayslider.get()
		return(dur_val, fre_val, delay_val)

	def __str__(self):
		return f"{self.durslider.get()} {self.freslider.get()} {self.delayslider.get()}"

class SaveBtn: # master, rownum, colnum, colspan, command
	# class variables (attributes)
	bg_color = bg_color

	def __init__(self, master, rownum, colnum, colspan, command):
		self.master = master
		self.rownum = rownum
		self.colnum = colnum
		self.colspan = colspan
		self.command = command

		self.save_btn = tk.Button(self.master, text='Save', font=("Ubuntu", 15), width=5, height=1,
			bg=self.bg_color, fg=fg_color, highlightcolor=fg_color, command=self.command)
		self.save_btn.grid(row=rownum, columnspan=colspan, column=colnum, padx="7", pady="5", sticky="")

# home button to appear after saving
class HomeBtn(): # master, rownum, colnum, colspan
	def __init__(self, master, rownum, colnum, colspan):
		self.master = master
		self.rownum = rownum
		self.colnum = colnum
		self.colspan = colspan
		self.command = raise_main_set

		# Read the Image
		if dark_mode == True:
			self.home_img = Image.open(resource_path("assets\\home-icon-dark.png"))
		else:
			self.home_img = Image.open(resource_path("assets\\home-icon-light.png"))
		# Resize the image using resize() method
		self.resized_image = self.home_img.resize((50, 50))
		self.img = ImageTk.PhotoImage(self.resized_image)
		self.img_widget = tk.Button(self.master, image=self.img, bg=bg_color, command=self.command)
		self.img_widget.image = self.img
		self.img_widget.grid(row=self.rownum, columnspan=self.colspan, column=self.colnum, sticky="", padx="3", pady="1")

class CreateToolTip(object): #stackoverflow.com/questions/3221956/how-do-i-display-tooltips-in-tkinter
    """
    create a tooltip for a given widget
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 100     #miliseconds
        self.wraplength = 180   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background="#ffffff", relief='solid', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()

# set functions
# general settings
def toggle_bool(value):
	value = not value
	print(value)
	return value

def clear_widgets(root):
	# select all frame widgets and delete them
	for frame in root.winfo_children():
		frame.destroy()

def all_set_changed():
	global all_changed
	if all([schedule_changed, wp_changed, led_changed, fan_changed, cam_changed, atmos_changed]) == True:
		print("all settings changed")
		# logf.write("GUI: All settings changed\n")
		all_changed = True
	else:
		print("not all settings changed")
		#global all_changed
		all_changed = False
	set_preview_btn()

def set_preview_btn():
	MyButton.bg_color=bg_color	
	if all_changed == True:
		set_preview_btn = MyButton("Preview Settings", ("Ubuntu", 22), 0, 24, 6, 3, 2, "sw", lambda:load_set_preview_frame())
	else:
		set_preview_btn = MyButton("Preview Settings", ("Ubuntu", 22), 0, 24, 6, 3, 2, "sw", lambda:load_set_preview_frame()) #"disabled"


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
def test_camera():
	print("*click*")
	arduino.write(bytes('C', 'utf-8')) # take picture and save it
	logf.write("GUI: Camera tested\n")

def test_atmos():
	print("read atmos")
	arduino.write(bytes('A', 'utf-8')) # take atmos reading and save it
	logf.write("GUI: Atmospheric sensor tested\n")

def test_pump():
	print("pump")
	arduino.write(bytes('P', 'utf-8')) # pump some water and shake leaves
	logf.write("GUI: Water pump tested\n")

def test_fan():
	print("fan running")
	arduino.write(bytes('F', 'utf-8')) # turn on the fan for a little bit
	logf.write("GUI: Fan tested\n")

# LED test = test_LED()

# send settings setup
array = np.array([1, 2, "f", 4, 5, 6, 7, 8, 9])

# Convert array to a C-style string
c_array = ", ".join(map(str, array))
# c_array_string = f"int myArray[] = {{ {c_array} }};\n" # default
c_array_string = f"int array = {{ {c_array} }};\n"
c_array_string += f"const int myArraySize = {len(array)};\n"

# functions for raising frames
global previous_frame, current_frame
previous_frame = f"none"
current_frame = f"{settings_frame}"

def back_func():
	previous_frame.tkraise()

def raise_main_set():
	global previous_frame, current_frame
	previous_frame = f"{current_frame}"
	print(previous_frame)
	current_frame = f"{settings_frame}"
	print(current_frame)
	settings_frame.tkraise()
	#data_results_frame.destroy()
	for frame in root.winfo_children():
		if isinstance(frame, tk.Toplevel):
			print(frame)

def raise_wp_set():
	global previous_frame, current_frame
	previous_frame = f"{current_frame}"
	print(previous_frame)
	current_frame = f"w_pump_settings_frame"
	print(current_frame)
	w_pump_settings_frame.tkraise()

def raise_led_set():
	global previous_frame, current_frame
	previous_frame = f"{current_frame}"
	current_frame = f"led_settings_frame"
	led_settings_frame.tkraise()

def raise_fan_set():
	global previous_frame, current_frame
	previous_frame = f"{current_frame}"
	current_frame = f"fan_settings_frame"
	fan_settings_frame.tkraise()

def raise_cam_set():
	global previous_frame, current_frame
	previous_frame = f"{current_frame}"
	current_frame = f"camera_settings_frame"
	camera_settings_frame.tkraise()

def raise_atmos_set():
	global previous_frame, current_frame
	previous_frame = f"{current_frame}"
	current_frame = f"atmos_sensor_frame"
	atmos_sensor_frame.tkraise()

def raise_data_results():
	global previous_frame, current_frame
	previous_frame = f"{current_frame}"
	current_frame = f"data_results_frame"
	data_results_frame.tkraise()

def raise_log_frame():
	global previous_frame, current_frame
	previous_frame = f"{current_frame}"
	current_frame = f"log_frame"
	log_frame.tkraise()

# defining button bar on top
def load_menu(): 
	# clear_widgets()
	menu.tkraise()
	# prevent widgets from modifying the frame
	menu.grid_propagate(False)

	# create back button widget to go back to main settings
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
		command=back_func  #lambda:raise_main_set()
		).grid(row=0, column=0, sticky="w", padx="5", pady="3") # row: across, column: vertical

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

	"""
	image = Image.open(resource_path("assets\\night-mode-dark.png"))
	# Resize the image using resize() method
	resize_image = image.resize((30, 30))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Button(menu, image=logo_img, bg=menu_bg_color, command=lambda:toggle_dark(dark_mode))
	logo_widget.image = logo_img
	#logo_widget.grid(row=0, columnspan=1, column=8, sticky="e", padx="3", pady="1")
	"""
	# print("loaded menu")

def load_settings_frame():
	#findard()
	set_theme()
	all_set_changed()

	global previous_frame, current_frame
	previous_frame = f"{current_frame}"
	current_frame = f"settings_frame"
	print(current_frame)

	# clear_widgets(settings_frame)
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
	image = Image.open(resource_path("assets\\NanoLabs_logo.png"))
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(settings_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	settings_title = Label(settings_frame, text = "Main Settings", font=title_font, bg=bg_color, fg=fg_color)
	settings_title.grid(row=0, columnspan=3, column=1, padx="8", pady="5")

	# Arduino connection indicator
	ard_connect_frame = tk.Frame(settings_frame, highlightbackground="grey", highlightthickness=1, width=150, height=100, bg=bg_color)
	ard_connect_frame.grid(row=0, columnspan=3, column=3, sticky="e", padx="10", pady="10")

	ard_title = Label(ard_connect_frame, text = "Arduino", font=normal_font, bg=bg_color, fg=fg_color)
	ard_title.grid(row=0, columnspan=3, column=0, padx="15", pady="1")

	# Refresh btn
	if dark_mode:
		rfrimage = Image.open(resource_path("assets\\refresh_dark.png"))
	else:
		rfrimage = Image.open(resource_path("assets\\refresh.png"))
	# Resize the image using resize() method
	resize_rfrimage = rfrimage.resize((30, 30))
	rfr_img = ImageTk.PhotoImage(resize_rfrimage)
	def rfr_indicator():
		findard()
		#if len(port) > 1:
			#rfr_widget.grid(row=0, columnspan=1, column=2, sticky="se", padx="0", pady="0")
	rfr_widget = tk.Button(ard_connect_frame, image=rfr_img, bg=bg_color, fg=fg_color, cursor="hand2", relief=FLAT, command=rfr_indicator())
	rfr_widget.image = rfr_img
	if len(port) > 1:
		rfr_widget.grid(row=0, columnspan=1, column=2, sticky="se", padx="0", pady="0")

	port_title = Label(ard_connect_frame, text = f"Port: {port}", font=normal_font, bg=bg_color, fg=fg_color)
	port_title.grid(row=1, columnspan=3, column=0, padx="15", pady="1")

	# Add start and end calendars
	global dates
	dates = []
	global datesard
	datesard = []
	def sel_date():
		global dates
		dates = []
		global datesard
		datesard = []
		dates.append(end_cal.get_date())
		dates.append(start_cal.get_date())
		datesard.append(end_cal.get_date())
		datesard.append(start_cal.get_date())
		print(f"Experiment will run from {dates[1]} - {dates[0]}")
		logf.write(f"GUI: Experiment will run from {dates[1]} - {dates[0]}\n")
		# schedule = dates[1] + "\n" + dates[0]
		MyButton.bg_color="green"
		select_sch_btn = MyButton("Select Schedule", ("Ubuntu", 15), 1, 19, 6, 2, 1, "", lambda:sel_date())
		global schedule_changed
		schedule_changed = True
		all_set_changed()
		return dates

	schedule_label = Label(settings_frame, text="Schedule", font=("Ubuntu", 18), bg=bg_color, fg=fg_color)
	schedule_label.grid(row=1, columnspan=1, column=2, sticky="n", padx="8", pady="5")

	start_label = Label(settings_frame, text="Start Date:", font=normal_font, bg=bg_color, fg=fg_color)
	start_label.grid(row=1, columnspan=2, column=1, padx="8", pady="5")

	start_cal = Calendar(settings_frame, selectmode='day',
			year=cur_year, month=cur_month,
			day=cur_day, mindate=datetime.date(year=cur_year, month=cur_month, day=cur_day), 
			date_pattern="mm-dd-yy", font=calender_font) # date yyyy/mm/dd (no starting zeros)
	start_cal.grid(row=2, columnspan=2, column=1, padx="8", pady="5", sticky="")

	end_label = Label(settings_frame, text="End Date:", font=normal_font, bg=bg_color, fg=fg_color)
	end_label.grid(row=1, columnspan=2, column=2, padx="8", pady="5")

	end_cal = Calendar(settings_frame, selectmode='day',
			year=cur_year, month=cur_month,
			day=cur_day+1, mindate=datetime.date(year=cur_year, month=cur_month, day=cur_day), 
			date_pattern="mm-dd-yy", font=calender_font)
	end_cal.grid(row=2, columnspan=2, column=2, padx="8", pady="5", sticky="")

	for c in components:
		global cmdlist
		comp_btns = components.copy()
		rownum = 4
		colnum = 1

		while comp_btns:
			# btntext, rownum, columnnum, command
			MainBtns(comp_btns[0], rownum, colnum, raise_wp_set) #cmdlist[0]
			del comp_btns[0]
			#del cmdlist[0]
			colnum += 1
			if colnum >= 4:
				rownum += 1
				colnum = 1

	select_sch_btn = MyButton("Select Schedule", ("Ubuntu", 15), 1, 19, 6, 2, 1, "", lambda:sel_date())
	global all_changed
	set_preview_btn()

	if beta == True:
		beta_btn = MyButton("Rate your experience", ("Ubuntu", 9), 0, 19, 7, 0, 2, "sw", lambda:openbetaform())
	version_label = Label(settings_frame, text=f"Version {vernum}", font=("Ubuntu", 9), bg=bg_color, fg=fg_color)
	version_label.grid(row=6, columnspan=1, column=0, sticky="sw")

	# settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
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
	image = Image.open(resource_path("assets\\NanoLabs_logo.png"))
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(w_pump_settings_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	w_pump_title = Label(w_pump_settings_frame, text = "Water Pump Settings", font=title_font, bg=bg_color, fg=fg_color)
	w_pump_title.grid(row=0, columnspan=8, column=1, padx="8", pady="5")

	if dev_mode == True:
		# master, rownum, columnnum, colspan, stickdir, command
		testbtn1 = TestButton(w_pump_settings_frame, 1, 1, 1, "w", lambda:test_pump())

	# setup sliders
	Sliders.dur_true = True
	Sliders.dur_unit = "seconds"
	Sliders.durto = 20
	Sliders.durres = 1
	# load sliders
	# master, rownum, colnum, stickdir, command
	sliders1 = Sliders(w_pump_settings_frame, hardware, 2, 1, "w", Sliders.show_values)

	def save_wp_set():
		# print(sliders1)
		print(sliders1.show_values())
		global dur_val, fre_val, delay_val
		global wp_dur, wp_fre, wp_delay
		wp_dur = dur_val
		wp_fre = fre_val
		wp_delay = delay_val
		print(wp_dur, wp_fre, wp_delay)
		# f.write(str(sliders1))
		# f.write("\n")
		SaveBtn.bg_color = "green"
		savebtn1 = SaveBtn(w_pump_settings_frame, 5, 1, 16, save_wp_set)
		homebtn1 = HomeBtn(w_pump_settings_frame, 5, 3, 1) # master, rownum, colnum, colspan
		logf.write("GUI: Water pump settings set\n")
		global wp_changed
		wp_changed = True
		all_set_changed()

	# master, rownum, colnum, colspan, command
	savebtn1 = SaveBtn(w_pump_settings_frame, 5, 1, 16, save_wp_set) # fix command

	w_pump_set = [50, 5, 'd/w'] #"50mL", "5d/w"

	# set frame in window
	# w_pump_settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
	# print("H2O pump settings loaded")

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

	# slider current value
	current_value = tk.DoubleVar()
	value_label = 0

	def get_current_value():
		return '{:.2f}'.format(current_value.get())

	def slider_changed():
	    # value_label.configure(text=get_current_value())
	    # ser.write(get_current_value()) # relace with send brightness to Arduino
		# arduino.write(bytes(get_current_value(), 'utf-8'))  # Convert to bytes
		print('brightness', get_current_value())

	# set colors for default color buttons
	led_bg = "#ECECEC"
	red_fg = "#DC143C"
	orange_fg = "#834e02"
	yellow_fg = "#787934"
	green_fg = "green"
	blue_fg = "blue"
	purple_fg = "purple"

	def test_LED():
		print("LED on")
		arduino.write(bytes('L', 'utf-8'))
		logf.write("GUI: LED tested\n")

	def redLED():
		global rgb_code, rgb_color
		rgb_code = "220, 20, 60"
		rgb_color = "#DC143C"
		led_color_box.config(bg=rgb_color, fg=rgb_color)
		led_color_box.grid(rowspan=3, row=2, columnspan=1, column=13, padx="8", pady="5", sticky="w")

	def orangeLED():
		global rgb_code, rgb_color
		rgb_code = "242, 140, 40"
		rgb_color = "#F28C28"
		led_color_box.config(bg=rgb_color, fg=rgb_color)
		led_color_box.grid(rowspan=3, row=2, columnspan=1, column=13, padx="8", pady="5", sticky="w")

	def yellowLED():
		global rgb_code, rgb_color
		rgb_code = "253, 218, 13"
		rgb_color = "#FDDA0D"
		led_color_box.config(bg=rgb_color, fg=rgb_color)
		led_color_box.grid(rowspan=3, row=2, columnspan=1, column=13, padx="8", pady="5", sticky="w")

	def greenLED():
		global rgb_code, rgb_color
		rgb_code = "34, 139, 34"
		rgb_color = "#228B22"
		led_color_box.config(bg=rgb_color, fg=rgb_color)
		led_color_box.grid(rowspan=3, row=2, columnspan=1, column=13, padx="8", pady="5", sticky="w")

	def blueLED():
		global rgb_code, rgb_color
		rgb_code = "0, 150, 255"
		rgb_color = "#0096FF"
		led_color_box.config(bg=rgb_color, fg=rgb_color)
		led_color_box.grid(rowspan=3, row=2, columnspan=1, column=13, padx="8", pady="5", sticky="w")

	def purpleLED():
		global rgb_code, rgb_color
		rgb_code = "191, 64, 191"
		rgb_color = "#BF40BF"
		led_color_box.config(bg=rgb_color, fg=rgb_color)
		led_color_box.grid(rowspan=3, row=2, columnspan=1, column=13, padx="8", pady="5", sticky="w")

	def PARTYLED():
		# arduino.write(bytes("ROYGBPROYGBPROYGBPROYGBP", 'utf-8'))
		time.sleep(0.05)
		load_error()

	def clearLED():
		arduino.write(bytes('CC', 'utf-8'))

	# Read the Image
	image = Image.open(resource_path("assets\\NanoLabs_logo.png"))
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(led_settings_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	led_settings_title = Label(led_settings_frame, text = "LED Settings", font=title_font, bg=bg_color, fg=fg_color)
	led_settings_title.grid(row=0, columnspan=12, column=1, padx="8", pady="5")

	if dev_mode == True:
		# master, rownum, columnnum, colspan, stickdir, command
		testbtn2 = TestButton(led_settings_frame, 1, 1, 1, "w", lambda:test_LED())

	# setup sliders
	Sliders.dur_true = True
	Sliders.dur_unit = "minutes"
	Sliders.durto = 360
	Sliders.durres = 10
	# load sliders
	# master, rownum, colnum, stickdir, command
	sliders2 = Sliders(led_settings_frame, hardware, 2, 1, "w", Sliders.show_values)

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
		).grid(row=2, column=10, sticky="n", padx="5", pady="3")

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
		).grid(row=2, column=11, sticky="n", padx="5", pady="3")

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
		).grid(row=2, column=12, sticky="n", padx="5", pady="3")

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
		).grid(row=2, column=13, sticky="n", padx="5", pady="3")

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
		).grid(row=2, column=14, sticky="n", padx="5", pady="3")

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
		).grid(row=2, column=15, sticky="n", padx="5", pady="3")
	"""
	# create clear color button widget
	tk.Button(
		led_settings_frame,
		text="Clear",
		font=normal_font,
		height=("0"),
		width=("7"),
		bg=bg_color,
		fg=fg_color,
		cursor="hand2",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		command=clearLED
		).grid(row=2, column=16, sticky="n", padx="5", pady="3")
	"""
	# create PARTY color button widget
	tk.Button(
		led_settings_frame,
		text="PARTY",
		font=("Ubuntu", 1),
		height=("0"),
		width=("4"),
		bg=bg_color,
		fg=fg_color,
		cursor="hand1",
		activebackground=act_bg_color,
		activeforeground=act_fg_color,
		command=PARTYLED
		).grid(row=2, columnspan=1, column=12, sticky="wn", padx="5", pady="3")

	# RGB color picker
	global rgb_code, rgb_color
	rgb_code = "191, 64, 191"
	rgb_color = "#7714b9"
	def choose_color(value):
		# variable to store hexadecimal code of color
		global rgb_code, rgb_color
		color_code = colorchooser.askcolor(title ="Choose color", initialcolor="#7714b9")
		rgb_color = color_code[1]
		rgb_code = color_code[0]
		print(rgb_code, rgb_color)
		led_color_box.config(bg=rgb_color, fg=rgb_color)
		led_color_box.grid(rowspan=3, row=2, columnspan=1, column=13, padx="8", pady="5", sticky="w")

	# button to open color picker
	color_btn = tk.Button(led_settings_frame,text = 'Select precise color', font=normal_font, bg=bg_color, fg=fg_color, command = lambda:choose_color(rgb_code))
	color_btn.grid(rowspan=2, row=2, columnspan=2, column=12, padx="10", pady="10", sticky="")

	# box of selected color
	led_color_label = tk.Label(led_settings_frame, bg=bg_color, fg=fg_color, text = f"Color: ", font=(normal_font))
	led_color_label.grid(rowspan=3, row=2, columnspan=1, column=12, padx="8", pady="5", sticky="e")
	led_color_box = tk.Button(
		led_settings_frame,
		text="B",
		font=("Ubuntu", 10),
		height=("0"),
		width=("3"),
		bg=rgb_color,
		fg=rgb_color,
		relief=FLAT,
		activebackground=act_bg_color,
		activeforeground=act_bg_color)
	led_color_box.grid(rowspan=3, row=2, columnspan=1, column=13, padx="8", pady="5", sticky="w")

	# label for brightness slider
	slider_label = tk.Label(
    	led_settings_frame,
    	text='Brightness',
    	font=normal_font,
    	bg=bg_color,
		fg=fg_color
	).grid(rowspan=2, row=3, columnspan=8, column=10, sticky="", padx="0", pady="0")

	# brightness slider  # highlightbackground="#ffffff"
	led_slider = Scale(led_settings_frame, from_=0, to=250, length=570, resolution=10, orient=HORIZONTAL,
		variable=current_value, bg=bg_color, fg=fg_color)
	led_slider.set(200)
	led_slider.grid(rowspan=1, row=4, columnspan=8, column=10, sticky="s")

	# save button using classes
	def save_led_set():
		print(sliders2.show_values())
		global dur_val, fre_val, delay_val
		global led_dur, led_fre, led_delay
		led_dur = dur_val
		led_fre = fre_val
		led_delay = delay_val
		print(led_dur, led_fre, led_delay)
		global led_brightness
		led_brightness = led_slider.get()
		# f.write(str(sliders2))
		# f.write("\n")
		print(rgb_code)
		# f.write(str(rgb_code))
		# f.write("\n")
		print(led_brightness)
		SaveBtn.bg_color = "green"
		savebtn2 = SaveBtn(led_settings_frame, 5, 1, 16, save_led_set)
		homebtn2 = HomeBtn(led_settings_frame, 5, 11, 1) # master, rownum, colnum, colspan
		logf.write("GUI: LED settings set\n")
		global led_changed
		led_changed = True
		all_set_changed()

	# master, rownum, colnum, colspan, command
	savebtn2 = SaveBtn(led_settings_frame, 5, 1, 16, save_led_set)

	LED_set = ['red', 105] #"red", "105"

	# set frame in window
	# led_settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
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
	image = Image.open(resource_path("assets\\NanoLabs_logo.png"))
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(fan_settings_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	fan_settings_title = Label(fan_settings_frame, text = "Fan Settings", font=title_font, bg=bg_color, fg=fg_color)
	fan_settings_title.grid(row=0, columnspan=8, column=1, padx="8", pady="5")

	if dev_mode == True:
		# master, rownum, columnnum, colspan, stickdir, command
		testbtn3 = TestButton(fan_settings_frame, 1, 1, 3, "w", lambda:test_fan())

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
		fg=fg_color)
	slider_label.grid(row=2, columnspan=8, column=9, sticky="n")

	fan_strength_slider = Scale(fan_settings_frame, from_=0, to=100, length=755, resolution=10, orient=HORIZONTAL, variable=current_value, 
		font=normal_font, bg=bg_color, fg=fg_color)
	fan_strength_slider.set(70)
	fan_strength_slider.grid(row=2, columnspan=8, column=9, sticky="s")

	# setup sliders
	Sliders.dur_true = True
	Sliders.durto = 360
	# load sliders
	# master, rownum, colnum, stickdir, command
	sliders3 = Sliders(fan_settings_frame, hardware, 2, 1, "w", Sliders.show_values)

	def save_fan_set():
		print(sliders3.show_values())
		global dur_val, fre_val, delay_val
		global fan_dur, fan_fre, fan_delay
		fan_dur = dur_val
		fan_fre = fre_val
		fan_delay = delay_val
		print(fan_dur, fan_fre, fan_delay)
		global fan_str
		fan_str = fan_strength_slider.get()
		print(fan_str)
		SaveBtn.bg_color = "green"
		savebtn3 = SaveBtn(fan_settings_frame, 5, 1, 16, save_fan_set)
		homebtn3 = HomeBtn(fan_settings_frame, 5, 10, 1) # master, rownum, colnum, colspan
		logf.write("GUI: Fan settings set\n")
		global fan_changed
		fan_changed = True
		all_set_changed()

	# master, rownum, colnum, colspan, command
	savebtn3 = SaveBtn(fan_settings_frame, 5, 1, 16, save_fan_set)

	fan_set = [90, 30, 3, 'd/w'] #"90%", "30m/3d/w"

	# set frame in window
	# fan_settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
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
	image = Image.open(resource_path("assets\\NanoLabs_logo.png"))
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(camera_settings_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	cam_settings_title = Label(camera_settings_frame, text = "Timelapse Intervals", font=title_font, bg=bg_color, fg=fg_color)
	cam_settings_title.grid(row=0, columnspan=8, column=1, padx="8", pady="5")
	
	if dev_mode == True:
		# master, rownum, columnnum, colspan, stickdir, command
		testbtn4 = TestButton(camera_settings_frame, 1, 1, 1, "w", lambda:test_camera())

	# setup sliders
	Sliders.dur_true = False
	# load sliders
	# master, rownum, colnum, stickdir, command
	sliders4 = Sliders(camera_settings_frame, hardware, 2, 1, "w", Sliders.show_values)

	def save_cam_set():
		print(sliders4.show_values())
		global dur_val, fre_val, delay_val
		global cam_dur, cam_fre, cam_delay
		cam_dur = dur_val
		cam_fre = fre_val
		cam_delay = delay_val
		print(cam_dur, cam_fre, cam_delay)
		SaveBtn.bg_color = "green"
		savebtn4 = SaveBtn(camera_settings_frame, 5, 1, 16, save_cam_set)
		homebtn4 = HomeBtn(camera_settings_frame, 5, 3, 1) # master, rownum, colnum, colspan
		logf.write("GUI: Timelapse intervals set\n")
		global cam_changed
		cam_changed = True
		all_set_changed()

	# master, rownum, colnum, colspan, command
	savebtn4 = SaveBtn(camera_settings_frame, 5, 1, 16, save_cam_set)

	cam_set = [1, 'w'] #"1/w"

	# set frame in window
	# camera_settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
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
	image = Image.open(resource_path("assets\\NanoLabs_logo.png"))
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(atmos_sensor_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	atmos_sensor_title = Label(atmos_sensor_frame, text = "Atmospheric Sensor Settings", font=title_font, bg=bg_color, fg=fg_color)
	atmos_sensor_title.grid(row=0, columnspan=8, column=1, padx="8", pady="5")

	if dev_mode == True:
		# master, rownum, columnnum, colspan, stickdir, command
		testbtn5 = TestButton(atmos_sensor_frame, 1, 1, 1, "w", lambda:test_atmos())

	# setup sliders
	Sliders.dur_true = False
	# load sliders
	# master, rownum, colnum, stickdir, command
	sliders5 = Sliders(atmos_sensor_frame, hardware, 1, 1, "w", Sliders.show_values)

	if atmos_changed == False:
		# global gas_val
		# global temp_val
		# global humid_val
		# global bar_press_val
		gas_val = False
		temp_val = False
		humid_val = False
		bar_press_val = False
	else:
		print("nah uh")

	# checkbox made with class
	class MyCheckboxs: # master, rownum, columnnum, rowspan
		def __init__(self, master, rownum, columnnum, rowspan):
			self.checktext1 = "Gases (VOCs)"
			self.checktext2 = "Temperature"
			self.checktext3 = "Humidity"
			self.checktext4 = "Barometric Pressure"
			self.gas_bool = tk.BooleanVar()
			#self.gas_bool.set(False)
			self.temp_bool = tk.BooleanVar()
			#self.temp_bool.set(False)
			self.humid_bool = tk.BooleanVar()
			#self.humid_bool.set(False)
			self.bar_press_bool = tk.BooleanVar()
			#self.bar_press_bool.set(False)

			self.master = master
			self.rownum = rownum
			self.columnnum = columnnum
			self.rowspan = rowspan

			self.checkbox1 = tk.Checkbutton(master, text=self.checktext1, variable=self.gas_bool, command=self.on_change)
			self.checkbox1.config(bg=bg_color, fg=fg_color, font=normal_font, selectcolor=bg_color, relief="raised", padx=10, pady=5)

			self.gas_ttp = CreateToolTip(self.checkbox1, "Read Volatile Organic Compounds (toxic gases)")

			self.checkbox2 = tk.Checkbutton(master, text=self.checktext2, variable=self.temp_bool, command=self.on_change)
			self.checkbox2.config(bg=bg_color, fg=fg_color, font=normal_font, selectcolor=bg_color, relief="raised", padx=10, pady=5)

			self.checkbox3 = tk.Checkbutton(master, text=self.checktext3, variable=self.humid_bool, command=self.on_change)
			self.checkbox3.config(bg=bg_color, fg=fg_color, font=normal_font, selectcolor=bg_color, relief="raised", padx=10, pady=5)

			self.checkbox4 = tk.Checkbutton(master, text=self.checktext4, variable=self.bar_press_bool, command=self.on_change)
			self.checkbox4.config(bg=bg_color, fg=fg_color, font=normal_font, selectcolor=bg_color, relief="raised", padx=10, pady=5)
			
			self.checkbox1.grid(row=self.rownum, column=self.columnnum, rowspan=self.rowspan, padx="7", pady="5", sticky="s")
			self.checkbox2.grid(row=self.rownum+1, column=self.columnnum, rowspan=self.rowspan, padx="7", pady="5", sticky="n")
			self.checkbox3.grid(row=self.rownum+1, column=self.columnnum, rowspan=self.rowspan+1, padx="7", pady="5", sticky="")
			self.checkbox4.grid(row=self.rownum+2, column=self.columnnum, rowspan=self.rowspan, padx="7", pady="5", sticky="s")

		def on_change(self):
			#if checktext1:
			#print(f"{self.checktext1} = {self.gas_bool.get()}")
			self.gas_bool.get()
			self.temp_bool.get()
			self.humid_bool.get()
			self.bar_press_bool.get()
			self.send_checks()

		def send_checks(self):
			global gas_val
			global temp_val
			global humid_val
			global bar_press_val

			gas_val = self.gas_bool.get()
			temp_val = self.temp_bool.get()
			humid_val = self.humid_bool.get()
			bar_press_val = self.bar_press_bool.get()
			print(gas_val)
			print(temp_val)
			print(humid_val)
			print(bar_press_val)

	# master, checktext, rownum, columnnum, rowspan
	checkboxs1 = MyCheckboxs(atmos_sensor_frame, 2, 6, 1)

	reading_checks_label = tk.Label(atmos_sensor_frame, text = "What do you want to record?", font=("Ubuntu", 14), bg=bg_color, fg=fg_color, padx="8", pady="8")
	reading_checks_label.grid(rowspan=2, row=1, column=6, sticky="", padx="8", pady="8")

	def save_atmos_set():
		print(sliders5.show_values())
		global dur_val, fre_val, delay_val
		global atmos_dur, atmos_fre, atmos_delay
		atmos_dur = dur_val
		atmos_fre = fre_val
		atmos_delay = delay_val
		print(atmos_dur, atmos_fre, atmos_delay)
		print(gas_val)
		print(temp_val)
		print(humid_val)
		print(bar_press_val)
		SaveBtn.bg_color = "green"
		savebtn5 = SaveBtn(atmos_sensor_frame, 6, 1, 15, save_atmos_set)
		homebtn5 = HomeBtn(atmos_sensor_frame, 6, 4, 2) # master, rownum, colnum, colspan
		logf.write("GUI: Atmospheric sensor settings set\n")
		global atmos_changed
		atmos_changed = True
		all_set_changed()

	# master, rownum, colnum, colspan, command
	savebtn5 = SaveBtn(atmos_sensor_frame, 6, 1, 15, save_atmos_set)

	atmos_sen_set = [2, 'd'] #"2/d"

	# set frame in window
	# atmos_sensor_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
	# print("atmos sensor frame loaded")

def load_data_results_frame(): 
	# clear_widgets(settings_frame)
	# raise data results frame to the top
	data_results_frame.tkraise()
	# prevent widgets from modifying the frame
	data_results_frame.grid_propagate(False)

	# Read the Image
	image = Image.open(resource_path("assets\\NanoLabs_logo.png"))
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(data_results_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	data_r_title = Label(data_results_frame, text = "Data Results", font=title_font, bg=bg_color, fg=fg_color)
	data_r_title.grid(row=0, columnspan=8, column=1, padx="8", pady="5")

	# graph
	def load_graph(): 

	    # the figure that will contain the plot 
	    fig = Figure(figsize = (6, 4), dpi = 100) 

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

	logf.write("GUI: error 404 (page doesn't exist)\n")

	e404_title = Label(error_404_frame, bg="grey", text = "error_404", font=("Ubuntu", 60))
	e404_title.pack(fill="both", expand=True, side="top")

	# Read the Image
	image = Image.open(resource_path("assets\\error_404.png"))
	# Resize the image using resize() method
	resize_image = image.resize((200, 200))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(error_404_frame, image=logo_img, bg="grey")
	logo_widget.image = logo_img
	logo_widget.pack()

	e404_title2 = Label(error_404_frame, bg="grey", text = "Sorry! That page doesn't exist.", font=("Ubuntu", 30))
	e404_title2.pack(fill="both", expand=True, side="bottom")

	# set frame in window
	error_404_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
	# print("error 404")

def load_log_frame(): # log of what is happening on Arduino right now
	# clear_widgets()
	log_frame.tkraise()
	# prevent widgets from modifying the frame
	log_frame.grid_propagate(False)

	# Read the Image
	image = Image.open(resource_path("assets\\NanoLabs_logo.png"))
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(log_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	log_title = Label(log_frame, text = "Log", font=title_font, bg=bg_color, fg=fg_color)
	log_title.grid(row=0, columnspan=8, column=1, padx="8", pady="5")

	# log file display ## https://stackoverflow.com/questions/43480156/how-to-display-a-files-text-in-python-tkinter-text-widget
	# text box ## https://www.geeksforgeeks.org/python-tkinter-text-widget
	log = tk.Text(log_frame, bg=bg_color, fg=fg_color, bd=1, font=("Ubuntu", 12), 
		width=80, height=22, state="normal") # yscrollcommand

	def load_log():
		global log_new
		raise_log_frame()
		logf.flush()
		with open("data\\log.txt", "r") as file:
			# file.seek(0)
			data = file.read()

			if log_new == True:  # First time loading the log
				log.insert(tk.INSERT, data)
				log_new = False  # Mark as loaded
			else:
				log.delete("1.0", tk.END)
				log.insert(tk.INSERT, data)
	load_log()
	log.grid(row=1, columnspan=4, column=1, sticky="nsew", padx="8", pady="5")

	upd_btn = tk.Button(log_frame,text = 'Update', font=normal_font, bg=bg_color, fg=fg_color, command = lambda:load_log())
	upd_btn.grid(rowspan=1, row=2, columnspan=4, column=1, padx="8", pady="5", sticky="")

	"""
	image = Image.open(resource_path("assets\\log.jpg"))
	# Resize the image using resize() method
	resize_image = image.resize((1000, 700))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(log_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	# logo_widget.grid(row=1, column=8, sticky="nsew", padx="8", pady="5")
	"""

	# set frame in window
	log_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
	# print("log loaded")

class SetPreview: # command
	# class variables (attributes)
	master = set_preview_frame
	rownum = 1
	colnum = 1
	colspan = 2

	def __init__(self):
		# all_set_changed()
		if all([schedule_changed, wp_changed, led_changed, fan_changed, cam_changed, atmos_changed]) == True:
			print("all settings changed")
			logf.write("GUI: All settings changed\n")
			all_changed = True
		else:
			print("Not all settings changed")
			all_changed = False

		self.bg_color = bg_color

		if all_changed == True:
			# pull all values
			print("All user set values")
			logf.write("GUI: Using all custom values")
			self.dates = dates
			self.datesard = datesard
			self.wp_dur = wp_dur
			self.wp_fre = wp_fre
			self.wp_delay = wp_delay

			self.led_dur = led_dur
			self.led_fre = led_fre
			self.led_delay = led_delay
			self.rgb_code = rgb_code
			self.rgb_color = rgb_color
			self.led_brightness = led_brightness

			self.fan_dur = fan_dur
			self.fan_fre = fan_fre
			self.fan_delay = fan_delay
			self.fan_str = fan_str

			self.cam_fre = cam_fre
			self.cam_delay = cam_delay

			self.atmos_fre = atmos_fre
			self.atmos_delay = atmos_delay
			self.gas_val = gas_val
			self.temp_val = temp_val
			self.humid_val = humid_val
			self.bar_press_val = bar_press_val

		elif all_changed == False:
			# set all values or set unselected values
			print("Using better one-click")
			logf.write("GUI: Using better one-click\n")
			self.predates = []
			self.pre_start_date = f"{cur_year}-{cur_month}-{cur_day}"
			self.pre_end_date = f"{cur_year}-{cur_month}-{cur_day+1}"
			self.predates.append(self.pre_end_date)
			self.predates.append(self.pre_start_date) #2025/3/12
			self.predatesard = []
			self.pre_start_date_ard = f"{cur_day}"
			self.pre_end_date_ard = f"{cur_day+1}"
			self.predatesard.append(self.pre_end_date_ard)
			self.predatesard.append(self.pre_start_date_ard) #2025/3/12
			if len(dates) == 2:
				self.dates = dates
				self.datesard = datesard
			else:
				self.dates = self.predates
				self.datesard = self.predatesard
			#finally:
				#raise Exception("Please select your schedule\n")
				#self.dates = self.predates
				#self.datesard = self.predatesard
			
			try:
				self.wp_dur = wp_dur
				self.wp_fre = wp_fre
				self.wp_delay = wp_delay
			except NameError:
				#logf.write("GUI: Please select water pump settings\n")
				#raise Exception("Select water pump settings")
				self.wp_dur = 8
				self.wp_fre = 2
				self.wp_delay = 720
				
			try:
				self.led_dur = led_dur
				self.led_fre = led_fre
				self.led_delay = led_dur
				self.rgb_code = rgb_code
				self.rgb_color = rgb_color
				self.led_brightness = led_brightness
			except NameError:
				#logf.write("GUI: Please select LED settings\n")
				#raise Exception("Select LED settings")
				self.led_dur = 360
				self.led_fre = 2
				self.led_delay = 360
				self.rgb_code = "191, 64, 191"
				self.rgb_color = "#7714b9"
				self.led_brightness = 200
				
			try:
				self.fan_dur = fan_dur
				self.fan_fre = fan_fre
				self.fan_delay = fan_delay
				self.fan_str = fan_str
			except NameError:
				#logf.write("GUI: Please select fan settings\n")
				#raise Exception("Select LED settings")
				self.fan_dur = 60
				self.fan_fre = 6
				self.fan_delay = 60
				self.fan_str = 50
				
			try:
				self.cam_fre = cam_fre
				self.cam_delay = cam_delay
			except NameError:
				#logf.write("GUI: Please select camera settings\n")
				#raise Exception("Select LED settings")
				self.cam_fre = 1
				self.cam_delay = 720
				
			try:
				self.atmos_fre = atmos_fre
				self.atmos_delay = atmos_delay
				self.gas_val = gas_val
				self.temp_val = temp_val
				self.humid_val = humid_val
				self.bar_press_val = bar_press_val
			except NameError:
				#logf.write("GUI: Please select atmospheric sensor settings\n")
				#raise Exception("Select LED settings")
				self.atmos_fre = 4
				self.atmos_delay = 180
				self.gas_val = False
				self.temp_val = True
				self.humid_val = True
				self.bar_press_val = False

		# vars for arduino
		self.start = 1 # symbol to tell ard to start putting it into array
		self.wp_dur_ard = self.wp_dur * 1000 # convert seconds to millisecs
		if all_changed:
			self.all_sets = f"""{self.start}\n{self.datesard[1]}\n{self.datesard[0]}\n{self.wp_dur_ard}\n{self.wp_fre}\n{self.wp_delay}\n{self.led_dur}\n{self.led_fre}\n{self.led_delay}\n{self.rgb_code}\n{self.led_brightness}\n{self.fan_dur}\n{self.fan_fre}\n{self.fan_delay}\n{self.fan_str}\n{self.cam_fre}\n{self.cam_delay}\n{self.atmos_fre}\n{self.atmos_delay}\n{int(self.gas_val)}\n{int(self.temp_val)}\n{int(self.humid_val)}\n{int(self.bar_press_val)}\n"""
		else:
			self.all_sets = f"""{self.start}\n{self.predatesard[1]}\n{self.predatesard[0]}\n{self.wp_dur_ard}\n{self.wp_fre}\n{self.wp_delay}\n{self.led_dur}\n{self.led_fre}\n{self.led_delay}\n{self.rgb_code}\n{self.led_brightness}\n{self.fan_dur}\n{self.fan_fre}\n{self.fan_delay}\n{self.fan_str}\n{self.cam_fre}\n{self.cam_delay}\n{self.atmos_fre}\n{self.atmos_delay}\n{int(self.gas_val)}\n{int(self.temp_val)}\n{int(self.humid_val)}\n{int(self.bar_press_val)}\n"""

		# define graphical elements
		self.start_date_title = tk.Label(self.master, bg=bg_color, fg=fg_color, text = f"Start Date:\n{self.dates[1]}", font=("Ubuntu", 14))
		self.end_date_title = tk.Label(self.master, bg=bg_color, fg=fg_color, text = f"End Date:\n{self.dates[0]}", font=("Ubuntu", 14))

		self.wp_preview_frame = tk.Frame(self.master, highlightbackground="grey", highlightthickness=1, width=200, height=300, bg=bg_color)
		self.wp_preview_title = tk.Button(self.wp_preview_frame, bg=bg_color, fg=fg_color, text ="Water Pump", font=("Ubuntu", 14), pady="0", relief=FLAT, command=raise_wp_set)
		self.wp_long_label = tk.Label(self.wp_preview_frame, bg=bg_color, fg=fg_color, text=f"How long: {self.wp_dur} (seconds)", font=(normal_font)) #normal_font(12 vs 14)
		self.wp_fre_label = tk.Label(self.wp_preview_frame, bg=bg_color, fg=fg_color, text=f"How often: {self.wp_fre} (in 24h period)", font=(normal_font))
		self.wp_delay_label = tk.Label(self.wp_preview_frame, bg=bg_color, fg=fg_color, text=f"How much delay: {self.wp_delay} (minutes)", font=(normal_font))
		self.wp_filler_label = tk.Label(self.wp_preview_frame, bg=bg_color, fg=bg_color, text="How much delay: ", font=(normal_font)) # dummy text to fill space
		self.wp_filler_label2 = tk.Label(self.wp_preview_frame, bg=bg_color, fg=bg_color, text="How much delay: ", font=(normal_font))

		self.led_preview_frame = tk.Frame(self.master, highlightbackground="grey", highlightthickness=1, width=200, height=300, bg=bg_color)
		self.led_preview_title = tk.Button(self.led_preview_frame, bg=bg_color, fg=fg_color, text = "LED", font=("Ubuntu", 14), pady="0", relief=FLAT, command=raise_led_set)
		self.led_long_label = tk.Label(self.led_preview_frame, bg=bg_color, fg=fg_color, text = f"How long: {self.led_dur} (minutes)", font=(normal_font))
		self.led_fre_label = tk.Label(self.led_preview_frame, bg=bg_color, fg=fg_color, text = f"How often: {self.led_fre} (in 24h period)", font=(normal_font))
		self.led_delay_label = tk.Label(self.led_preview_frame, bg=bg_color, fg=fg_color, text = f"How much delay: {self.led_delay} (minutes)", font=(normal_font))
		self.led_color_label = tk.Label(self.led_preview_frame, bg=bg_color, fg=fg_color, text = f"Color: {self.rgb_code}", font=(normal_font))
		# create led color box widget
		self.led_color_box = tk.Button(
			self.led_preview_frame,
			text="B",
			font=("Ubuntu", 10),
			height=("0"),
			width=("3"),
			bg=self.rgb_color,
			fg=self.rgb_color,
			relief=FLAT,
			activebackground=act_bg_color,
			activeforeground=act_bg_color)	
		self.led_bright_label = tk.Label(self.led_preview_frame, bg=bg_color, fg=fg_color, text = f"Brightness: {self.led_brightness}%", font=(normal_font))	

		self.fan_preview_frame = tk.Frame(self.master, highlightbackground="grey", highlightthickness=1, width=200, height=300, bg=bg_color)
		self.fan_preview_title = tk.Button(self.fan_preview_frame, bg=bg_color, fg=fg_color, text = "Fan", font=("Ubuntu", 14), pady="0", relief=FLAT, command=raise_fan_set)
		self.fan_long_label = tk.Label(self.fan_preview_frame, bg=bg_color, fg=fg_color, text = f"How long: {self.fan_dur} (minutes)", font=(normal_font))
		self.fan_fre_label = tk.Label(self.fan_preview_frame, bg=bg_color, fg=fg_color, text = f"How often: {self.fan_fre} (in 24h period)", font=(normal_font))
		self.fan_delay_label = tk.Label(self.fan_preview_frame, bg=bg_color, fg=fg_color, text = f"How much delay: {self.fan_delay} (minutes)", font=(normal_font))
		self.fan_strength_label = tk.Label(self.fan_preview_frame, bg=bg_color, fg=fg_color, text = f"Fan Strength: {self.fan_str}%", font=(normal_font))

		self.cam_preview_frame = tk.Frame(self.master, highlightbackground="grey", highlightthickness=1, width=200, height=300, bg=bg_color)
		self.cam_preview_title = tk.Button(self.cam_preview_frame, bg=bg_color, fg=fg_color, text = "Timelapse", font=("Ubuntu", 14), pady="0", relief=FLAT, command=raise_cam_set)
		#self.cam_long_label = tk.Label(self.cam_preview_frame, bg=bg_color, fg=fg_color, text = f"How long: {cam_dur} (minutes)", font=(normal_font))
		self.cam_fre_label = tk.Label(self.cam_preview_frame, bg=bg_color, fg=fg_color, text = f"How often: {self.cam_fre} (in 24h period)", font=(normal_font))
		self.cam_delay_label = tk.Label(self.cam_preview_frame, bg=bg_color, fg=fg_color, text = f"How much delay: {self.cam_delay} (minutes)", font=(normal_font))

		self.atmos_preview_frame = tk.Frame(self.master, highlightbackground="grey", highlightthickness=1, width=200, height=300, bg=bg_color)
		self.atmos_preview_title = tk.Button(self.atmos_preview_frame, bg=bg_color, fg=fg_color, text = "Atmospheric Sensor", font=("Ubuntu", 14), pady="0", relief=FLAT, command=raise_atmos_set)
		#self.atmos_long_label = tk.Label(self.atmos_preview_frame, bg=bg_color, fg=fg_color, text = f"How long: {atmos_dur} (minutes)", font=(normal_font))
		self.atmos_fre_label = tk.Label(self.atmos_preview_frame, bg=bg_color, fg=fg_color, text = f"How often: {self.atmos_fre} (in 24h period)", font=(normal_font))
		self.atmos_delay_label = tk.Label(self.atmos_preview_frame, bg=bg_color, fg=fg_color, text = f"How much delay: {self.atmos_delay} (minutes)", font=(normal_font))
		self.atmos_check1_label = tk.Label(self.atmos_preview_frame, bg=bg_color, fg=fg_color, text = f"Gas (VOCs) = {self.gas_val}", font=(normal_font))
		self.atmos_check2_label = tk.Label(self.atmos_preview_frame, bg=bg_color, fg=fg_color, text = f"Temperature = {self.temp_val}", font=(normal_font))
		self.atmos_check3_label = tk.Label(self.atmos_preview_frame, bg=bg_color, fg=fg_color, text = f"Humidity = {self.humid_val}", font=(normal_font))
		self.atmos_check4_label = tk.Label(self.atmos_preview_frame, bg=bg_color, fg=fg_color, text = f"Barometric Pressure = {self.bar_press_val}", font=(normal_font))


		# create cancel button widget
		self.cancel_btn = tk.Button(
			self.master,
			text="Cancel",
			font=("Ubuntu", 14),
			height=("2"),
			width=("17"),
			bg=bg_color,
			fg=fg_color,
			cursor="hand2",
			activebackground=act_bg_color,
			activeforeground=act_fg_color,
			command=lambda:raise_main_set()) # command to go back to main screen

		def send_settings():
			# print(repr(all_set))
			# arduino.write(bytes(str(repr(all_set)), 'utf-8'))
			# something to check Arduino got it
			self.confirm_btn.config(bg="green")
			self.confirm_btn.grid(rowspan=1, row=self.rownum+19, columnspan=3, column=7, sticky="e", padx="5", pady="3")
			f.write(self.all_sets)
			arduino.write(repr(self.all_sets))
			print("experiment started")
			logf.write("GUI: Custom experiment started\n")
			#f.close()
			#logf.close()

		# create confirm button widget
		self.confirm_btn = tk.Button(
			self.master,
			text="Send settings to your NanoLab", 
			font=("Ubuntu", 14),
			height=("2"),
			width=("25"),
			bg=self.bg_color,
			fg=fg_color,
			cursor="hand2",
			activebackground=act_bg_color,
			activeforeground=act_fg_color,
			command=send_settings) # command to send settings to NanoLab
		
		# place everything
		self.start_date_title.grid(columnspan=1, row=1, column=2, sticky="ns", padx="8", pady="5")
		self.end_date_title.grid(columnspan=1, row=1, column=8, sticky="ns", padx="8", pady="5")

		self.wp_preview_frame.grid(rowspan=6, columnspan=self.colspan+1, row=3, column=1, sticky="nesw", padx="8", pady="5")
		self.wp_preview_title.grid(row=self.rownum, columnspan=self.colspan, column=self.colnum, padx="8", pady="5")
		self.wp_long_label.grid(row=self.rownum+1, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		self.wp_fre_label.grid(row=self.rownum+2, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		self.wp_delay_label.grid(row=self.rownum+3, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		self.wp_filler_label.grid(row=self.rownum+4, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		self.wp_filler_label2.grid(row=self.rownum+5, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")

		self.led_preview_frame.grid(rowspan=6, columnspan=self.colspan+1, row=3, column=4, sticky="nesw", padx="8", pady="5")
		self.led_preview_title.grid(row=self.rownum, columnspan=self.colspan, column=self.colnum+3, padx="8", pady="5")
		self.led_long_label.grid(row=self.rownum+1, columnspan=self.colspan, column=self.colnum+3, sticky="w", padx="10", pady="2")
		self.led_fre_label.grid(row=self.rownum+2, columnspan=self.colspan, column=self.colnum+3, sticky="w", padx="10", pady="2")
		self.led_delay_label.grid(row=self.rownum+3, columnspan=self.colspan, column=self.colnum+3, sticky="w", padx="10", pady="2")
		self.led_color_label.grid(row=self.rownum+4, columnspan=self.colspan, column=self.colnum+3, sticky="w", padx="10", pady="2")
		self.led_color_box.grid(row=self.rownum+4, columnspan=1, column=self.colnum+4, sticky="", padx="5", pady="3")
		self.led_bright_label.grid(row=self.rownum+5, columnspan=self.colspan, column=self.colnum+3, sticky="w", padx="10", pady="2")

		self.fan_preview_frame.grid(rowspan=6, columnspan=self.colspan+1, row=10, column=1, sticky="nesw", padx="8", pady="5")
		self.fan_preview_title.grid(row=self.rownum+6, columnspan=self.colspan, column=self.colnum, padx="8", pady="5")
		self.fan_long_label.grid(row=self.rownum+7, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		self.fan_fre_label.grid(row=self.rownum+8, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		self.fan_delay_label.grid(row=self.rownum+9, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		self.fan_strength_label.grid(row=self.rownum+10, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		
		self.cam_preview_frame.grid(rowspan=6, columnspan=self.colspan+1, row=10, column=4, sticky="nesw", padx="8", pady="5")
		self.cam_preview_title.grid(row=self.rownum+6, columnspan=self.colspan, column=self.colnum+3, padx="8", pady="5")
		#self.cam_long_label.grid(row=self.rownum+7, columnspan=self.colspan, column=self.colnum+3, sticky="w", padx="10", pady="2")
		self.cam_fre_label.grid(row=self.rownum+8, columnspan=self.colspan, column=self.colnum+3, sticky="w", padx="10", pady="2")
		self.cam_delay_label.grid(row=self.rownum+9, columnspan=self.colspan, column=self.colnum+3, sticky="w", padx="10", pady="2")

		self.atmos_preview_frame.grid(rowspan=13, columnspan=self.colspan+1, row=3, column=7, sticky="nesw", padx="8", pady="5")
		self.atmos_preview_title.grid(row=self.rownum, columnspan=self.colspan, column=self.colnum, padx="8", pady="5")
		#self.atmos_long_label.grid(row=self.rownum+1, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		self.atmos_fre_label.grid(row=self.rownum+2, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		self.atmos_delay_label.grid(row=self.rownum+3, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		self.atmos_check1_label.grid(row=self.rownum+4, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		self.atmos_check2_label.grid(row=self.rownum+5, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		self.atmos_check3_label.grid(row=self.rownum+6, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		self.atmos_check4_label.grid(row=self.rownum+7, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		
		self.cancel_btn.grid(rowspan=1, row=self.rownum+19, columnspan=3, column=self.colnum, sticky="w", padx="5", pady="3")
		self.confirm_btn.grid(rowspan=1, row=self.rownum+19, columnspan=3, column=7, sticky="e", padx="5", pady="3")

def load_set_preview_frame(): # preview of settings
	# all_set_changed()
	# clear_widgets()
	set_preview_frame.tkraise()
	# prevent widgets from modifying the frame
	set_preview_frame.grid_propagate(False)

	# Read the Image
	image = Image.open(resource_path("assets\\NanoLabs_logo.png"))
	# Resize the image using resize() method
	resize_image = image.resize((125, 125))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Label(set_preview_frame, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.grid(row=0, column=0, sticky="w", padx="8", pady="5")

	set_preview_title = Label(set_preview_frame, text = "Settings Preview", font=title_font, bg=bg_color, fg=fg_color)
	set_preview_title.grid(row=0, columnspan=8, column=1, padx="8", pady="5")

	all_set_preview = SetPreview()

	# set frame in window
	set_preview_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
	# print("settings preview loaded")

# run main app
load_menu()
load_w_pump_settings_frame()
load_led_settings_frame()
load_fan_settings_frame()
load_camera_settings_frame()
load_atmos_sensor_frame()
load_settings_frame()
root.mainloop()

# =======================
# main window end
# =======================