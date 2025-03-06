
# Code writen by Asher Powell at Warren Tech North
# Version 1.6a

# import dependencies
import tkinter as tk
# import tkinter.ttk as ttk
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
import numpy as np

# set fonts
pyglet.font.add_file("fonts/Ubuntu-Bold.ttf")
normal_font = ("Ubuntu", 12)
big_font = ("Ubuntu", 24)
title_font = ("Ubuntu", 46)
calender_font = ("Arial", 10)

"""
# Arduino Stuff
# open serial port
arduino = serial.Serial(port="COM4", baudrate=9600, timeout=0.1)
# check which port was really used
print(arduino.name)

# close serial port from https://stackoverflow.com/questions/35235436/python-arduino-prototyping-api-v2-closing-serial-port
def closeport(): # closes port if currently open
    ser = serial.Serial(usbport) 
    if ser.isOpen() == True:
        ser.close()

# closeport()
"""

# set starting variables
dev_mode = True # if True will show log button and test buttons
beta = True # enable beta testing form button
dark_mode = False # changes colors
comp_count = 5 # number of components
type_selected = False
box_type = ""

if dark_mode == False:
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
	menu_bg_color = "#000000"
	menu_fg_color = "#ffffff"
	menu_act_bg_color = "#ffffff"
	bg_color = "#000000"
	fg_color = "#ffffff"
	act_bg_color = "#808080"
	act_fg_color = "#ffffff"

# ttk.Style().theme_use('black') https://stackoverflow.com/questions/24367710/how-do-i-change-the-overall-theme-of-a-tkinter-application?rq=3
def toggle_dark(value): # maybe use stackoverflow.com/questions/60595078/implementing-dark-mode-with-on-off-function-in-simple-python-tkinter-program
	value = not value
	print(value)
	return value
	color_mode_switch()
# dark_mode = toggle_bool(dark_mode)
print(dark_mode)
def color_mode_switch():
	if dark_mode == False:
		# set normal colors
		menu_bg_color = "#000000"
		menu_fg_color = "#ffffff"
		menu_act_bg_color = "#000000"
		bg_color = "#ffffff"
		fg_color = "#000000"
		act_bg_color = "#ffffff"
		act_fg_color = "#808080"
		return(menu_bg_color, menu_fg_color, menu_act_bg_color, bg_color, fg_color, act_bg_color, act_fg_color)
	else:
		# set dark mode colors
		menu_bg_color = "#000000"
		menu_fg_color = "#ffffff"
		menu_act_bg_color = "#ffffff"
		bg_color = "#000000"
		fg_color = "#ffffff"
		act_bg_color = "#808080"
		act_fg_color = "#ffffff"
		return(menu_bg_color, menu_fg_color, menu_act_bg_color, bg_color, fg_color, act_bg_color, act_fg_color)
color_mode_switch()

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
	welcome_label = Label(setup1_frame, text="Welcome to your NanoLab!", font=("Ubuntu-Bold", 20), bg=bg_color, fg=fg_color)
	welcome_label.grid(row=0, columnspan=8, column=0, sticky="")

	welcome_label = Label(setup1_frame, text="Pick Your Version", font=("Ubuntu-Bold", 18), bg=bg_color, fg=fg_color)
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
	hydrofuge_label = Label(setup1_frame, text="HydroFuge", font=normal_font, bg=bg_color, fg=fg_color)
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
	hydrofuge_label = Label(setup1_frame, text="Universal (Coming Soon)", font=normal_font, bg=bg_color, fg=fg_color)
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

# lists
w_pump_set = [] #"50mL", "5d/w"
LED_set = [] #"red", "105"
fan_set = [] #"90%", "30m/3d/w"
cam_set = [] #"1/w"
atmos_sen_set = [] #"2/d"
all_set = f"{w_pump_set = } {LED_set = } {fan_set = } {cam_set = } {atmos_sen_set = }"
schedule_changed = False
wp_changed = False
led_changed = False
fan_changed = False
cam_changed = False
atmos_changed = False

f = open("C:/Users/rcpow/Documents/GitHub/NanoLab-GUI/NanoLab-GUI/Arduino/basic_hydrofuge_schedule/array_for_arduino.h", "w")
# f.write(all_set + '\n')
f.write("test \n")
# f.write("rehehe2 \n")

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
settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
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

# slider
class Sliders: # master, hardware, rownum, colnum, stickdir, command
	# class variables (attributes)
	value_label = 0
	value_label2 = 0
	value_label3 = 0
	durto = 360
	freto = 24
	delayto = 360

	def __init__(self, master, hardware, rownum, colnum, stickdir, command):
		self.master = master
		self.hardware = hardware
		self.label_txt = f"How long do you want {hardware} to run? (minutes)"
		self.label_txt2 = f"How many times should {hardware} run? (24h period)"
		self.label_txt3 = f"How much delay do you want between runs? (minutes)"
		self.rownum = rownum
		self.colnum = colnum
		self.colspan = 3
		self.stickdir = stickdir
		self.command = command
		self.current_value = tk.DoubleVar()
		self.current_value2 = tk.DoubleVar()
		self.current_value3 = tk.DoubleVar()

		self.durslider = Scale(self.master, from_=0, to=self.durto, length=700, resolution=10, orient=HORIZONTAL, 
			variable=self.current_value, label=self.label_txt, font=normal_font, bg=bg_color, fg=fg_color)
		self.durslider.set(10)
		self.durslider.grid(row=self.rownum, columnspan=self.colspan, column=self.colnum, sticky=self.stickdir, padx="0", pady="10")

		self.freslider = Scale(self.master, from_=0, to=self.freto, length=700, resolution=1, orient=HORIZONTAL, 
			variable=self.current_value2, label=self.label_txt2, font=normal_font, bg=bg_color, fg=fg_color)
		self.freslider.set(10)
		self.freslider.grid(row=self.rownum+1, columnspan=self.colspan, column=self.colnum, sticky=self.stickdir, padx="0", pady="10")

		self.delayslider = Scale(self.master, from_=0, to=self.delayto, length=700, resolution=10, orient=HORIZONTAL, 
			variable=self.current_value3, label=self.label_txt3, font=normal_font, bg=bg_color, fg=fg_color)
		self.delayslider.set(10)
		self.delayslider.grid(row=self.rownum+2, columnspan=self.colspan, column=self.colnum, sticky=self.stickdir, padx="0", pady="10")

		self.showbtn = tk.Button(self.master, text='Show slider values', font=normal_font, bg=bg_color, fg=fg_color, command=self.show_values)
		self.showbtn.grid(row=self.rownum+3, columnspan=1, column=self.colnum, padx="7", pady="5", sticky="w")

	# class methods
	def show_values(self):
		print(self.durslider.get(), self.freslider.get(), self.delayslider.get())
		return(self.durslider.get(), self.freslider.get(), self.delayslider.get())

	def __str__(self):
		return f"{self.durslider.get()} {self.freslider.get()} {self.delayslider.get()}"

class SaveBtn: # master, rownum, colnum, colspan, command
	# class variables (attributes)

	def __init__(self, master, rownum, colnum, colspan, command):
		self.master = master
		self.rownum = rownum
		self.colnum = colnum
		self.colspan = colspan
		self.command = command

		self.save_btn = tk.Button(self.master, text='Save', font=normal_font, bg=bg_color, fg=fg_color, command=self.command)
		self.save_btn.grid(row=rownum, columnspan=colspan, column=colnum, padx="7", pady="5", sticky="")

class SetPreview: # command
	# class variables (attributes)
	master = set_preview_frame
	rownum = 1
	colnum = 1
	colspan = 2
	# schedule
	# led_color = rgb_code
	# led_bright = brightness
	# fan_strength = fan_str
	# gas_check = gas_check
	# temp_check = temp_check
	# humid_check = humid_check
	# bar_press_check = bar_press_check

	def __init__(self):
		# self.command = command


		self.start_date_title = tk.Label(self.master, bg=bg_color, fg=fg_color, text = "Start Date", font=("Ubuntu", 14))
		self.start_date_label = tk.Label(self.master, bg=bg_color, fg=fg_color, text = "3/6/2025", font=normal_font)
		self.end_date_title = tk.Label(self.master, bg=bg_color, fg=fg_color, text = "End Date", font=("Ubuntu", 14))
		self.end_date_label = tk.Label(self.master, bg=bg_color, fg=fg_color, text = "3/7/2025", font=normal_font)

		self.wp_preview_frame = tk.Frame(self.master, highlightbackground="grey", highlightthickness=1, width=200, height=300, bg=bg_color)
		self.wp_preview_title = tk.Label(self.wp_preview_frame, bg=bg_color, fg=fg_color, text = "Water Pump", font=("Ubuntu", 14))
		self.wp_long_label = tk.Label(self.wp_preview_frame, bg=bg_color, fg=fg_color, text = "How long: ", font=(normal_font)) #normal_font(12 vs 14)
		self.wp_fre_label = tk.Label(self.wp_preview_frame, bg=bg_color, fg=fg_color, text = "How often: ", font=(normal_font))
		self.wp_delay_label = tk.Label(self.wp_preview_frame, bg=bg_color, fg=fg_color, text = "How much delay: ", font=(normal_font))
		self.wp_filler_label = tk.Label(self.wp_preview_frame, bg=bg_color, fg=bg_color, text = "How much delay: ", font=(normal_font))
		self.wp_filler_label2 = tk.Label(self.wp_preview_frame, bg=bg_color, fg=bg_color, text = "How much delay: ", font=(normal_font))

		self.led_preview_frame = tk.Frame(self.master, highlightbackground="grey", highlightthickness=1, width=200, height=300, bg=bg_color)
		self.led_preview_title = tk.Label(self.led_preview_frame, bg=bg_color, fg=fg_color, text = "LED", font=("Ubuntu", 14))
		self.led_long_label = tk.Label(self.led_preview_frame, bg=bg_color, fg=fg_color, text = "How long: ", font=(normal_font)) #normal_font(12 vs 14)
		self.led_fre_label = tk.Label(self.led_preview_frame, bg=bg_color, fg=fg_color, text = "How often: ", font=(normal_font))
		self.led_delay_label = tk.Label(self.led_preview_frame, bg=bg_color, fg=fg_color, text = "How much delay: ", font=(normal_font))
		self.led_color_label = tk.Label(self.led_preview_frame, bg=bg_color, fg=fg_color, text = f"Color: #834e02", font=(normal_font))
		# create led color box widget
		self.led_color_box = tk.Button(
			self.led_preview_frame,
			text="B",
			font=("Ubuntu", 10),
			height=("0"),
			width=("3"),
			bg="#834e02",
			fg="#834e02",
			cursor="hand2",
			activebackground=act_bg_color,
			activeforeground=act_bg_color)	
		self.led_bright_label = tk.Label(self.led_preview_frame, bg=bg_color, fg=fg_color, text = f"Brightness: 50%", font=(normal_font))	

		self.fan_preview_frame = tk.Frame(self.master, highlightbackground="grey", highlightthickness=1, width=200, height=300, bg=bg_color)
		self.fan_preview_title = tk.Label(self.fan_preview_frame, bg=bg_color, fg=fg_color, text = "Fan", font=("Ubuntu", 14))
		self.fan_long_label = tk.Label(self.fan_preview_frame, bg=bg_color, fg=fg_color, text = "How long: ", font=(normal_font)) #normal_font(12 vs 14)
		self.fan_fre_label = tk.Label(self.fan_preview_frame, bg=bg_color, fg=fg_color, text = "How often: ", font=(normal_font))
		self.fan_delay_label = tk.Label(self.fan_preview_frame, bg=bg_color, fg=fg_color, text = "How much delay: ", font=(normal_font))
		self.fan_strength_label = tk.Label(self.fan_preview_frame, bg=bg_color, fg=fg_color, text = f"Fan Strength: 30%", font=(normal_font))

		self.cam_preview_frame = tk.Frame(self.master, highlightbackground="grey", highlightthickness=1, width=200, height=300, bg=bg_color)
		self.cam_preview_title = tk.Label(self.cam_preview_frame, bg=bg_color, fg=fg_color, text = "Camera", font=("Ubuntu", 14))
		self.cam_long_label = tk.Label(self.cam_preview_frame, bg=bg_color, fg=fg_color, text = "How long: ", font=(normal_font)) #normal_font(12 vs 14)
		self.cam_fre_label = tk.Label(self.cam_preview_frame, bg=bg_color, fg=fg_color, text = "How often: ", font=(normal_font))
		self.cam_delay_label = tk.Label(self.cam_preview_frame, bg=bg_color, fg=fg_color, text = "How much delay: ", font=(normal_font))

		self.atmos_preview_frame = tk.Frame(self.master, highlightbackground="grey", highlightthickness=1, width=200, height=300, bg=bg_color)
		self.atmos_preview_title = tk.Label(self.atmos_preview_frame, bg=bg_color, fg=fg_color, text = "Atmospheric Sensor", font=("Ubuntu", 14))
		self.atmos_long_label = tk.Label(self.atmos_preview_frame, bg=bg_color, fg=fg_color, text = "How long: ", font=(normal_font)) #normal_font(12 vs 14)
		self.atmos_fre_label = tk.Label(self.atmos_preview_frame, bg=bg_color, fg=fg_color, text = "How often: ", font=(normal_font))
		self.atmos_delay_label = tk.Label(self.atmos_preview_frame, bg=bg_color, fg=fg_color, text = "How much delay: ", font=(normal_font))
		self.atmos_check1_label = tk.Label(self.atmos_preview_frame, bg=bg_color, fg=fg_color, text = f"Gas (VOCs) = True", font=(normal_font))
		self.atmos_check2_label = tk.Label(self.atmos_preview_frame, bg=bg_color, fg=fg_color, text = f"Temperature = False", font=(normal_font))
		self.atmos_check3_label = tk.Label(self.atmos_preview_frame, bg=bg_color, fg=fg_color, text = f"Humidity = True", font=(normal_font))
		self.atmos_check4_label = tk.Label(self.atmos_preview_frame, bg=bg_color, fg=fg_color, text = f"Barometric Pressure = True", font=(normal_font))


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
			command=lambda:load_settings_frame) # command to go back to main screen

		# create confirm button widget
		self.confirm_btn = tk.Button(
			self.master,
			text="Confirm settings",
			font=("Ubuntu", 14),
			height=("2"),
			width=("17"),
			bg=bg_color,
			fg=fg_color,
			cursor="hand2",
			activebackground=act_bg_color,
			activeforeground=act_fg_color,
			command=send_settings) # command to send settings to NanoLab
		
		# place everything
		self.start_date_title.grid(columnspan=6, row=1, column=1, sticky="nesw", padx="8", pady="5")
		self.start_date_label.grid(columnspan=6, row=2, column=1, sticky="nesw", padx="8", pady="5")
		self.end_date_title.grid(columnspan=6, row=1, column=6, sticky="nesw", padx="8", pady="5")
		self.end_date_label.grid(columnspan=6, row=2, column=6, sticky="nesw", padx="8", pady="5")

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
		self.led_color_box.grid(row=self.rownum+4, columnspan=1, column=self.colnum+5, sticky="w", padx="5", pady="3")
		self.led_bright_label.grid(row=self.rownum+5, columnspan=self.colspan, column=self.colnum+3, sticky="w", padx="10", pady="2")

		self.fan_preview_frame.grid(rowspan=6, columnspan=self.colspan+1, row=10, column=1, sticky="nesw", padx="8", pady="5")
		self.fan_preview_title.grid(row=self.rownum+6, columnspan=self.colspan, column=self.colnum, padx="8", pady="5")
		self.fan_long_label.grid(row=self.rownum+7, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		self.fan_fre_label.grid(row=self.rownum+8, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		self.fan_delay_label.grid(row=self.rownum+9, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		self.fan_strength_label.grid(row=self.rownum+10, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		
		self.cam_preview_frame.grid(rowspan=6, columnspan=self.colspan+1, row=10, column=4, sticky="nesw", padx="8", pady="5")
		self.cam_preview_title.grid(row=self.rownum+6, columnspan=self.colspan, column=self.colnum+3, padx="8", pady="5")
		self.cam_long_label.grid(row=self.rownum+7, columnspan=self.colspan, column=self.colnum+3, sticky="w", padx="10", pady="2")
		self.cam_fre_label.grid(row=self.rownum+8, columnspan=self.colspan, column=self.colnum+3, sticky="w", padx="10", pady="2")
		self.cam_delay_label.grid(row=self.rownum+9, columnspan=self.colspan, column=self.colnum+3, sticky="w", padx="10", pady="2")

		self.atmos_preview_frame.grid(rowspan=13, columnspan=self.colspan+1, row=3, column=10, sticky="nesw", padx="8", pady="5")
		self.atmos_preview_title.grid(row=self.rownum, columnspan=self.colspan, column=self.colnum, padx="8", pady="5")
		self.atmos_long_label.grid(row=self.rownum+1, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		self.atmos_fre_label.grid(row=self.rownum+2, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		self.atmos_delay_label.grid(row=self.rownum+3, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		self.atmos_check1_label.grid(row=self.rownum+4, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		self.atmos_check2_label.grid(row=self.rownum+5, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		self.atmos_check3_label.grid(row=self.rownum+6, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		self.atmos_check4_label.grid(row=self.rownum+7, columnspan=self.colspan, column=self.colnum, sticky="w", padx="10", pady="2")
		
		self.cancel_btn.grid(rowspan=1, row=self.rownum+19, columnspan=3, column=self.colnum, sticky="w", padx="5", pady="3")
		self.confirm_btn.grid(rowspan=1, row=self.rownum+19, columnspan=3, column=self.colnum+9, sticky="e", padx="5", pady="3")

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
def test_camera():
	print("*click*")
	# arduino.write(bytes(str(repr(all_set)), 'utf-8')) # take picture and save it

def test_atmos():
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
	# print(repr(all_set))
	# arduino.write(bytes(str(repr(all_set)), 'utf-8'))
	# something to check Arduino got it
	f.write("send test\n")
	print("experiment started")

def clear_widgets(root):
	# select all frame widgets and delete them
	for frame in root.winfo_children():
		frame.destroy()

def raise_main_set():
	settings_frame.tkraise()

def toggle_bool(value):
	value = not value
	print(value)
	return value


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
		command=lambda:raise_main_set()
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

	# Read the Image
	image = Image.open("assets/night-mode.png")
	# Resize the image using resize() method
	resize_image = image.resize((30, 30))
	logo_img = ImageTk.PhotoImage(resize_image)
	logo_widget = tk.Button(menu, image=logo_img, bg="#ffffff", command=lambda:toggle_bool(dark_mode))
	logo_widget.image = logo_img
	logo_widget.grid(row=0, columnspan=1, column=8, sticky="e", padx="3", pady="1")

	# print("loaded menu")

def load_settings_frame():
	clear_widgets(settings_frame)
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

	settings_title = Label(settings_frame, text = "Main Settings", font=title_font, bg=bg_color, fg=fg_color)
	settings_title.grid(row=0, columnspan=3, column=1, padx="8", pady="5")

	# Add start and end calendars
	start_date = ""
	end_date = ""
	def sel_date():
		dates = []
		dates.append(end_cal.get_date())
		dates.append(start_cal.get_date())
		# print(f"Experiment will run from {dates[1]} - {dates[0]}")
		schedule = dates[1] + "\n" + dates[0]
		print(schedule)
		f.write(schedule)
		f.write("\n")
		schedule_changed = True

	schedule_label = Label(settings_frame, text="Schedule", font=("Ubuntu", 18), bg=bg_color, fg=fg_color)
	schedule_label.grid(row=1, columnspan=1, column=2, sticky="n", padx="8", pady="5")

	start_label = Label(settings_frame, text="Start Date:", font=normal_font, bg=bg_color, fg=fg_color)
	start_label.grid(row=1, columnspan=2, column=1, padx="8", pady="5")

	start_cal = Calendar(settings_frame, selectmode='day',
			year=cur_year, month=cur_month,
			day=cur_day, mindate=datetime.date(year=cur_year, month=cur_month, day=cur_day), font=calender_font) #date yyyy/mm/dd (no starting zeros)
	start_cal.grid(row=2, columnspan=2, column=1, padx="8", pady="5", sticky="")

	end_label = Label(settings_frame, text="End Date:", font=normal_font, bg=bg_color, fg=fg_color)
	end_label.grid(row=1, columnspan=2, column=2, padx="8", pady="5")

	end_cal = Calendar(settings_frame, selectmode='day',
			year=cur_year, month=cur_month,
			day=cur_day+1, mindate=datetime.date(year=cur_year, month=cur_month, day=cur_day), font=calender_font)
	end_cal.grid(row=2, columnspan=2, column=2, padx="8", pady="5", sticky="")

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
	image = Image.open("assets/NanoLabs_logo.png")
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

	# master, rownum, colnum, stickdir, command
	sliders1 = Sliders(w_pump_settings_frame, hardware, 2, 1, "w", Sliders.show_values)

	def save_wp_set():
		print(sliders1)
		f.write(str(sliders1))
		f.write("\n")
		wp_changed = True

	# master, rownum, colnum, colspan, command
	savebtn1 = SaveBtn(w_pump_settings_frame, 5, 1, 16, save_wp_set) # fix command

	w_pump_set = [50, 5, 'd/w'] #"50mL", "5d/w"

	# set frame in window
	w_pump_settings_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
	# print("H2O pump settings loaded")


# LED settings stuff
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

def clearLED():
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

	led_settings_title = Label(led_settings_frame, text = "LED Settings", font=title_font, bg=bg_color, fg=fg_color)
	led_settings_title.grid(row=0, columnspan=12, column=1, padx="8", pady="5")

	if dev_mode == True:
		# master, rownum, columnnum, colspan, stickdir, command
		testbtn2 = TestButton(led_settings_frame, 1, 1, 1, "w", lambda:test_LED())

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

	# create clear color button widget
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
		command=clearLED
		).grid(row=2, column=16, sticky="n", padx="5", pady="3")

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
	# global rgb_code
	rgb_code = 0
	def choose_color(value):
		# variable to store hexadecimal code of color
		color_code = colorchooser.askcolor(title ="Choose color", initialcolor="#7714b9")
		value = color_code[0]
		print(value)
		global rgb_code
		rgb_code = value
		return value
	# rgb_code = choose_color(rgb_code)

	# button to open color picker
	color_btn = tk.Button(led_settings_frame,text = 'Select precise color', font=normal_font, bg=bg_color, fg=fg_color, command = lambda:choose_color(rgb_code))
	color_btn.grid(row=2, columnspan=3, column=12, padx="8", pady="5", sticky="s")

	# label for brightness slider
	slider_label = tk.Label(
    	led_settings_frame,
    	text='Brightness',
    	font=normal_font,
    	bg=bg_color,
		fg=fg_color
	).grid(rowspan=2, row=2, columnspan=8, column=10, sticky="s", padx="0", pady="0")

	# brightness slider  # highlightbackground="#ffffff"
	led_slider = Scale(led_settings_frame, from_=0, to=250, length=570, resolution=10, orient=HORIZONTAL,
		variable=current_value, bg=bg_color, fg=fg_color)
	led_slider.set(200)
	led_slider.grid(rowspan=1, row=4, columnspan=8, column=10, sticky="n")

	# save button using classes
	def save_led_set(): # add more stuff
		print(sliders2)
		f.write(str(sliders2))
		f.write("\n")
		print(rgb_code)
		print("test")
		f.write(str(rgb_code))
		f.write("\n")
		led_changed = True

	# master, rownum, colnum, colspan, command
	savebtn2 = SaveBtn(led_settings_frame, 5, 1, 16, save_led_set)

	LED_set = ['red', 105] #"red", "105"

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
		fg=fg_color
	).grid(row=2, columnspan=8, column=9, sticky="n")

	fan_strength_slider = Scale(fan_settings_frame, from_=0, to=100, length=755, resolution=10, orient=HORIZONTAL, variable=current_value, bg=bg_color, fg=fg_color)
	fan_strength_slider.set(70)
	fan_strength_slider.grid(row=2, columnspan=8, column=9, sticky="s")

	# master, rownum, colnum, stickdir, command
	sliders3 = Sliders(fan_settings_frame, hardware, 2, 1, "w", Sliders.show_values)

	def save_fan_set(): # add more stuff
		print(sliders3)

	# master, rownum, colnum, colspan, command
	savebtn3 = SaveBtn(fan_settings_frame, 5, 1, 16, save_fan_set)

	fan_set = [90, 30, 3, 'd/w'] #"90%", "30m/3d/w"

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

	cam_settings_title = Label(camera_settings_frame, text = "Camera Intervals", font=title_font, bg=bg_color, fg=fg_color)
	cam_settings_title.grid(row=0, columnspan=8, column=1, padx="8", pady="5")
	
	if dev_mode == True:
		# master, rownum, columnnum, colspan, stickdir, command
		testbtn4 = TestButton(camera_settings_frame, 1, 1, 1, "w", lambda:take_picture())

	# master, rownum, colnum, stickdir, command
	sliders4 = Sliders(camera_settings_frame, hardware, 2, 1, "w", Sliders.show_values)
	
	def save_cam_set(): # add more stuff
		print(sliders4)
		cam_changed = True

	# master, rownum, colnum, colspan, command
	savebtn4 = SaveBtn(camera_settings_frame, 5, 1, 16, save_cam_set)

	cam_set = [1, 'w'] #"1/w"

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

	atmos_sensor_title = Label(atmos_sensor_frame, text = "Atmospheric Sensor Settings", font=title_font, bg=bg_color, fg=fg_color)
	atmos_sensor_title.grid(row=0, columnspan=8, column=1, padx="8", pady="5")

	if dev_mode == True:
		# master, rownum, columnnum, colspan, stickdir, command
		testbtn5 = TestButton(atmos_sensor_frame, 1, 1, 1, "w", lambda:take_atmos_reading())

	# master, rownum, colnum, stickdir, command
	sliders5 = Sliders(atmos_sensor_frame, hardware, 2, 1, "w", Sliders.show_values)

	# checkbox made with class
	class MyCheckbox: # master, checktext, rownum, columnnum, rowspan, stickdir
		def __init__(self, master, checktext, rownum, columnnum, rowspan, stickdir):
			self.master = master
			self.checkbox_value = tk.BooleanVar()
			self.checktext = checktext
			self.rownum = rownum
			self.columnnum = columnnum
			self.rowspan = rowspan
			self.stickdir = stickdir

			self.checkbox = tk.Checkbutton(master, text=self.checktext, variable=self.checkbox_value, command=self.on_change)
			self.checkbox.config(bg=bg_color, fg=fg_color, font=normal_font, selectcolor="white", relief="raised", padx=10, pady=5)
			self.checkbox.grid(row=self.rownum, column=self.columnnum, rowspan=self.rowspan, padx="7", pady="5", sticky=stickdir)

		def on_change(self):
			print(f"Record {self.checktext} = {self.checkbox_value.get()}")

	# master, checktext, rownum, columnnum, rowspan, stickdir
	gas_checkbox = MyCheckbox(atmos_sensor_frame, "Gas (VOCs)", 2, 6, 1, "n")
	temp_checkbox = MyCheckbox(atmos_sensor_frame, "Temperature", 2, 6, 2, "")
	humid_checkbox = MyCheckbox(atmos_sensor_frame, "Humidity", 3, 6, 2, "")
	press_checkbox = MyCheckbox(atmos_sensor_frame, "Barometric pressure", 4, 6, 2, "")

	def save_atmos_set(): # add more stuff
		print(sliders5)
		atmos_changed = True

	# master, rownum, colnum, colspan, command
	savebtn5 = SaveBtn(atmos_sensor_frame, 5, 1, 15, save_atmos_set)

	atmos_sen_set = [2, 'd'] #"2/d"

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

	# set frame in window
	error_404_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
	# print("error 404")

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

	log_title = Label(log_frame, text = "Log", font=title_font, bg=bg_color, fg=fg_color)
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

	set_preview_title = Label(set_preview_frame, text = "Settings Preview", font=title_font, bg=bg_color, fg=fg_color)
	set_preview_title.grid(row=0, columnspan=8, column=1, padx="8", pady="5")

	all_set_preview = SetPreview()

	# set frame in window
	set_preview_frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
	# print("settings preview loaded")

# run main app
load_menu()
load_settings_frame()
# f.close()
root.mainloop()

# main window end
# =======================