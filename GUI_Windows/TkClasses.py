import tkinter as tk
# from tkinter import ttk
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

# example from https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes

class Framework(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) # set "root"
        # Adding a title to the window
        self.wm_title("Universal NanoLab Settings")
        # setting diamentions
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry("%dx%d" % (width, height))
        root.configure(bg=bg_color)
        root.iconbitmap("assets/Universal logo.ico")

        # creating a frame and assigning it to container
        container = tk.Frame(self, height=400, width=600)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (MainPage, SidePage, CompletionScreen):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(MainPage)