from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here
mypass = "0000"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here 
recipeTable = "recipe" 
userTable = "user_log"

def deleteRecipe():
    
    bid = recipeInfo1.get()
    
    deleteSql = "delete from "+recipeTable+" where recipe_id = '"+bid+"'"
    deleteLog = "delete from "+userTable+" where recipe_id = '"+bid+"'"

    try:
        cur.execute(deleteSql)
        con.commit()
        
        cur.execute(deleteLog)
        con.commit()
        
        messagebox.showinfo('Success',"Recipe Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Recipe ID")

    #trig="DELIMITER // CREATE TRIGGER del_rec BEFORE DELETE ON"+recipeTable+"
    #FOR EACH ROW IF NEW.Recipe_id NOT IN(select * from "+recipeTable+" )THEN SIGNAL SQLSTATE '45000' STE MESSAGE_TEXT = 'Check Recipe ID' END IF
    #// DELIMETER"

    #cursor.execute("Drop trigger if exists mytrigger")
    #trigger= 'CREATE TRIGGER mytrigger BEFORE DELETE ON "+recipeTable+" FOR EACH ROW'
    #BEGIN
    #SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='NOT ALLOWED'
    #END
    #cursor.execute(trigger)
        

    recipeInfo1.delete(0, END)
    root.destroy()
    
def delete(): 
    
    global recipeInfo1,recipeInfo2,recipeInfo3,recipeInfo4,Canvas1,con,cur,recipeTable,root
    
    root = Tk()
    root.title("Recipe Database")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Recipe", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Recipe ID to Delete
    lb2 = Label(labelFrame,text="Recipe ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    recipeInfo1 = Entry(labelFrame)
    recipeInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteRecipe)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
