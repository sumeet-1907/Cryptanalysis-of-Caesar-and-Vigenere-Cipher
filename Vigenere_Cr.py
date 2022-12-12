from tkinter import *
from tkinter import messagebox
import detectEnglish, vigenereCipher, pyperclip


screen =Tk()
screen.title("Cryptanalysis of Vigenere Cipher")
screen.geometry('400x400')

def reset():
    code.set("")
    entry1.delete(1.0,END)

def vignere():
    ciphertext = entry1.get()
    hackedMessage = hackVigenere(ciphertext)
    if hackedMessage != None:
        Label(screen,text='Copying hacked message to clipboard:').place(x=0,y=20)
        Label(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        Label(screen,text= 'Failed to hack encryption.')
        
def hackVigenere(ciphertext):
    txt = ''
            
    fo = open('dictionary.txt')
    words = fo.readlines()
    fo.close()
    for word in words:
        word = word.strip() 
        decryptedText = vigenereCipher.decryptMessage(word, ciphertext)
        if detectEnglish.isEnglish(decryptedText, wordPercentage=40):
            
            print()
            Label(screen,text='').place(x=20,y=20)
            txt1 = 'Key ' + str(word) + ': ' + decryptedText[:100]
            txt += str(word)+ txt1 +'\n'
            messagebox.showinfo('',txt)
            print()
            #print('Enter D for done, or just press Enter to continue breaking:')
            #response = input('> ')
            #if response.upper().startswith('D'):
                #return decryptedText
    

txt_label = Label(screen,text="Enter Cipher Text",fg="black",font=("calbri",13)).place(x=10,y=10)
entry1=Entry(screen,font = "Robote 20",bg="white",relief=GROOVE,bd=0)
entry1.place(x=10,y=50,width=355,height=100)
    
Button(screen,text="DECODE",height=2,width=50,bd=0,bg="#00bd56",fg="white", command=vignere).place(x=10,y=250)
Button(screen,text="RESET",height=2,width=50,bd=0,bg="#1089ff",fg="white", command=reset).place(x=10,y=300)
    
screen.mainloop()
