import tkinter as tk
import pickle
from tkinter import messagebox
import numpy as np

window=tk.Tk()
window.title('Welcome to my world')
window.geometry('450x300')

#welcome comvas
canvas=tk.Canvas(window,height=127,width=445)
image_file=tk.PhotoImage(file='welcome.gif')
image=canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack(side='top')

tk.Label(window,text='User name: ').place(x=50,y=150)
tk.Label(window,text='Password: ').place(x=50,y=190)

var_usr_name=tk.StringVar()
var_usr_name.set('example@python.com')
entry_usr_name=tk.Entry(window,textvariable=var_usr_name)
entry_usr_name.place(x=160,y=150)


var_usr_pw=tk.StringVar()

entry_usr_pw=tk.Entry(window,textvariable=var_usr_pw,show='*')
entry_usr_pw.place(x=160,y=190)
def usr_login():
    user_name=var_usr_name.get()
    user_pw=var_usr_pw.get()
    try:
        with open('user_info.pickle','rb') as user_file:
            user_info=pickle.load(user_file)
    except FileNotFoundError:
        with open('user_info.pickle','wb') as user_file:
            user_info={'admin':'admin'}
            pickle.dump(user_info,user_file)
    if user_name in user_info:
        if user_pw==user_info[user_name]:
            tk.messagebox.showinfo(title='Login Success!',message='Welcome!'+user_name)
        else:
            tk.messagebox.showerror(title='error!',message='Not found Username')
    else:
        Is_sign_up=tk.messagebox.askyesno(title='welcome',message='signup a new account?')
        if Is_sign_up==1:
            usr_sign_up()

def usr_sign_up():
    def signup():
        type_name=user_name.get()
        type_pw=  user_pw.get()
        try:
            with open('user_info.pickle', 'rb') as user_file:
                info_exist = pickle.load(user_file)
        except FileNotFoundError:
            with open('user_info.pickle', 'wb') as user_file:
                info_exist = {'admin': 'admin'}
                pickle.dump(info_exist, user_file)
        if type_name in info_exist:
            tk.messagebox.showinfo(title='Notice',message='existed user name!')
        else:
            info_exist[type_name]=type_pw
            with open('user_info.pickle', 'wb') as user_file:
                pickle.dump(info_exist,user_file)
            tk.messagebox.showinfo(title='congratulation',message='you hace sign up successfully')
        window_new.destroy()
    window_new=tk.Toplevel(window)
    window_new.title('sign up window')
    window_new.geometry('300x200')
    tk.Label(window_new,text='user name').place(x=25,y=50)
    tk.Label(window_new,text='pass word').place(x=25,y=100)
    user_name=tk.StringVar()
    entry_user_name=tk.Entry(window_new,textvariable=user_name)
    entry_user_name.place(x=100,y=50)
    user_pw=tk.StringVar()
    entry_user_pw=tk.Entry(window_new,textvariable=user_pw)
    entry_user_pw.place(x=100,y=100)
    button_signup=tk.Button(window_new,text='sign up',width=15,height=1,command=signup)
    button_signup.place(x=100,y=150)

button_login=tk.Button(window,text='Login',command=usr_login)
button_login.place(x=170,y=230)
button_signup=tk.Button(window,text='Sign up',command=usr_sign_up)
button_signup.place(x=270,y=230)
window.mainloop()