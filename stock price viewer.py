from tkinter import *
import json                            #only for pretty printing
import requests

root=Tk()
e=Entry(root,width=50)                 #makes boxes
e.pack()
e.insert(0,"enter stock symbol here")  #pre-written text in box
def myclick():
       symbol=e.get()
       #url consists of url of website from documentation on website then symbol and token(api key)
       url=f"https://finnhub.io/api/v1/quote?symbol={symbol}&token=d32aglpr01qn0gi34v30d32aglpr01qn0gi34v3g"
       reponse=requests.get(url)
       sdata=reponse.json()
       mylabel=Label(root,text=f"{symbol} price: {sdata["c"]}")   # f" with {} in a continous string separates variables
                                                                  #and string
       mylabel.pack()                                             
mybutton=Button(root,text="get current price",command=myclick)
                                             #command shows mylabel after clicking button
                                             #status=DISABLED disables the button
mybutton.pack()
root.mainloop()