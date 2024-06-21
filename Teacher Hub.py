from tkinter import *

def funResizeText(event):
    global relative_fontsize
    
    w = 0.42 * event.width / 1920
    h = 0.42 * event.height / 1017
    
    new_relative_fontsize = max(w, h)
    
    for widget in Win.winfo_children():
        if isinstance(widget, Label):
            print(widget.cget("font"))
            widget.config(font = (widget.cget("font"), new_relative_fontsize * widget.cget("font") / relative_fontsize))
    
    relative_fontsize = new_relative_fontsize

Win = Tk()
Win.bind("<Configure>", funResizeText)

relative_fontsize = 0.42

def TeacherHub():
    # Changes the background
    Win.config(bg = "light blue")
    
    # Creates a label
    txtHello = Label(bg = "dark blue", relief = "solid", borderwidth = 3, text = "Hello Test Account!", font = ("Arial", int(100 * relative_fontsize)))
    txtHello.place(relwidth = 1, relheight = 0.1, relx = 0.5, rely = 0.05, anchor = "center")
    
    btnExit = Button(background = "red", text = "X", height = 1, width = 3)
    btnExit.place(relx = 0.99, rely = 0.015, anchor = CENTER)
    
    Win.mainloop()

TeacherHub()