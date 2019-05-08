from tkinter import *
import subprocess
import Display
keyword = ''
def show_entry_fields():
   global KeyWord
   KeyWord=e1.get()
   print(KeyWord)



master = Tk()
Label(master, text="Key Word").grid(row=0)


e1 = Entry(master)


e1.grid(row=0, column=1)


Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Enter', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )