from tkinter import*
import mysql.connector
from tkinter import messagebox

def UpdatePhysics():
 newWindow = Tk()
 newWindow.title("Update Physics Status") 
 newWindow.geometry("700x600")

 def update():
      Output.delete("1.0", "end-1c")
      try:
       chapter_number = int(CHAP_NO.get("1.0", "end-1c"))      
      except ValueError:
       messagebox.showwarning("ERROR","PLEASE ENTER CHAPTER NUMBER IN NUMERIC FORM", parent=newWindow)
     
      else:    
       mydb = mysql.connector.connect(host="localhost", port= "3306", user="root", passwd="root",database="revision")
       mycursor = mydb.cursor()
       mycursor.execute("SELECT * FROM physics where CHAP_NO = '{0}'" .format(chapter_number))
       result= mycursor.fetchall()

     
       
       if len(result) == 0:
        Output.insert(END, "There are no CHAPTERS with CHAPTER NUMBER {0}" .format(chapter_number))
       else:
        result = messagebox.askquestion("Updating Confirmation","Do you want to set CHAP_NO {0} as completed?".format(chapter_number), icon="info",parent=newWindow)
        if result == 'yes':
         mycursor = mydb.cursor()
         mycursor.execute("update physics set STATUS= 'COMPLETED' where CHAP_NO= '{0}'" .format(chapter_number))
         mydb.commit()
         Output.insert(END,"Status Updated")
        else:
         Output.insert(END,"operation aborted")
         
         
 l1=Label(newWindow, text="ENTER CHAPTER NUMBER")
 l2= Label(newWindow, text="OUTPUT-")
 CHAP_NO= Text(newWindow, height= 2, width= 5, bg= 'light yellow')
 b1= Button(newWindow, text= "UPDATE", height= 5, width= 20, command= update)
 b2= Button(newWindow, text= "EXIT", height= 5, width= 20, command= newWindow.destroy)
 Output= Text(newWindow, height= 5, width= 50, bg="light yellow")
 l1.place(x=50,y=20)
 l2.place(x=50,y=80)
 CHAP_NO.place(x=200,y=20)
 b1.place(x=50,y=250)
 b2.place(x=400,y=250)
 Output.place(x=100,y=80)
 
 
 newWindow.mainloop()





       
