from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def recipeRegister():
    
    recipe_id = recipeInfo1.get()
    Name = recipeInfo2.get()
    Ingredients = recipeInfo3.get()
    Instructions = recipeInfo4.get()
    Instructions = Instructions.lower()
    
    insertRecipe = "insert into "+recipeTable+" values('"+recipe_id+"','"+Name+"','"+Ingredients+"','"+Instructions+"')"
    try:
        cur.execute(insertRecipe)
        con.commit()
        messagebox.showinfo('Success',"Recipe added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(recipe_id)
    print(Name)
    print(Ingredients)
    print(Instructions)


    root.destroy()
    
def addRecipe(): 
    
    global recipeInfo1,recipeInfo2,recipeInfo3,recipeInfo4,Canvas1,con,cur,recipeTable,root
    
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
    recipeTable = "recipe"
    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Recipes", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Recipe ID
    lb1 = Label(labelFrame,text="Recipe ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    recipeInfo1 = Entry(labelFrame)
    recipeInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Name
    lb2 = Label(labelFrame,text="Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    recipeInfo2 = Entry(labelFrame)
    recipeInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Ingredients
    lb3 = Label(labelFrame,text="Ingredients : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    recipeInfo3 = Entry(labelFrame)
    recipeInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Instructions
    lb4 = Label(labelFrame,text="Instructions : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    recipeInfo4 = Entry(labelFrame)
    recipeInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=recipeRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
