from tkinter import *
from tkinter import messagebox
import base64
import os

screen =Tk()
screen.title("Cryptanalysis of Caesar Cipher")
screen.geometry('400x400')

def reset():
    code.set("")
    entry1.delete(1.0,END)
    
def caesar():
    message = entry1.get()
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    new_screen=Toplevel(screen)
    new_screen.title("DECODE")
    new_screen.geometry("400x600")
    

    K_LABEL = Label(new_screen,text='DECODED CIPHER TEXT',font="arial")
    K_LABEL.place(x=10,y=0)
    txt = ()
    for key in range(len(LETTERS)):
        translated = ''

        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                
                if num < 0:
                    num = num + len(LETTERS)
                    
                translated = translated + LETTERS[num]
                
            else:
                translated = translated + symbol
        print('Key #%s: %s' % (key, translated))
        txt += (key, translated+'\n')
    K_LABEL.config(text=txt)
    screen.iconify()
    #messagebox.showinfo("",'Key #%s: %s' % (key, translated))

    new_screen.mainloop()
    
txt_label = Label(screen,text="Enter Cipher Text",fg="black",font=("calbri",13)).place(x=10,y=10)
entry1=Entry(screen,font = "Robote 20",bg="white",relief=GROOVE,bd=0)
entry1.place(x=10,y=50,width = 355,height=100)
    
Button(screen,text="DECODE",height=2,width=50,bd=0,bg="#00bd56",fg="white", command=caesar).place(x=10,y=250)
Button(screen,text="RESET",height=2,width=50,bd=0,bg="#1089ff",fg="white", command=reset).place(x=10,y=300)
    
screen.mainloop()
