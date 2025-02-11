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

class Framework(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # setting up window
        self.title("Universal NanoLab Settings")
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry("%dx%d" % (width, height))
        # self.eval("tk::PlaceWindow . center")
        self.attributes("-fullscreen", False)
        self.iconbitmap("assets/Universal logo.ico")
        self.configure(bg=bg_color)

        # creating a frame to contain all other frames
        container = tk.Frame(self, width=width, height=height, bg=bg_color)
        # specifying the region where the frame is put into root
        container.grid(rowspan=4, columnspan=8, row=1, column=0, sticky="nsew")

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # create a dictionary of frames
        self.frames = {}
        # the frames themselves are created later but add the frames to the dictionary now
        for F in (MainPage, SecondPage): # add all classes for the frames
            frame = F(container, self)

            # the Framework class acts as the root window for the frames.
            self.frames[F] = frame
            frame.config(width=width, height=height - menu_height, bg=bg_color)
            frame.grid(row=1, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(MainPage)

    def show_frame(self, cont):
            frame = self.frames[cont]
            # raises the current frame to the top
            frame.tkraise()

class Menu(tk.Frame):
    def __init__(self, parent): #, controller
        tk.Frame.__init__(self, parent)
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, minsize=35)
        self.tkraise()
        self.grid_propagate(False)

        # add things into frame
        label = tk.Label(self, text="Menu")
        label.grid(row=0, column=0, sticky="w", padx="5", pady="3")

# make one of these for each page
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page")
        label.grid(row=2, column=0, sticky="w", padx="5", pady="3")

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = tk.Button(
            self,
            text="Go to the Second Page",
            command=lambda: controller.show_frame(SecondPage),
        )
        switch_window_button.grid(row=3, column=0, sticky="w", padx="5", pady="3")

class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Second Page")
        label.pack(padx=10, pady=10)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = tk.Button(
            self,
            text="Go back to the Main Page",
            command=lambda: controller.show_frame(MainPage),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

# define objects and start app
if __name__ == "__main__":
    Menu = Menu()
    Menu.mainloop()
    MainApp = Framework()
    MainApp.mainloop()


# example from https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes

"""class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Test Application")

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
        for F in (MainPage, SidePage, NextPage, CompletionScreen):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(MainPage)

    def show_frame(self, cont):
            frame = self.frames[cont]
            # raises the current frame to the top
            frame.tkraise()

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page")
        label.pack(padx=10, pady=10)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = tk.Button(
            self,
            text="Go to the Side Page",
            command=lambda: controller.show_frame(SidePage),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


class SidePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is the Side Page")
        label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Go to the Next Page",
            command=lambda: controller.show_frame(NextPage),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

class NextPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is the Next Page")
        label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Go to the Completion Screen",
            command=lambda: controller.show_frame(CompletionScreen),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

class CompletionScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Completion Screen, we did it!")
        label.pack(padx=10, pady=10)
        switch_window_button = ttk.Button(
            self, text="Return to menu", command=lambda: controller.show_frame(MainPage)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

if __name__ == "__main__":
    testObj = windows()
    testObj.mainloop()"""