from tkinter import *

root = Tk()
root.title("CheckList Application")
root.iconbitmap("CheckList Asset/check.ico")

root.resizable(0,0)
root.geometry("400x500+500+100")

font = ("arial",15)
color = "pink"
root.config(bg=color)

def addItem():
    data = inputEntry.get()
    listbox.insert(END,data)
    inputEntry.delete(0,END)

def removeItem():
    listbox.delete(ANCHOR)

def clearList():
    listbox.delete(0,END)


input_frame = Frame(root,bg=color)
output_frame = Frame(root,bg=color)
Button_frame = Frame(root,bg=color)

input_frame.pack()
output_frame.pack()
Button_frame.pack()

inputEntry = Entry(input_frame,width=25,font=font)
inputEntry.grid(row=0,column=0,padx=5,pady=5,ipady=5)

btnAdd = Button(input_frame,text="Add",font=font,command=addItem)
btnAdd.grid(row=0,column=1,padx=5,pady=5)

listbox = Listbox(output_frame,width=35,height=12,font=font)
listbox.grid(row=0,column=0,padx=5,pady=5)

btnRemove = Button(Button_frame,text="delete",font=font,command=removeItem)
btnRemove.grid(row=0,column=0,padx=2,pady=2,ipadx=10)

btnClear = Button(Button_frame,text="Delete all",font=font,command=clearList)
btnClear.grid(row=0,column=1,padx=2,pady=2,ipadx=10)

btnQuit = Button(Button_frame,text="Quit Program",font=font,command=root.destroy)
btnQuit.grid(row=0,column=2,padx=2,pady=2,ipadx=10)
root.mainloop()