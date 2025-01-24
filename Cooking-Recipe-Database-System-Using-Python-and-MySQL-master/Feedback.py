from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def feedbackRegister():
    
    user_id = feedbackInfo1.get()
    user_name = feedbackInfo2.get()
    fdb = feedbackInfo3.get()
       
    insertFeedback = "insert into "+feedbackTable+" values('"+user_id+"','"+ user_name+"','"+fdb+"')"
    try:
        cur.execute(insertFeedback)
        con.commit()
        messagebox.showinfo('Success',"Feedback added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    root.destroy()
    
def addFeedback(): 
    
    global feedbackInfo1,feedbackInfo2,feedbackInfo3,Canvas1,con,cur,feedbackTable,root
    
    root = Tk()
    root.title("Recipe Database")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your database name and password here
    mypass = "0000"
    mydatabase="db"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    feedbackTable = "feedback"
    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Give Feedback", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # User ID
    lb1 = Label(labelFrame,text="User ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    feedbackInfo1 = Entry(labelFrame)
    feedbackInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Name
    lb2 = Label(labelFrame,text="User Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    feedbackInfo2 = Entry(labelFrame)
    feedbackInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Feedback
    lb3 = Label(labelFrame,text="Feedback : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    feedbackInfo3 = Entry(labelFrame)
    feedbackInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=feedbackRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
