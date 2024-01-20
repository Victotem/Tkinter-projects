from tkinter import *



window = Tk()
window.title("Parking Tkinter")
window.minsize(width=300, height=200)
window.config(padx=100,pady=0)

def button_clicked():
    
    
    label1.configure(text=f"Tu numero de plaza es [plaza]")
def button_clicked2():
    
    
    label2.configure(text=f"Tu numero de plaza es [plaza]")
  
    


label1 = Label(text="Zona Cliente",font=("Arial",18,"bold"))
label1.grid(column=0,row=1)



button=Button(text="Siguiente",command=button_clicked)
button.grid(column=0,row=3)


label2 = Label(text="Zona Aministrador",font=("Arial",18, "bold"))
label2.grid(column=0,row=4)

button2=Button(text="Siguiente",command=button_clicked2)
button2.grid(column=0,row=5)







    



window.mainloop()