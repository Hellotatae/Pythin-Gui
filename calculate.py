import sys
from tkinter import Tk, simpledialog , messagebox

def Calculate(width,height):
    area = (width * height)
    return area

root = Tk()
root.withdraw()
root.geometry("500x500")
simpledialog.askstring

while True:
    g = simpledialog.askstring("Area calculator", "Enter Width :")
    t = simpledialog.askstring("Area calculator", "Wnter height :")
    a = str(Calculate(g,t))
    messagebox.showinfo("ans","Area of the rectangle is :" + a)

    quit = simpledialog.askstring('continue',"Do you want to exit program ? (yes/no) : ")
    if quit.lower() == "yes":
        messagebox.showinfo("finish","Thankyou for calculate")
        root.destroy
        sys.exit()