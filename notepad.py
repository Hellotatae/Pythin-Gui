from tkinter import *
from PIL import ImageTk,Image
from tkinter import font
from tkinter import scrolledtext
import tkinter.messagebox
from tkinter.filedialog import *

root = Tk()
root.title("Notepad")
root.resizable(0,0)
root.geometry("600x600")
root.config(bg="#6c8099")
root.iconbitmap("Note Asset/note.ico")

def changeFont(e):
    pass

def saveNote():
    myFile = asksaveasfilename(initialdir="./",title="Seva Note",filetypes=(("Text File","*.txt"),("All File","*")))
    with open(myFile,"w",encoding="utf8") as file:
        file.write(fontfamily.get()+"\n")
        file.write(str(fontSize.get())+"\n")
        file.write(fontstyle.get()+"\n")
        file.write(textArea.get("1.0",END))

def openNote():
    myFile = askopenfilename(initialdir="./",title="open notes",filetypes=(("Text File","*.txt"),("All File","*")))
    with open(myFile,"r",encoding="utf8") as file:
        textArea.delete("1.0",END)
        fontfamily.set(file.readline().strip())
        fontSize.set(file.readline().strip())
        fontstyle.set(file.readline().strip())
        content = file.read()
        textArea.insert("1.0",content)

def newNote():
    confirm = tkinter.messagebox.askquestion("Enter","Are you sure ?")
    if confirm == "yes":
        textArea.delete("1.0",END)

def closeNote():
    confirm = tkinter.messagebox.askquestion("Enter","Are you sure ?")
    if confirm == "yes":
       root.destroy()

def changeFont(e):
    if fontstyle.get()=="none":
        myFont=(fontfamily.get(),fontSize.get())
    else:
        myFont=(fontfamily.get(),fontSize.get(),fontstyle.get())
    
    textArea.config(font=myFont)

#settings
menu_color = "#dbdadb"
text_color = "white"

#frame
menuFrame = Frame(root,bg=menu_color)
textFrame = Frame(root,bg=text_color)
menuFrame.pack(padx=5,pady=5)
textFrame.pack(padx=5,pady=5)

#menu button
new_img = ImageTk.PhotoImage(Image.open("Note Asset/new.png"))
btnNew = Button(menuFrame,image=new_img,command = newNote)
btnNew.grid(row=0,column=0,padx=5,pady=5)

open_img = ImageTk.PhotoImage(Image.open("Note Asset/open.png"))
btnOpen = Button(menuFrame,image=open_img,command=openNote)
btnOpen.grid(row=0,column=1,padx=5,pady=5)

save_img = ImageTk.PhotoImage(Image.open("Note Asset/save.png"))
btnSave = Button(menuFrame,image=save_img,command=saveNote)
btnSave.grid(row=0,column=2,padx=5,pady=5)

quit_img = ImageTk.PhotoImage(Image.open("Note Asset/quit.png"))
btnQuit = Button(menuFrame,image=quit_img,command=closeNote)
btnQuit.grid(row=0,column=3,padx=5,pady=5)

allFonts = font.families()
fontfamily = StringVar()
fontOption = OptionMenu(menuFrame,fontfamily,*allFonts,command=changeFont)
fontfamily.set("Arial")
fontOption.config(width=20)
fontOption.grid(row=0,column=4,padx=5,pady=5)

sizes = [8,12,18,25,36,42,50]
fontSize = IntVar()
sizeOption = OptionMenu(menuFrame,fontSize,*sizes,command=changeFont)
fontSize.set(12)
sizeOption.config(width=5)
sizeOption.grid(row=0,column=5,padx=5,pady=5)

styles = ["none","bold","italic"]
fontstyle = StringVar()
styleOption = OptionMenu(menuFrame,fontstyle,*styles,command=changeFont)
fontstyle.set("none")
styleOption.config(width=10)
styleOption.grid(row=0,column=6,padx=5,pady=5)
                 
#scroll text 

myFont = (fontfamily.get(),fontSize.get())
textArea = scrolledtext.ScrolledText(textFrame,bg=text_color,font=myFont,width=1000,height = 1000)
textArea.pack()

root.mainloop()