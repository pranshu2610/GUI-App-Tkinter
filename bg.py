from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.geometry("400x420")
canvas=Canvas(root,width=300,height=160)
image=ImageTk.PhotoImage(Image.open(r"C:\Users\prans\Desktop\Python Course\GUI\back.png"))
#canvas.create_image(0,0,anchor=NW,image=image)
#canvas.pack()
Label(root,image=image,text="Update User",compound=CENTER).pack()

music=PhotoImage(file=r"C:\Users\prans\Desktop\Python Course\GUI\earphones.png")
save=PhotoImage(file=r"C:\Users\prans\Desktop\Python Course\GUI\disk.png")
load=PhotoImage(file=r"C:\Users\prans\Desktop\Python Course\GUI\folder.png")
Button(root,text= 'Click Me',image=music).pack(side=TOP)
Button(root,text= 'Click Me',image=save).pack(side=TOP)
Button(root,text= 'Click Me',image=load).pack(side=TOP)

root.mainloop()