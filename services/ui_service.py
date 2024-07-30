from tkinter import *
from PIL import ImageTk, Image

class UI:
    query_display = ""
    output_display = ""
    
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('Voice Assitant for Visually Impaired')
        self.root.geometry("800x450")
        bg = ImageTk.PhotoImage(file="static/background.jpg")
        self.canvas = Canvas(self.root, width=800, height=3500)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0,0, image=bg, anchor='nw')
        self.root.bind("<Configure>", self.resizer)
        self.root.resizable(FALSE, FALSE)

    def resizer(self,e):
        global bg1, resized_bg, new_bg
        bg1 = Image.open("static/background.jpg")
        resized_bg = bg1.resize((e.width, e.height), Image.LANCZOS)
        new_bg = ImageTk.PhotoImage(resized_bg)
        self.canvas.create_image(0,0, image=new_bg, anchor='nw')
        self.canvas.create_text(400, 40, text="Voice Assistant", font=("Arial", 24), fill="white")
        self.canvas.create_text(100,100, text="Query: "+self.query_display, font=("Arial", 18),fill="white",anchor="w")
        self.canvas.create_text(100,200, text="Output:"+self.output_display, font=("Arial", 18), fill="white",anchor="w")
    
    def update_text(self):
        #global new_bg
        self.canvas.delete("all")  # Clear canvas
        self.canvas.create_image(0,0, image=new_bg, anchor='nw')
        self.canvas.create_text(400, 40, text="Voice Assistant", font=("Arial", 24), fill="white")
        self.canvas.create_text(100,100, text="Query: "+self.query_display, font=("Arial", 18),fill="white", anchor="w")
        self.canvas.create_text(100,200, text="Output:"+self.output_display, font=("Arial", 18), fill="white", anchor="w")
        self.root.update_idletasks()
        self.root.update()