import customtkinter as ck
import tkinter as tk
from PIL import Image,ImageTk
import os
import ui

PATH=os.path.dirname(os.path.realpath(__file__))
ck.set_appearance_mode("dark")
ck.set_default_color_theme("dark-blue")

class App(ck.CTk):
    WIDTH=340
    HEIGHT=650

    def __int__(self,*args,fg_color="default_theme",**kwargs):
        super().__init__(*args,fg_color=fg_color,**kwargs)
        self.title("Expense Tracker")
        self.resizable(False,False)
        screenHeight=self.winfo_screenheight()
        screenWidth=self.winfo_screenwidth()
        x=(screenWidth/2)-(App.WIDTH/2)
        y=(screenHeight/2)-(App.HEIGHT/2)
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}+{int(x)}+{int(y)}")
        self.config(background=ui.Color.MAIN)
        self.InsertButton=ck.CTkButton(
            self,
            text=None,
            fg_color=ui.Color.PURPLE,
            corner_radius=50,
            text_font=ui.Font.MID,
            width=30,
            height=30,
            hover=False,
            command=self.EntryAnimation,
        )
        self.InsertButton.pack(
            side=tk.BOTTOM,fill=tk.Y,expand=False,pandy=20,ipady=10,ipadx=10
        )
        self.PlusLabel= tk.Label(
            self.InsertButton,
            bg=ui.Color.PURPLE,
            text="+",
            font=ui.Font.BTN,
        )
        self.PlusLabel.place(relx=0.5,rely=0.5,anchor="center")
        self.space=ck.CTkFrame(
            self, fg_color=ui.Color.MAIN,height=1,corner_radius=0
        )
        self.space.pack(side=tk.BOTTOM,fill=tk.X,expand=False,padx=40)
        self.space = ck.CTkFrame(
            self,fg_color=ui.Color.MAIN,width=20,corner_radius=0
        )
        self.space.pack(side=tk.LEFT,fill=tk.Y,expand=False)
        self.space =ck.CTkFrame(
            self,fg_color=ui.Color.MAIN,width=20,corner_radius=0
        )
        self.space=ck.CTkFrame(
            self,fg_color=ui.Color.MAIN,height=20,corner_radius=0
        )
        self.space.pack(side=tk.TOP,fill=tk.X ,expand=False)

        self.NameFrame =ck.CTkFrame(self,fg_color=ui.Color.MAIN)
        self.NameFrame.pack(side=tk.TOP,fill=tk.X,expand=False)
        self.NameLabel=tk.Label(
            self.NameFrame,
            text="Hi , Line Indent "+" sd",
            bg=ui.Color.MAIN,
            justify=tk.LEFT,
            font=ui.font.NAME,
        )
        self.NameLabel.pack(side=tk.left,fill=tk.BOTH,expand=False)
        self.space=ck.CtkFrame(
            self,fg_color=ui.Color.MAIN,height=40,corner_radius=0
        )
        self.space.pack(side=tk.TOP,fill=tk.X,expand=False)




    def on_closing(self,event=0):
        self.destroy()
    def start(self):
        self.mainloop()
if __name__=="__main__":
    app=App()
    app.start()
