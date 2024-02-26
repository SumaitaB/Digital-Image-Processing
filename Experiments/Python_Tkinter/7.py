from tkinter import *
root = Tk()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
buttons = [0]*26
for i in range(26):
    buttons[i] = Button(text=alphabet[i])
    buttons[i].grid(row=0, column=i)
ok_button = Button(text='Ok', font=('Verdana', 24))
ok_button.grid(row=1, column=0)
mainloop()

