from tkinter import *
from UpdatePhysicsStatus import*
from UpdateMathsStatus import*
from UpdateChemistryStatus import*

def Update():
 newWindow = Tk()
 newWindow.title("Update Status") 
 newWindow.geometry("700x600")

 physics = Button(newWindow, height = 2, width = 20, text = 'PHYSICS',command= UpdatePhysics)
 chemistry = Button(newWindow, height = 2, width = 20, text = 'CHEMISTRY', command= UpdateChemistry)
 maths = Button(newWindow, height = 2, width = 20, text= 'MATHS', command= UpdateMaths)
 Exit = Button(newWindow, height = 2, width = 20, text ="Exit",command=newWindow.destroy)

 l1 = Label(newWindow,text='MY REVISION STATUS',anchor = CENTER)

 physics.place(x=100,y=300)
 chemistry.place(x=300,y=300)
 maths.place(x=500,y=300)
 Exit.place(x=300,y=400)
 l1.place(x=300,y=40)
 mainloop()


