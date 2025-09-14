from tkinter import *
root=Tk()
root.title("VapidTech Calculator 1.2")

e=Entry(root,width=60)   #makes boxes
e.grid(row=0,column=0,columnspan=3,padx=10,pady=20)
                                           #grid() has row,col,colspan,padx,pady commands to design layout of button

def button_click(number):
       num=e.get()
       e.delete(0,END)                     #stops displaying the number stored in e
       e.insert(0,str(num)+str(number))    #number is dislplayed from command=lambda function

                                           #str(num) is number you entered from key
def button_add():
       num1=e.get()                        #number entered before using operand is stored
       global f_num                        #global function can be called outside a function also
       f_num=int(num1)
       global math
       math="add"
       e.delete(0,END)                     #stops displaying the number stored in e

def button_sub():
       num1=e.get()                        #number entered before using operand is stored
       global f_num                        #global function can be called outside a function also
       f_num=int(num1)
       global math
       math="sub"
       e.delete(0,END)

def button_multi():
       num1=e.get()                        #number entered before using operand is stored
       global f_num                        #global function can be called outside a function also
       f_num=int(num1)
       global math
       math="multi"
       e.delete(0,END)                     #stops displaying the number stored in e

def button_div():
       num1=e.get()                        #number entered before using operand is stored
       global f_num                        #global function can be called outside a function also
       f_num=int(num1)
       global math
       math="div"
       e.delete(0,END)       
        
def button_equal():
       num2=int(e.get())
       e.delete(0,END)
       if math=="add":
              e.insert(0,f_num+num2)
       if math=="sub":
              e.insert(0,f_num-num2)
       if math=="multi":
              e.insert(0,f_num*num2)
       if math=="div":
              e.insert(0,f_num/num2)                    

                                 
       
def button_clear():
       e.delete(0,END)

mybutton1=Button(root,text="1",command=lambda: button_click(1),width=20,pady=20).grid(row=1,column=0)
mybutton2=Button(root,text="2",command=lambda: button_click(2),width=20,pady=20).grid(row=1,column=1)
mybutton3=Button(root,text="3",command=lambda: button_click(3),width=20,pady=20).grid(row=1,column=2)
mybutton4=Button(root,text="4",command=lambda: button_click(4),width=20,pady=20).grid(row=2,column=0)
mybutton5=Button(root,text="5",command=lambda: button_click(5),width=20,pady=20).grid(row=2,column=1)
mybutton6=Button(root,text="6",command=lambda: button_click(6),width=20,pady=20).grid(row=2,column=2)
mybutton7=Button(root,text="7",command=lambda: button_click(7),width=20,pady=20).grid(row=3,column=0)
mybutton8=Button(root,text="8",command=lambda: button_click(8),width=20,pady=20).grid(row=3,column=1)
mybutton9=Button(root,text="9",command=lambda: button_click(9),width=20,pady=20).grid(row=3,column=2)
mybutton0=Button(root,text="0",command=lambda: button_click(0),width=20,pady=20).grid(row=4,column=0)
mybutton_equal=Button(root,text="=",command=button_equal,pady=20,width=20).grid(row=6,column=0)
mybutton_clear=Button(root,text="Clear",command=button_clear,pady=20,width=20).grid(row=5,column=0,columnspan=1)
mybutton_add=Button(root,text="+",command=button_add,pady=20,width=42).grid(row=4,column=1,columnspan=2)
mybutton_sub=Button(root,text="-",command=button_sub,pady=20,width=42).grid(row=5,column=1,columnspan=2)
mybutton_multi=Button(root,text="*",command=button_multi,pady=20,width=42).grid(row=6,column=1,columnspan=2)
mybutton_div=Button(root,text="/",command=button_div,pady=20,width=42).grid(row=7,column=1,columnspan=2)
                                          #lambda function assisgns number into a function
                                          #status=DISABLED disables the button 
                                          #above .grid() syntax to adjust the posn of buttons
root.mainloop()