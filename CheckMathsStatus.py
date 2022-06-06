from tkinter import *
import mysql.connector
def MathsCheck():
 newWindow = Tk() 
 newWindow.title("Check Maths Status") 
 newWindow.geometry("1000x1000")


 
 mydb = mysql.connector.connect(host="localhost",user="root", passwd="root",database="revision")
 mycursor = mydb.cursor()

 mycursor.execute("SELECT * FROM maths limit 0,14")
 i=0 
 for chapters in mycursor: 
    for j in range(len(chapters)):
        e = Entry(newWindow, width=10, fg='blue') 
        e.grid(row=i, column=j, pady= 10, ipadx=80, ipady=5) 
        e.insert(END, chapters[j])
        
    i=i+1
 Exit= Button(newWindow, text="EXIT", height=2, width= 20, command= newWindow.destroy)
 Exit.place(x=700,y=400)

 newWindow.mainloop()
