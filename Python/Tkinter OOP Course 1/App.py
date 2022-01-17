import tkinter as tk

STANDARD_FONT = ("FS Elliot Pro", 12)

#pass Tkinter into class
class mainapp(tk.Tk):
    #creates main app window
    #*args is arguments, **kwargs is keyword arguments
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #container is the argument
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.frames = {}
        #frame is the keyword argument
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        #sticky below indicates the alignment plus stretch of the parameter;
        #nsew stands for North, South, East, West
        #if a widget is given EW as the sticky, it will align to the middle of the
        #program and stretch left and right, for example.
        frame.grid(row=0, column=0, sticky = "nsew")
        self.show_frame(StartPage)
    
    def show_frame(self, cont):
        #cont indicates that the self.frames is within the init method
        frame = self.frames[cont]
        frame.tkraise()

def qf(param):
    print(param)

#adds page to window
class StartPage(tk.Frame):
    #init here requires 3 arguments as the parent init uses 3 arguments
    #parent here refers to the mainapp class
    #parent is seen as the argument, controller is seen as the keyword argument
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #STANDARD_FONT is a global variable
        label = tk.Label(self, text = "Start Page", font = STANDARD_FONT)
        label.pack(pady = 10, padx = 10)
        button1 = tk.Button(self, text = "Visit Page 1",
         command = lambda: qf("param"))
        button1.pack()

app = mainapp()
app.mainloop()