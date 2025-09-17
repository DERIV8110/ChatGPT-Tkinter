from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("VapidTech gallery v1.3")
root.iconbitmap('C:/python images/feather.ico')            
# root.iconbitmab() --> icon of the app
my_img1 =ImageTk.PhotoImage(Image.open("C:/python images/porsche.png"))
my_img2 =ImageTk.PhotoImage(Image.open("C:/python images/audi.png"))
my_img3 =ImageTk.PhotoImage(Image.open("C:/python images/bmw.png"))
my_img4 =ImageTk.PhotoImage(Image.open("C:/python images/ferrari.png"))
my_img5 =ImageTk.PhotoImage(Image.open("C:/python images/tesla.png"))
my_img6 =ImageTk.PhotoImage(Image.open("C:/python images/subaru.png"))

# imagetk.photoimage(image.open()) -->shows image from location provided
my_list = [my_img1,my_img2,my_img3,my_img4,my_img5,my_img6]
# lists of images variables to change images
my_label1=Label(image=my_img1)
my_label1.grid(row=0,column=0,columnspan=3)

def forward(image_number):
       global my_label1
       global button_forw
       global button_back

       my_label1.grid_forget()  #grid_forget() --> forgets given row and column
       my_label1=Label(image=my_list[image_number-1])
       my_label1.grid(row=0, column=0, columnspan=3)
       button_forw = Button(root,text=">",command=lambda: forward(image_number+1))
       button_back = Button(root,text="<",command=lambda: back(image_number-1))
       button_forw.grid(row=1,column=2)
       button_back.grid(row=1,column=0)
                                #Lambda: --> let's work on numbers given
       if image_number==5:      #disables next button on last image
              button_forw=Button(root, text=">", state=DISABLED)

def back(image_number):
       global my_label1
       global button_forw
       global button_back

       my_label1.grid_forget()
       my_label1=Label(image=my_list[image_number-1])
       my_label1.grid(row=0, column=0, columnspan=3)
       button_forw = Button(root,text=">",command=lambda: forward(image_number+1))
       button_back = Button(root,text="<",command=lambda: back(image_number-1))
       button_forw.grid(row=1,column=2)
       button_back.grid(row=1,column=0)

       if image_number==1:      #disables back button on first image
              button_back=Button(root, text="<", state=DISABLED)      

button_forw = Button(root,text=">",bg="blue",fg="white",command=lambda: forward(2))
button_exit = Button(root,text="Close",command=root.quit,font=("Arial",10),pady=10,width=20,bg="blue",fg="white")
button_back = Button(root,text="<",bg="blue",fg="white",command=back,state=DISABLED)
button_forw.grid(row=1,column=2)
button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)

root.mainloop()