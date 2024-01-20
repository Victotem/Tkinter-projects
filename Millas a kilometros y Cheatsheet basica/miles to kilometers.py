from tkinter import *



window = Tk()
window.title("Miles to kilometers")
window.minsize(width=300, height=200)
window.config(padx=100,pady=0)

def button_clicked():
    miles=float(input.get())
    km= miles* 1.609
    label2.configure(text=f"The number of km/s is {km}")
  
    


label1 = Label(text="Insert miles here",font=("Arial",18,"bold"))
label1.grid(column=0,row=1)

input=Entry(width=7)
input.grid(column=0,row=2)

button=Button(text="Convert",command=button_clicked)
button.grid(column=0,row=3)


label2 = Label(text="",font=("Arial",12))
label2.grid(column=0,row=4)





    



window.mainloop()