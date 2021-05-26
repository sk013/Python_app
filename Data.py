#  stater code

import tkinter
from tkinter import ttk
from typing import Text
win = tkinter.Tk()
win.title('GUI python app')

# create lables

name_label = ttk.Label(win, text="Enter your name: ")
name_label.grid(row=0, column=0, sticky=tkinter.W)

email_label = ttk.Label(win, text="Enter your email: ")
email_label.grid(row=1, column=0, sticky=tkinter.W)

age_label = ttk.Label(win, text="Enter your age: ")
age_label.grid(row=2, column=0, sticky=tkinter.W)

gender_label = ttk.Label(win, text="Select your gender: ")
gender_label.grid(row=3, column=0, sticky=tkinter.W)

# create entry box
name_var = tkinter.StringVar()
name_entrybox = ttk.Entry(win, width=16, textvariable= name_var)
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()

email_var = tkinter.StringVar()
email_entrybox = ttk.Entry(win, width=16, textvariable= email_var)
email_entrybox.grid(row=1, column=1)

age_var = tkinter.StringVar()
age_entrybox = ttk.Entry(win, width=16, textvariable= age_var)
age_entrybox.grid(row=2, column=1)

# create combobox
gender_var = tkinter.StringVar()
gender_combobox = ttk.Combobox(win, width=13, textvariable = gender_var, state='readonly')
gender_combobox['values'] = ('Male','Female','Others')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

# radio button
user_type = tkinter.StringVar()
radio1 = ttk.Radiobutton(win, text='Student', value='Student', variable= user_type)
radio1.grid(row=4, column=0)
radio2 = ttk.Radiobutton(win, text='Teacher', value='Teacher', variable= user_type)
radio2.grid(row=4, column=1)

# check button
check_var = tkinter.IntVar()
check = ttk.Checkbutton(win, text='i accept all the tearms and conditon' , variable=check_var)
check.grid(row=5 , columnspan=2)

# create button
def action():
    name = name_var.get()
    email = email_var.get()
    age = age_var.get()
    gender = gender_var.get()
    usertype = user_type.get()
    if check_var == 0:
        accept = 'NO'
    else:
        accept = 'YES'

    with open('file.txt','a') as f:
        f.write(f'{name},{email},{age},{gender},{usertype},{accept}')

    name_entrybox.delete(0, tkinter.END)   
    email_entrybox.delete(0, tkinter.END)   
    age_entrybox.delete(0, tkinter.END)   

submit_button = ttk.Button(win, text = "Submit", command=action)
submit_button.grid(row=6, column=1)




win.mainloop()

