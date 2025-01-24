from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddRecipe import *
from DeleteRecipe import *
from ViewRecipe import *
from IngSubs import *
from Measurements import *
from UserLog import *
from Feedback import *
from ViewUser import *

# Add your own database name and password here to reflect in the code
mypass = "0000"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("RECIPE DATABASE")
root.minsize(width=400,height=400)
root.geometry("600x500")

# Take n greater than 0.25 and less than 5
same=True
n=1.10

# Adding a background image
background_image =Image.open("cook.jpeg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*(n+0.90))
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="grey",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n Cooking Recipe Database", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="User Log",bg='black', fg='white', command = addUser)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.06)

btn2 = Button(root,text="View User Log",bg='black', fg='white', command = View4)
btn2.place(relx=0.28,rely=0.46, relwidth=0.45,relheight=0.06)

btn3 = Button(root,text="Add Recipe",bg='black', fg='white', command=addRecipe)
btn3.place(relx=0.28,rely=0.52, relwidth=0.45,relheight=0.06)
    
btn4 = Button(root,text="Delete Recipe",bg='black', fg='white', command=delete)
btn4.place(relx=0.28,rely=0.58, relwidth=0.45,relheight=0.06)
    
btn5 = Button(root,text="View Recipe List",bg='black', fg='white', command=View)
btn5.place(relx=0.28,rely=0.64, relwidth=0.45,relheight=0.06)
    
btn6 = Button(root,text="Ingredient Substitution",bg='black', fg='white', command = View2)
btn6.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.06)
    
btn7 = Button(root,text="Standard Measurements",bg='black', fg='white', command = View3)
btn7.place(relx=0.28,rely=0.76, relwidth=0.45,relheight=0.06)

btn8 = Button(root,text="Feedback",bg='black', fg='white', command = addFeedback)
btn8.place(relx=0.28,rely=0.82, relwidth=0.45,relheight=0.06)

root.mainloop()
