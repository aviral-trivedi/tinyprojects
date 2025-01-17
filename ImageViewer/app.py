import tkinter as tk
from PIL import Image, ImageTk

class Ui():

    def __init__(self):
        self.loadGUI()

    
    def loadGUI(self):

        self.root = tk.Tk()
        self.root.geometry("1000x600")
        self.root.resizable()
        self.root.title("Image Viewer")
        self.root.configure(bg="Black") 
        
        self.image_container = (1000,600)
        
        self.pil_image = Image.open("Converter/img.jpg")
        self.pil_image.thumbnail(self.image_container)

        self.image = ImageTk.PhotoImage(self.pil_image)
        self.image_label = tk.Label(image = self.image)
        self.image_label.place(x=0,y=0)

        self.prev_btn = tk.Button(self.root, text="Previous")
        self.prev_btn.place(x=400,y=566)

        self.next_btn = tk.Button(self.root, text="Next")
        self.next_btn.place(x=490,y=566)

    
        self.root.mainloop()


if __name__ == "__main__":
    usr1 = Ui()
