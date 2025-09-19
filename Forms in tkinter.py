from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('VapidSelect v1.1')
root.iconbitmap('c:/python images/vapidTech.ico')


text1=Label(root,text="Select desired parts below",font=("arial",10))
text1.pack()

text2=Label(root,text="1.Select engine:",font=("arial",10))
text2.pack(anchor=W)

engine_image=ImageTk.PhotoImage(Image.open("C:/python images/engine.jpg"))
image=Label(image=engine_image).pack()

engines = [("Inline 6",150000),("V6",80000),("V8",250000),("V10",400000)]

engine = StringVar()                                                              #reads variable in the list
engine.set("Inline 6")                                                            #preset is inline 6

for text, part in engines:
	Radiobutton(root, text=text, variable=engine, value=part).pack(anchor=W)   #part is value in the list

def clicked(value):
	myLabel = Label(root, text=value)
	myLabel.pack()	

myButton = Button(root, text="select", command=lambda: clicked(engine.get()))
myButton.pack()
mainloop()