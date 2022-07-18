from tkinter import Tk,Label
import time
root=Tk()
root.title("timer")
root.geometry("420x150")
l=Label(root)
l.grid(row=5,column=5)
border_width=25
text_font=("boulder",68,'bold')
background='#f2e750'
foreground='#363529'
def timeur():
    time_now=time.strftime("%H:%M:%S")
    l.config(text=time_now,font=text_font,bg=background,fg=foreground,bd=border_width)
    l.after(200,timeur)
timeur()
















root.mainloop()
