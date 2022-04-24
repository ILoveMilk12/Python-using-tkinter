import string
from tkinter import *

# Window

window = Tk()

window.title("Konverter")
window.geometry("800x600")

# Code

def km_to_mi():
    aa=in1.get()
    aab = string(aa)
    if in1=="Esc":
        print("******Esc******")
    else:
        try:
            km=in1.get()
            ktm = float(km) / 1.609344
            Mérföld["state"] = NORMAL
            Mérföld.delete(1.0, END)
            ktm = str(ktm)
            Mérföld.insert(END, ktm[0:5])
            Mérföld["state"]=DISABLED
            print(in1,ktm)
            print(in2)
        except:
            Mérföld["state"] = NORMAL
            Mérföld.delete(1.0, END)
            Mérföld.insert(END,"Error")
            Mérföld["state"]=DISABLED
            print(aab)

def c_to_f():
    try:
        c=in2.get()
        ctf = float(c) * 9/5 + 32   
        Farenheit["state"] = NORMAL
        Farenheit.delete(1.0, END)
        ctf = str(ctf)
        Farenheit.insert(END, ctf[0:5])
        Farenheit["state"]=DISABLED
    except:
        Farenheit["state"] = NORMAL
        Farenheit.delete(1.0, END)
        Farenheit.insert(END,"Error")
        Farenheit["state"]=DISABLED

# Costumise Window 

Label(window, text="Kilóméter", font="Helmetica 12 bold").grid(row=0,column=1) # row == sor column == oszlop
Label(window, text="Mérföld", font="Helmetica 12 bold").grid(row=1,column=1)

Label(window, text="Celsius", font="Helmetica 12 bold").grid(row=3,column=1) # row == sor column == oszlop
Label(window, text="Farenheit", font="Helmetica 12 bold").grid(row=4,column=1)

Button(window, text="Calculate",command=km_to_mi, font="Helmetica 12 bold").grid(row=2, column=0)

Button(window, text="Calculate",command=c_to_f, font="Helmetica 12 bold").grid(row=6, column=0)

in1= Entry(window, font="Helmetica 20 bold")
in1.grid(row=0, column=0)

in2= Entry(window, font="Helmetica 20 bold")
in2.grid(row=3, column=0)

Mérföld= Text(window, height=1, width=20, state=DISABLED, font="Helmetica 20 bold")
Mérföld.grid(row=1, column=0)


Farenheit= Text(window, height=1, width=20, state=DISABLED, font="Helmetica 20 bold")
Farenheit.grid(row=4, column=0)

window.mainloop()
