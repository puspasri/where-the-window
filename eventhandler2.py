from tkinter import*
from tkinter import messagebox



window=Tk()
window.title("welcome")
window.geometry("200x200")

def msg():
    messagebox.showwarning("Alert","stop there is a virus found.")

button=Button(window,text="test",command=msg)
button.place(x=50,y=50)
window.mainloop()