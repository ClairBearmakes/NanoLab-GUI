import tkinter as tk
from tkinter import ttk
import pyglet

# set fonts
pyglet.font.add_file("fonts/Ubuntu-Bold.ttf")
normal_font= ("Ubuntu", 12)
title_font= ("Ubuntu", 48)
calender_font= ("Arial", 10)

# set starting variables
dev_mode = True # if True will show log button and test buttons
beta = True
dark_mode = False
component_count = 5
type_selected = False
box_type = ""
menu_height = 55

if dark_mode == False: 
    # set normal colors
    menu_bg_color = "#000000"
    menu_fg_color = "#ffffff"
    menu_act_bg_color = "#000000"
    bg_color = "#ffffff"
    fg_color = "#000000"
    act_bg_color = "#ffffff"
    act_fg_color = "#808080"
else: # fix these
    # set dark mode colors
    menu_bg_color = "#ffffff"
    menu_fg_color = "#000000"
    menu_act_bg_color = "#ffffff"
    bg_color = "#000000"
    fg_color = "#ffffff"
    act_bg_color = "#808080"
    act_fg_color = "#ffffff"

"""
# fullscreen stuff https://stackoverflow.com/questions/7966119/display-fullscreen-mode-on-tkinter
self.attributes("-fullscreen", False)
self.state = False
self.tk.bind("<Escape>", self.toggle_fullscreen)
# self.tk.bind("<Escape>", self.end_fullscreen)
def toggle_fullscreen(self, event=None):
    self.state = not self.state  # Just toggling the boolean
    self.tk.attributes("-fullscreen", self.state)
    return "break"
"""

# TkClass example from https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes

class Setup(tk.Tk):
    def __init__(self, width, height, *args, **kwargs):
        # creating window
        tk.Tk.__init__(self, *args, **kwargs)

        # setting up window
        self.title("Universal NanoLab Settings")
        self.width = width 
        self.height = height
        self.geometry("%dx%d" % (self.width, self.height))
        self.attributes("-fullscreen", False)
        self.iconbitmap("assets/Universal logo.ico")
        self.configure(bg=bg_color)

        def frames():
            # creating a default frame
            frame = tk.Frame(self, width=self.width, height=self.height, bg=bg_color, highlightbackground="grey", highlightthickness=1)
            frame.grid(self, rowspan=4, columnspan=10, row=0, column=0, sticky="nesw")
        frames()

        """
        def FirstScreen():
            label = tk.Label(frame, bg=bg_color, text = "Preview Your Settings", font=title_font)
            label.grid(row=0, columnspan=8, column=1, padx="8", pady="5")
        FirstScreen()
        """

SetupApp = Setup(600, 550)
SetupApp.mainloop()

"""
class Framework(tk.Tk):
    def __init__(self, *args, **kwargs):
        # creating window
        tk.Tk.__init__(self, *args, **kwargs)

        # setting up window
        self.title("Universal NanoLab Settings")
        self.width = self.winfo_screenwidth() 
        self.height = self.winfo_screenheight()
        self.geometry("%dx%d" % (self.width, self.height))
        self.attributes("-fullscreen", False)
        self.iconbitmap("assets/Universal logo.ico")
        self.configure(bg=bg_color)

    class Frames(Framework, self):
        # attributes for frames
        def __init__(Framework, self):

            def frames():
                # creating a default frame
                frame = tk.Frame(self, width=self.width, height=self.height - menu_height, bg=bg_color, highlightbackground="grey", highlightthickness=1)
            frames()

            def MainScreen():
                label = tk.Label(frame, bg=bg_color, text = "Preview Your Settings", font=title_font)
                label.grid(row=0, columnspan=8, column=1, padx="8", pady="5")
                frame.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nesw")
        

# define objects and start app
# if __name__ == "__main__":
MainApp = Framework()
MainFrames = Framework.Frames()

MainApp.mainloop()

"""