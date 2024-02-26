from tkinter import *
def callback(event):
    global move
    if event.keysym=='Right':
        move += 1
    elif event.keysym=='Left':
        move -=1
    canvas.coords(rect,50+move,50,100+move,100)
root = Tk()
root.bind('<Key>', callback)
canvas = Canvas(width=200,height=200)
canvas.grid(row=0,column=0)
rect = canvas.create_rectangle(50,50,100,100,fill='blue')
move = 0
mainloop()
