from tkinter import *
import os
from tkinter import filedialog

def openfile():
    path = filedialog.askopenfilename(initialdir='/', title="Open a File", filetypes=(("All Files", '*.*'), ("Text Documnents", '*.txt')))
    os.startfile(path)

window = Tk()
window.title("Marc File Explorer")
window.geometry("248x80")
button = Button(text="Open", command=openfile)
button.pack()
window.mainloop()