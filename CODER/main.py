from cod import*
from decod import* 
from tkinter import*
from keyboard import*
from sumvols import*

def mcod ():
    l4 = Label(text=cod(e.get(), e1.get()), font="arial, 10", bg="#69ebff")
    
    def writ ():
        write(cod(e.get(), e1.get()))
    add_hotkey("ctrl+alt+w", writ)

    l4.place(x=75, y=110)
    
def mdecod ():
    l4 = Label(text=decod(e.get(), e1.get()), font="arial, 10", bg="#69ebff")

    def writ ():
        write(cod(e.get(), e1.get()))
    add_hotkey("ctrl+alt+w", writ)  

    l4.place(x=75, y=110)


w = Tk()
w.geometry("200x200")
w.config(bg="#69ebff")

l = Label(text="шифрувальник", font="arial, 15", bg="#69ebff")
l1 = Label(text="текст/шифр", font="arial, 10", bg="#69ebff")
l2 = Label(text="пароль", font="arial, 10", bg="#69ebff")


b = Button(text="COD", width="10", height="2", bg = "green", command=mcod)
b1 = Button(text="DECOD", width="10", height="2", bg = "red", command=mdecod)

e = Entry()
e1 = Entry()


add_hotkey("ctrl+alt+s+n", new_sumvol)

l.pack()
l1.pack()
e.pack()
l2.pack()
e1.pack()
b.place(x = 10, y = 140)
b1.place(x = 110, y = 140)

w.mainloop()