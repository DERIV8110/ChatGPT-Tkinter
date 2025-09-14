from tkinter import *
import math as mt
root=Tk()
root.title("VapidTech Calculator 1.3")

e=Entry(root,width=60)                     #makes boxes
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

def button_pow():
       num1=e.get()                        #number entered before using operand is stored
       global f_num                        #global function can be called outside a function also
       f_num=int(num1)
       global math
       math="pow"
       e.delete(0,END)

def button_sqrt():
       num1=e.get()                        #number entered before using operand is stored
       global f_num                        #global function can be called outside a function also
       f_num=int(num1)
       global math
       math="sqrt"
       e.delete(0,END)       

def button_cbrt():
       num1=e.get()                        #number entered before using operand is stored
       global f_num                        #global function can be called outside a function also
       f_num=int(num1)
       global math
       math="cbrt"
       e.delete(0,END)

def button_equal():
       if math=="add":
              num2=int(e.get())
              e.delete(0,END)
              e.insert(0,f_num+num2)
       if math=="sub":
              num2=int(e.get())
              e.delete(0,END)
              e.insert(0,f_num-num2)
       if math=="multi":
              num2=int(e.get())
              e.delete(0,END)
              e.insert(0,f_num*num2)
       if math=="div":
              num2=int(e.get())
              e.delete(0,END)
              e.insert(0,f_num/num2)                    
       if math=="pow":
              num2=int(e.get())
              e.delete(0,END)
              e.insert(0,f_num**num2)
       if math=="sqrt":
              e.insert(0,mt.sqrt(f_num))       #only one input number is to be operated and displayed                    
       if math=="cbrt":
              e.insert(0,mt.cbrt(f_num))       #only one input number is to be operated and displayed
                                 
       
def button_clear():
       e.delete(0,END)

mybutton1     =Button(root,text="1"          ,command=lambda: button_click(1),width=20,pady=20).grid(row=1,column=0)
mybutton2     =Button(root,text="2"          ,command=lambda: button_click(2),width=20,pady=20).grid(row=1,column=1)
mybutton3     =Button(root,text="3"          ,command=lambda: button_click(3),width=20,pady=20).grid(row=1,column=2)
mybutton4     =Button(root,text="4"          ,command=lambda: button_click(4),width=20,pady=20).grid(row=2,column=0)
mybutton5     =Button(root,text="5"          ,command=lambda: button_click(5),width=20,pady=20).grid(row=2,column=1)
mybutton6     =Button(root,text="6"          ,command=lambda: button_click(6),width=20,pady=20).grid(row=2,column=2)
mybutton7     =Button(root,text="7"          ,command=lambda: button_click(7),width=20,pady=20).grid(row=3,column=0)
mybutton8     =Button(root,text="8"          ,command=lambda: button_click(8),width=20,pady=20).grid(row=3,column=1)
mybutton9     =Button(root,text="9"          ,command=lambda: button_click(9),width=20,pady=20).grid(row=3,column=2)
mybutton0     =Button(root,text="0"          ,command=lambda: button_click(0),width=20,pady=20).grid(row=4,column=0)
mybutton_equal=Button(root,text="="          ,command=button_equal,pady=20,width=20).grid(row=6,column=0)
mybutton_clear=Button(root,text="Clear"      ,command=button_clear,pady=20,width=20).grid(row=5,column=0,columnspan=1)
mybutton_add  =Button(root,text="+"          ,command=button_add  ,pady=20,width=42).grid(row=4,column=1,columnspan=2)
mybutton_sub  =Button(root,text="-"          ,command=button_sub  ,pady=20,width=42).grid(row=5,column=1,columnspan=2)
mybutton_multi=Button(root,text="*"          ,command=button_multi,pady=20,width=42).grid(row=6,column=1,columnspan=2)
mybutton_div  =Button(root,text="/"          ,command=button_div  ,pady=20,width=42).grid(row=7,column=1,columnspan=2)

mybutton_pow  =Button(root,text="^"          ,command=button_pow   ,pady=20,width=42).grid(row=8,column=1,columnspan=2)
mybutton_sqrt =Button(root,text="sq.root"    ,command=button_sqrt  ,pady=20,width=42).grid(row=9,column=1,columnspan=2)
mybutton_cbrt =Button(root,text="cb.root"    ,command=button_cbrt  ,pady=20,width=42).grid(row=10,column=1,columnspan=2)


                                          #lambda function assisgns number into a function
                                          #status=DISABLED disables the button 
                                          #above .grid() syntax to adjust the posn of buttons
root.mainloop()