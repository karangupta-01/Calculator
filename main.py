from logging import exception
from tkinter import *
from tkinter import font

root = Tk()
root.geometry("280x470")
root.minsize(260, 450)
root.maxsize(300, 490)
root.title("Calculator")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="comicsansms 15 bold")
screen.pack(fill=X, ipadx=8, padx=10, pady=10)

f1 = Frame(root, bg="Grey", borderwidth=9, relief=SUNKEN)
f1.pack(side = BOTTOM, anchor="s")

f2 = Frame(root, bg="Grey", borderwidth=7, relief=SUNKEN)
f2.pack(side = BOTTOM, anchor="s")

f3 = Frame(root, bg="grey", borderwidth=7, relief=SUNKEN)
f3.pack(side = BOTTOM, anchor="s")

f4 = Frame(root, bg="grey", borderwidth=7, relief=SUNKEN)
f4.pack(side = BOTTOM, anchor="s")

f5 = Frame(root, bg="grey", borderwidth=7, relief=SUNKEN)
f5.pack(side = BOTTOM, anchor="e")

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == '=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(scvalue.get())
            except Exception as e:
                value = "Error!"
        scvalue.set(value)
        screen.update()
    elif text == 'C':
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+ text)
        screen.update()

b1 = Button(f1, text=".", font="comicsansms 20 bold")
b1.pack(pady=0, padx=8, side = LEFT)
b1.bind("<Button-1>", click)

b2 = Button(f1, text="0", font="comicsansms 20 bold")
b2.pack(pady=0, padx=8, side = LEFT)
b2.bind("<Button-1>", click)

b3 = Button(f1, text="=", font="comicsansms 20 bold")
b3.pack(pady=0, padx=8, side = LEFT)
b3.bind("<Button-1>", click)

b4 = Button(f1, text="+", font="comicsansms 20 bold")
b4.pack(pady=0, padx=8, side = LEFT)
b4.bind("<Button-1>", click)

b5 = Button(f2, text="1", font="comicsansms 20 bold")
b5.pack(pady=0, padx=8, side = LEFT)
b5.bind("<Button-1>", click)

b6 = Button(f2, text="2", font="comicsansms 20 bold")
b6.pack(pady=0, padx=8, side = LEFT)
b6.bind("<Button-1>", click)

b7 = Button(f2, text="3", font="comicsansms 20 bold")
b7.pack(pady=0, padx=8, side = LEFT)
b7.bind("<Button-1>", click)

b8 = Button(f2, text="-", font="comicsansms 20 bold")
b8.pack(pady=0, padx=8, side = LEFT)
b8.bind("<Button-1>", click)

b9 = Button(f3, text="4", font="comicsansms 20 bold")
b9.pack(pady=0, padx=8, side = LEFT)
b9.bind("<Button-1>", click)

b10 = Button(f3, text="5", font="comicsansms 20 bold")
b10.pack(pady=0, padx=8, side = LEFT)
b10.bind("<Button-1>", click)

b11 = Button(f3, text="6", font="comicsansms 20 bold")
b11.pack(pady=0, padx=8, side = LEFT)
b11.bind("<Button-1>", click)

b12 = Button(f3, text="*", font="comicsansms 20 bold")
b12.pack(pady=0, padx=8, side = LEFT)
b12.bind("<Button-1>", click)

b13 = Button(f4, text="7", font="comicsansms 20 bold")
b13.pack(pady=0, padx=8, side = LEFT)
b13.bind("<Button-1>", click)

b14 = Button(f4, text="8", font="comicsansms 20 bold")
b14.pack(pady=0, padx=8, side = LEFT)
b14.bind("<Button-1>", click)

b15 = Button(f4, text="9", font="comicsansms 20 bold")
b15.pack(pady=0, padx=8, side = LEFT)
b15.bind("<Button-1>", click)

b16 = Button(f4, text="/", font="comicsansms 20 bold")
b16.pack(pady=0, padx=8, side = LEFT)
b16.bind("<Button-1>", click)

b17 = Button(f5, text="C", font="comicsansms 20 bold")
b17.pack(pady=0, padx=8, side = LEFT)
b17.bind("<Button-1>", click)

root.mainloop()
