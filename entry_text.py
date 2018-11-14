import tkinter as tk
window=tk.Tk()
window.title('text_window')
window.geometry('200x200')

E=tk.Entry(window,show='1')
E.pack()
T=tk.Text(window,height=2)
T.pack()

def insert_point():
    var=E.get()
    T.insert('insert',var)
def insert_end():
    var=E.get()
    #T.insert(1.1,var) #代表第一行第一位
    T.insert('end',var)

botton1=tk.Button(window,text='insert point', width=15,
                  height=2, command=insert_point)
botton1.pack()

botton2=tk.Button(window,text='insert end',width=15,
                  height=2,command=insert_end)
botton2.pack()


window.mainloop()

#各个框的位置默认height是1，位置从上到下按照解释器充上到下的顺序。