from tkinter import*
from CheckStatus import*
from update import*

newWindow = Tk()
newWindow.title("MY REVISION STATUS") 
newWindow.geometry("700x600")

l1= Label(newWindow, text= 'MY REVISION STATUS', anchor= CENTER)
b1= Button(newWindow, height= 2, width= 40, text= 'CHECK COMPLETION', command= Check)
b2= Button(newWindow, height= 2, width= 40, text='UPDATE COMPLETION', command= Update)
b3=Button(newWindow, height= 2, width= 20, text= 'EXIT', command=newWindow.destroy)

l1.place(x=300,y=40)
b1.place(x=50,y=300)
b2.place(x=400,y=300)
b3.place(x=350,y=400)

newWindow.mainloop()


