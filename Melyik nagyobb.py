from tkinter import *

# Window

window = Tk()

window.title("Melyik nagyobb?")
window.geometry("405x150")

def ok():
    try:
        sz2=in2.get()
        sz1=in1.get()
        In1 = int(sz1)
        In2 = int(sz2)
        if In1 > In2:
            log["state"] = NORMAL
            log.delete(1.0, END)
            log["state"]=DISABLED
            Rjel["state"] = NORMAL
            Rjel.delete(1.0, END)
            Rjel.insert(END," >")
            Rjel["state"]=DISABLED
        elif In2 > In1:
            log["state"] = NORMAL
            log.delete(1.0, END)
            log["state"]=DISABLED
            Rjel["state"] = NORMAL
            Rjel.delete(1.0, END)
            Rjel.insert(END," <")
            Rjel["state"]=DISABLED
        elif In1 == In2:
            log["state"] = NORMAL
            log.delete(1.0, END)
            log["state"]=DISABLED
            Rjel["state"] = NORMAL
            Rjel.delete(1.0, END)
            Rjel.insert(END," =")
            Rjel["state"]=DISABLED
    except:
        print("Error")
        print("Write just numbers")
        log["state"] = NORMAL
        log.delete(1.0, END)
        log.insert(END,"       Error")
        log["state"]=DISABLED
        Rjel["state"] = NORMAL
        Rjel.delete(1.0, END)
        Rjel["state"]=DISABLED


Button(window, text="Ok",command=ok, font="Helmetica 12 bold").grid(row=1, column=1)

in1= Entry(window, font="Helmetica 20 bold",width=10)
in1.grid(row=0, column=0)

Rjel= Text(window, height=1, width=2, state=DISABLED, font="Helmetica 20 bold",)
Rjel.grid(row=0, column=1)

in2= Entry(window, font="Helmetica 20 bold",width=10)
in2.grid(row=0, column=2)

log= Text(window, height=1, width=10, state=DISABLED, font="Helmetica 12 bold")
log.grid(row=2,column=1)

window.mainloop()
