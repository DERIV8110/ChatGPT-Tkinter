from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('VapidSelect v1.2')
root.iconbitmap('c:/python images/vapidTech.ico')

# ============ SCROLLABLE FRAME SETUP ============                           #scroll part is written by chatGPT
canvas = Canvas(root)                                                        #adds canvas 
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)           #scrollbar() --> vertical added with y axis sliding
scrollbar.pack(side=RIGHT, fill=Y)                                           #position of scrollbar in app
canvas.pack(side=LEFT, fill=BOTH, expand=True)

canvas.configure(yscrollcommand=scrollbar.set)

frame = Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_configure)

# ============ YOUR CONTENT GOES INSIDE FRAME ============
text1 = Label(frame, text="CAR PARTS", font=("arial", 10))
text1.pack()

text2 = Label(frame, text="1. Select engine:", font=("arial", 10))
text2.pack(anchor=W)

engine_image = ImageTk.PhotoImage(Image.open("C:/python images/engine.jpg"))
Label(frame, image=engine_image).pack()

engines = [("Inline 6", 150000), ("V6", 80000), ("V8", 250000), ("V10", 400000)]

engine = StringVar()
engine.set("Inline 6")

for text, part in engines:
    Radiobutton(frame, text=text, variable=engine, value=part).pack(anchor=W)

def clicked(value):
    Label(frame, text=value).pack()

myButton = Button(frame, text="Select Engine", command=lambda: clicked(engine.get()))
myButton.pack()

# ---------------- Transmission ----------------
text3 = Label(frame, text="2. Select Transmission:", font=("arial", 10))
text3.pack(anchor=W)

trans_image = ImageTk.PhotoImage(Image.open("C:/python images/trans.jpeg"))
Label(frame, image=trans_image).pack()

trans_type = [("Manual", 70000), ("Automatic", 400000)]

trans = StringVar()
trans.set("Manual")

for text, part in trans_type:
    Radiobutton(frame, text=text, variable=trans, value=part).pack(anchor=W)

myButton2 = Button(frame, text="Select Transmission", command=lambda: clicked(trans.get()))
myButton2.pack()
# ---------------- Air Intake ----------------

text4 = Label(frame, text="3. Select Intake:", font=("arial", 10))
text4.pack(anchor=W)

intake_image = ImageTk.PhotoImage(Image.open("C:/python images/turbo.webp"))
Label(frame, image=intake_image).pack()

intake_type = [("Naturally Aspirated", 0), ("TurboCharger", 40000), ("SuperCharger", 90000)]

intake = StringVar()                                    #intake registers response selected
intake.set("Naturally Aspirated")                       #intake peset option

for text, part in intake_type:
    Radiobutton(frame, text=text, variable=intake, value=part).pack(anchor=W)

myButton3 = Button(frame, text="Select Intake", command=lambda: clicked(intake.get()))    #command --> to get the value using Lambda:
myButton3.pack()
# ---------------- Fuel Capacity ----------------
text5 = Label(frame, text="4. Select Fuel Capacity:", font=("arial", 10))
text4.pack(anchor=W)

tank_image = ImageTk.PhotoImage(Image.open("C:/python images/tank.webp"))
Label(frame, image=tank_image).pack()

tank_type = [("Small(50L)", 20000), ("Medium(60L)", 25000), ("Large(90L)", 30000)]

tank = StringVar()
tank.set("Small(L)")

for text, part in tank_type:
    Radiobutton(frame, text=text, variable=tank, value=part).pack(anchor=W)

myButton4 = Button(frame, text="Select Tank", command=lambda: clicked(tank.get()))
myButton4.pack()
# ---------------- Show Total ----------------
def show_total():
    try:
        eng_value = int(engine.get())
        transmission = int(trans.get())
        tank_cap=int(tank.get())
        grand_total = eng_value + transmission + tank_cap
        Label(frame, text=f"Grand Total: {grand_total}").pack()
    except:
        Label(frame, text="Error calculating total").pack()

Button(frame, text="Show Grand Total", command=show_total).pack(pady=10)

# ============ MAIN LOOP ============
root.mainloop()
