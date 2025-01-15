from tkinter import* 

window=Tk()

window.title("event handler")
window.geometry("100x100")

def hand_keypress(event):
    print(event.char)
window.bind("<Key>",hand_keypress)

def hand_click(event):
    print("button is clicked ")

button=Button(text="click me")
button.pack()
button.bind("<Button-1>",hand_click)

window.mainloop()