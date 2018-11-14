import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
window.title('my window')
window.geometry('200x200')

def hit_me():
    #tk.messagebox.showinfo(title='hi!',message='hello')
    print(tk.messagebox.askretrycancel(title='output',message='are you sure?'))
tk.Button(window,text='hit me',command=hit_me).pack()
window.mainloop()