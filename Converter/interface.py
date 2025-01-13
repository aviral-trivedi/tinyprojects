from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from conversion import conversion

class ui():

    def __init__(self):
        self.loadGUI()
       
        
    def loadGUI(self):

        #Loading GUI
        self.root = Tk()
        self.root.geometry("250x400")
        self.root.resizable()
        self.root.title("Conversion")
        self.root.configure(bg="Black") 

        heading= Label(self.root,text="Conversion",bg="Black",fg="White",justify="center")
        heading.config(font=("0xProto Nerd Font Mono",25))
        heading.pack(pady=1)

        text1= Label(self.root,text="Cm To Ft",bg="Black",fg="White",justify="center")
        text1.config(font=("Source Sans Pro Normal",13))
        text1.pack(pady=1)

        msgbox1 = Entry()
        msgbox1.pack()

        conv1 = Button(text="Convert",width=4,height=1)
        conv1.config(font=("Source Sans Pro Normal",10))
        conv1.pack(pady=5)

        blank1= Label(self.root,bg="Black")
        blank1.pack(pady=5)
        
        text2= Label(self.root,text="Km To Miles",bg="Black",fg="White",justify="center")
        text2.pack(pady=1)
        text2.config(font=("Source Sans Pro Normal",13))

        msgbox2 = Entry()
        msgbox2.pack()

        conv2 = Button(text="Convert",width=4,height=1)
        conv2.config(font=("Source Sans Pro Normal",10))
        conv2.pack(pady=5)

        blank2= Label(self.root,bg="Black")
        blank2.pack(pady=5)
        
        text3= Label(self.root,text="Usd To Inr",bg="Black",fg="White",justify="center")
        text3.pack(pady=1)
        text3.config(font=("Source Sans Pro Normal",13))

        msgbox3 = Entry()
        msgbox3.pack()

        conv3 = Button(text="Convert",width=4,height=1)
        conv3.config(font=("Source Sans Pro Normal",10))
        conv3.pack(pady=5)

        self.root.mainloop()

ui()