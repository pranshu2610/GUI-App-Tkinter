from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image

root=Tk()

Label(root,text='StrikeScore Zone',font=('Verdana',15)).pack(side=TOP,pady=10)

background_image=PhotoImage(file=r"C:\Users\prans\Desktop\Python Course\GUI\back.png")
background_label = Label(parent, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

music=PhotoImage(file=r"C:\Users\prans\Desktop\Python Course\GUI\earphones.png")
save=PhotoImage(file=r"C:\Users\prans\Desktop\Python Course\GUI\disk.png")
load=PhotoImage(file=r"C:\Users\prans\Desktop\Python Course\GUI\folder.png")
Button(root,text= 'Click Me',image=music).pack(side=TOP)
Button(root,text= 'Click Me',image=save).pack(side=TOP)
Button(root,text= 'Click Me',image=load).pack(side=TOP)
root.mainloop()
