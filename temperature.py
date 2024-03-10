from tkinter import *
from tkinter import ttk


root = Tk()
root.title("chamge temperature")
root.iconbitmap("CheckList Asset/check.ico")
root.resizable(0,0)

font = ("Arial",15,"bold")
color = "orange"

def convert():
    celcius_value = float(input_txt.get())

    unit_value = temp_combo.get()

    print(celcius_value)
    print(unit_value)

input_label = Label(root,text="Celcius",font=font)
input_txt = Entry(root,width=20,font=font)
input_label.grid(row=0,column=0,sticky=W)
input_txt.grid(row=0,column=1)

unit_label = Label(root,text="Change celcius",font=font)
unit_list = ["fahrenheit","Kelvin"]
temp_combo = ttk.Combobox(root,value=unit_list,font=font,width=18)
temp_combo.set("Kelvin")
unit_label.grid(row=1,column=0,sticky=W)
temp_combo.grid(row=0,column=0)

output_label = Label(root,text="result",font=font)
output_txt = Entry(root,width=20,font=font)
output_label.grid(row=2,column=0,sticky=W)
temp_combo.grid(row=2,column=1)

convertBtn = Button(root,text="Change",font=font,width=10,bg=color,command=convert)
resetBtn = Button(root,text="delete",font=font,width=7,bg=color)
convertBtn.grid(row=3,column=1,sticky=W,padx=5,pady=5)
resetBtn.grid(row=3,column=1,sticky=E)

root.mainloop()