#https://pythonprogramming.net/


from tkinter import *
from PIL import Image,ImageTk  #Pillow Library

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()

    def init_window(self):
        self.master.title("StrikeScore Notepad") #Title
        self.pack(fill=BOTH, expand=1)           #Widget to take fullspace

        menu=Menu(self.master)
        self.master.config(menu=menu)
        file=Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)
        edit=Menu(menu)
        edit.add_command(label="Music", command=self.showImg1)
        edit.add_command(label="Save", command=self.showImg2)
        edit.add_command(label="Files", command=self.showImg3)
        edit.add_command(label="Show Text", command=self.showText)
        menu.add_cascade(label="Edit", menu=edit)

        quitButton=Button(self,text="Quit",command=self.client_exit)
        quitButton.place(x=180,y=30)

    def showImg1(self):
        load=Image.open("earphones.png")
        render=ImageTk.PhotoImage(load)

        #label can be text or images
        img=Label(self, image=render)
        img.image=render
        img.place(x=0,y=0)

    def showImg2(self):
        load=Image.open("disk.png")
        render=ImageTk.PhotoImage(load)

        #label can be text or images
        img=Label(self, image=render)
        img.image=render
        img.place(x=0,y=70)

    def showImg3(self):
        load=Image.open("folder.png")
        render=ImageTk.PhotoImage(load)

        #label can be text or images
        img=Label(self, image=render)
        img.image=render
        img.place(x=0,y=140)

    def showText(self):
        text=Label(self,text="Hey this looks good")
        text.pack()
        
    def client_exit(self):
        exit()
        

root=Tk()
root.geometry("400x420")
app=Window(root) #creation of an instance
root.mainloop()
