from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd

#Function that encrypt the .bat file

def bat_encriptation(bat,window):

    f = open(bat,'r')
    cnt = f.read()
    encrypted = '\xff\xfe\ncls\n' + cnt
    f.close()
    f2 = open('encryptedbat.bat','w')
    f2.write(encrypted)
    f2.close()
    button = Button(window, text='Close the program and the file will be on the same path where this program is',width=60 , height =6,bg='orange',state='disabled')
    button.grid(row = 8, column = 60,padx=150,pady=50)


#This function asks the user for the file they want to encrypt.
def select_file(window):

    filetypes = (
        ('bat files', '*.bat'),
        ('All files', '*.*')
    )
    file = fd.askopenfilename(title='Choose a file',initialdir='/',filetypes=filetypes)
    bat_encriptation(file,window)
   

window = tk.Tk() #Creation of the tkinter window.

window.title('Bat Encryptor')
window.geometry('700x500')              #Config of the window
window.config(background='purple',)

button = Button(window, text='Select Bat File',width=60 , height =6,command=lambda:select_file(window),bg='green') #Creating the button that calls the 'select file' function. 
button.grid(row = 4, column = 60,padx=150,pady=50)
txt = Button(window,text='Developed by @aitortxu_pk', width=30,height=2,bg='light blue',state='disabled',fg='yellow')
txt.grid(row=6,column=60,padx=150,pady=50)


window.mainloop()
