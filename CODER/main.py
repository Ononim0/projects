from cod import*
from decod import* 
from tkinter import*

def mcod ():
    l4 = Label(text=cod(e.get(), e1.get()), font="arial, 10")
    l4.place(x=75, y=110)
    
def mdecod ():
    l4 = Label(text=decod(e.get(), e1.get()), font="arial, 10")
    l4.place(x=75, y=110)

w = Tk()
w.geometry("200x200")

l = Label(text="шифрувальник", font="arial, 15")
l1 = Label(text="текст/шифр", font="arial, 10")
l2 = Label(text="пароль", font="arial, 10")


b = Button(text="COD", width="10", height="2", bg = "green", command=mcod)
b1 = Button(text="DECOD", width="10", height="2", bg = "red", command=mdecod)

e = Entry()
e1 = Entry()

l.pack()
l1.pack()
e.pack()
l2.pack()
e1.pack()
b.place(x = 10, y = 140)
b1.place(x = 110, y = 140)

w.mainloop()