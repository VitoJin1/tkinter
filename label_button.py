import tkinter as tk

window=tk.Tk()
window.title('my first window')
window.geometry('200x100')
#窗口内容
message_show=tk.Variable()
L=tk.Label(window,textvariable=message_show,
           bg='green',font=('Arial',12),
           width=15,height=2)
L.pack()
click_flag=False
def button_click():
    global click_flag
    if click_flag==False:
        click_flag=True
        message_show.set('clicked')
    else:
        click_flag=False
        message_show.set('')

B=tk.Button(window,text='click it',width=15,height=2,command=button_click)
B.pack()
window.mainloop()
#这里的message_show指的是tk的一个方法，相当于tk.StringVar().set(),不需要设置成变量，只调用方法。