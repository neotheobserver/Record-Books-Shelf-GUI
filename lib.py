from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk
import os,sys

#initialize and define screen values
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root=Tk()
root.title('Jyoti-Narayan-Library')
'''width=1024
height=720
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x=(screen_width/2)-(width/2)
y=(screen_height/2)-(height/2)
root.geometry("%dx%d+%d+%d"%(width,height,x,y))'''
root.geometry("1280x720")

#root.resizable(1.12,1.12)
#root.config(bg="#800000")

#variables
USERNAME=StringVar()
PASSWORD=StringVar()
TITLE=StringVar()
AUTHOR=StringVar()
GENRE=StringVar()
YEAR=StringVar()
SHELF_NO=StringVar()
SEARCH=StringVar()
UPDATE=IntVar()

#methods to database query
def Database():
    global conn,cursor
    conn=sqlite3.connect('data.db')
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS admin(admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,username TEXT,password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT,year VARCHAR(8),shelf_no VARCHAR(4),genre TEXT)")
    cursor.execute("SELECT * FROM admin WHERE username='admin' AND password ='admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO admin(username,password) VALUES('admin','admin')")
        conn.commit()

#exit screen functionality
def Exit():
    result=tkMessageBox.askquestion('Jyoti-Narayan-Library','Do you want to exit?',icon='warning')
    if result=='yes':
        root.destroy()
        exit()

def Exit2():
    result=tkMessageBox.askquestion('Jyoti-Narayan-Libray','Do you want to exit?',icon='warning')
    if result=='yes':
        Home.destroy()
        exit()

#show login form
def ShowLoginForm():
    global loginform
    loginform=Toplevel()
    loginform.title("Jyoti-Narayan-Library/Account_Login")
    width=600
    height=500
    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()
    x=(screen_width/2)-(width/2)
    y=(screen_height/2)-(height/2)
    loginform.resizable(0,0)
    loginform.geometry("%dx%d+%d+%d"%(width,height,x,y))
    LoginForm()

#function for login form
def LoginForm():
    global lbl_result
    TopLoginForm=Frame(loginform,width=600,height=100,bd=1,relief=SOLID)
    TopLoginForm.pack(side=TOP,pady=20)
    lbl_text=Label(TopLoginForm,text='Admin Login',font=('arial',18),width=600)
    lbl_text.pack(fill=X)
    MidLoginForm=Frame(loginform,width=600)
    MidLoginForm.pack(side=TOP,pady=50)
    lbl_username=Label(MidLoginForm,text="Username:",font=('arial',25),bd=18)
    lbl_username.grid(row=0)
    lbl_password=Label(MidLoginForm,text="Password:",font=('arial',25),bd=18)
    lbl_password.grid(row=1)
    lbl_result=Label(MidLoginForm,text='',font=('arial',18))
    lbl_result.grid(row=3,columnspan=2)
    username=Entry(MidLoginForm,textvariable=USERNAME,font=('arial',25),width=15)
    username.grid(row=0,column=1)
    password=Entry(MidLoginForm,textvariable=PASSWORD,font=('arial',25),width=15,show='*')
    password.grid(row=1,column=1)
    btn_login=Button(MidLoginForm,text='Login',font=('arial',18),width=30,command=Login)
    btn_login.grid(row=2,columnspan=2,pady=20)
    btn_login.bind('<Return>',Login)

#Home Screen
def Home():
    global Home
    Home=Tk()
    Home.title("Jyoti-Narayan-Library/Home")
    width=1024
    height=720
    screen_width=Home.winfo_screenwidth()
    screen_height=Home.winfo_screenheight()
    x=(screen_width/2)-(width/2)
    y=(screen_height/2)-(height/2)
    Home.geometry("%dx%d+%d+%d"%(width,height,x,y))
    #Home.resizable(0,0)
    Title=Frame(Home,bd=2,relief=SOLID)
    Title.pack(pady=10)
    lbl_display=Label(Title,text="Jyoti-Narayan-Library",font=('arial',45))
    lbl_display.pack()
    menubar=Menu(Home)
    filemenu=Menu(menubar,tearoff=0)
    filemenu1=Menu(menubar,tearoff=0)
    #filemenu.add_command(label='Logout',command=Logout)
    filemenu.add_command(label='Exit',command=Exit2)
    filemenu1.add_command(label='Add Entry',command=ShowAddNew)
    filemenu1.add_command(label='Update Entry',command=UpdateNew)
    filemenu1.add_command(label='View All',command=ShowView)
    menubar.add_cascade(label='Account',menu=filemenu)
    menubar.add_cascade(label='Database',menu=filemenu1)
    Home.config(menu=menubar)
    Home.config(bg="DarkBlue")

#Add new data
def ShowAddNew():
    global addnewform
    addnewform=Toplevel()
    addnewform.title("Jyoti-Narayan-Library/New Entry")
    width=600
    height=600
    screen_width=Home.winfo_screenwidth()
    screen_height=Home.winfo_screenheight()
    x=(screen_width/2)-(width/2)
    y=(screen_height/2)-(height/2)
    addnewform.geometry("%dx%d+%d+%d"%(width,height,x,y))
    addnewform.resizable(0,0)
    AddNewForm()

#frame for new data
def AddNewForm():
    TopAddNew=Frame(addnewform,width=600,height=100,bd=1,relief=SOLID)
    TopAddNew.pack(side=TOP,pady=20)
    lbl_text=Label(TopAddNew,text="Add New Entry",font=('arial',18),width=600)
    lbl_text.pack(fill=X)
    MidAddNew=Frame(addnewform,width=600)
    MidAddNew.pack(side=TOP,pady=50)
    lbl_title=Label(MidAddNew,text='TITLE',font=('arial',25),bd=10)
    lbl_title.grid(row=0,sticky=W)
    lbl_author=Label(MidAddNew,text='AUTHOR',font=('arial',25),bd=10)
    lbl_author.grid(row=1,sticky=W)
    lbl_year=Label(MidAddNew,text='YEAR_PUBLISHED',font=('arial',25),bd=10)
    lbl_year.grid(row=2,sticky=W)
    lbl_shelf=Label(MidAddNew,text='SHELF_NO',font=('arial',25),bd=10)
    lbl_shelf.grid(row=3,sticky=W)
    lbl_genre=Label(MidAddNew,text='GENRE',font=('arial',25),bd=10)
    lbl_genre.grid(row=4,sticky=W)
    title=Entry(MidAddNew,textvariable=TITLE,font=('arial',25),width=15)
    title.grid(row=0,column=1)
    author=Entry(MidAddNew,textvariable=AUTHOR,font=('arial',25),width=15)
    author.grid(row=1,column=1)
    year=Entry(MidAddNew,textvariable=YEAR,font=('arial',25),width=15)
    year.grid(row=2,column=1)
    shelf=Entry(MidAddNew,textvariable=SHELF_NO,font=('arial',25),width=15)
    shelf.grid(row=3,column=1)
    genre=Entry(MidAddNew,textvariable=GENRE,font=('arial',25),width=15)
    genre.grid(row=4,column=1)
    btn_add=Button(MidAddNew,text="Save",font=('arial',18),width=30,bg='#009ACD',command=AddNew)
    btn_add.grid(row=5,columnspan=2,pady=20)

def AddNew():
    Database()
    cursor.execute("INSERT INTO book VALUES(NULL,?,?,?,?,?)",(TITLE.get(),AUTHOR.get(),YEAR.get(),SHELF_NO.get(),GENRE.get()))
    conn.commit()
    TITLE.set('')
    AUTHOR.set('')
    YEAR.set('')
    SHELF_NO.set('')
    GENRE.set('')
    cursor.close()
    conn.close()

def UpdateNew():
    global updatenewform
    updatenewform=Toplevel()
    updatenewform.title("Jyoti-Narayan-Library/Update Entry")
    width=600
    height=600
    screen_width=Home.winfo_screenwidth()
    screen_height=Home.winfo_screenheight()
    x=(screen_width/2)-(width/2)
    y=(screen_height/2)-(height/2)
    updatenewform.geometry("%dx%d+%d+%d"%(width,height,x,y))
    updatenewform.resizable(0,0)
    UpdateForm()

#frame for new data
def UpdateForm():
    TopAddNew=Frame(updatenewform,width=600,height=100,bd=1,relief=SOLID)
    TopAddNew.pack(side=TOP,pady=20)
    lbl_text=Label(TopAddNew,text="Update Entry",font=('arial',18),width=600)
    lbl_text.pack(fill=X)
    MidAddNew=Frame(updatenewform,width=600)
    MidAddNew.pack(side=TOP,pady=50)
    lbl_title=Label(MidAddNew,text='TITLE',font=('arial',25),bd=10)
    lbl_title.grid(row=0,sticky=W)
    lbl_author=Label(MidAddNew,text='AUTHOR',font=('arial',25),bd=10)
    lbl_author.grid(row=1,sticky=W)
    lbl_year=Label(MidAddNew,text='YEAR_PUBLISHED',font=('arial',25),bd=10)
    lbl_year.grid(row=2,sticky=W)
    lbl_shelf=Label(MidAddNew,text='SHELF_NO',font=('arial',25),bd=10)
    lbl_shelf.grid(row=3,sticky=W)
    lbl_genre=Label(MidAddNew,text='GENRE',font=('arial',25),bd=10)
    lbl_genre.grid(row=4,sticky=W)
    lbl_update=Label(MidAddNew,text='ID TO UPDATE',font=('arial',25),bd=10)
    lbl_update.grid(row=5,sticky=W)
    title=Entry(MidAddNew,textvariable=TITLE,font=('arial',25),width=15)
    title.grid(row=0,column=1)
    author=Entry(MidAddNew,textvariable=AUTHOR,font=('arial',25),width=15)
    author.grid(row=1,column=1)
    year=Entry(MidAddNew,textvariable=YEAR,font=('arial',25),width=15)
    year.grid(row=2,column=1)
    shelf=Entry(MidAddNew,textvariable=SHELF_NO,font=('arial',25),width=15)
    shelf.grid(row=3,column=1)
    genre=Entry(MidAddNew,textvariable=GENRE,font=('arial',25),width=15)
    genre.grid(row=4,column=1)
    update=Entry(MidAddNew,textvariable=UPDATE,font=('arial',25),width=15)
    update.grid(row=5,column=1)
    btn_add=Button(MidAddNew,text="Update",font=('arial',18),width=30,bg='#009ACD',command=Update)
    btn_add.grid(row=6,columnspan=2,pady=20)

def Update():
    Database()
    cursor.execute("UPDATE book SET title=?, author=?, year=?, shelf_no=?, genre=? WHERE id=?",(TITLE.get(),AUTHOR.get(),YEAR.get(),SHELF_NO.get(),GENRE.get(),UPDATE.get()))
    conn.commit()
    TITLE.set('')
    AUTHOR.set('')
    YEAR.set('')
    SHELF_NO.set('')
    GENRE.set('')
    cursor.close()
    conn.close()

#View the data
def ViewForm():
    global tree
    TopViewForm=Frame(viewform,width=600,bd=1,relief=SOLID)
    TopViewForm.pack(side=TOP,fill=X)
    LeftViewForm=Frame(viewform,width=600)
    LeftViewForm.pack(side=LEFT,fill=X)
    MidViewForm=Frame(viewform,width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text=Label(TopViewForm,text="View Data",font=('arial',18),width=1280)
    lbl_text.pack(side=RIGHT)
    lbl_textsearch=Label(LeftViewForm,text='Search',font=('arial',15))
    lbl_textsearch.pack(side=TOP,anchor=W)
    search=Entry(LeftViewForm,textvariable=SEARCH,font=('arial',15),width=25)
    search.pack(side=TOP,padx=25,pady=25,fill=X)
    btn_search=Button(LeftViewForm,text="Search",command=Search)
    btn_search.pack(side=TOP,padx=20,pady=20,fill=BOTH)
    btn_reset=Button(LeftViewForm,text="Reset",command=Reset)
    btn_reset.pack(side=TOP,padx=20,pady=20,fill=BOTH)
    btn_delete=Button(LeftViewForm,text="Delete",command=Delete)
    btn_delete.pack(side=TOP,padx=20,pady=20,fill=BOTH)
    scrollbarx=Scrollbar(MidViewForm,orient=HORIZONTAL)
    scrollbary=Scrollbar(MidViewForm,orient=VERTICAL)
    tree=ttk.Treeview(MidViewForm,columns=('ID','TITLE','AUTHOR','YEAR_PUBLISHED','SHELF_NO','GENRE'),selectmode='extended',height=720,yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT,fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM,fill=X)

    tree.heading('ID',text='ID',anchor='w')
    tree.heading('TITLE',text='TITLE',anchor='w')
    tree.heading('AUTHOR',text='AUTHOR',anchor='w')
    tree.heading('YEAR_PUBLISHED',text='YEAR_PUBLISHED',anchor='w')
    tree.heading('SHELF_NO',text='SHELF_NO',anchor='w')
    tree.heading('GENRE',text='GENRE',anchor='w')
    tree.column('#0',stretch=False,minwidth=0,width=0)
    tree.column('#1',stretch=False,minwidth=0,width=50)
    tree.column('#2',stretch=True,minwidth=0,width=400)
    tree.column('#3',stretch=True,minwidth=0,width=300)
    tree.column('#4',stretch=True,minwidth=0,width=150)
    tree.column('#5',stretch=False,minwidth=0,width=100)
    tree.column('#6',stretch=False,minwidth=0,width=200)
    tree.pack()
    DisplayData()

def DisplayData():
    Database()
    cursor.execute("SELECT * FROM book ORDER BY title COLLATE NOCASE")
    fetch=cursor.fetchall()
    for data in fetch:
        tree.insert('','end',values=(data))
    cursor.close()
    conn.close()

def Search():
    if SEARCH.get()!='':
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM book WHERE title LIKE? COLLATE NOCASE OR author LIKE? COLLATE NOCASE OR year LIKE?",('%'+SEARCH.get()+'%','%'+SEARCH.get()+'%',SEARCH.get()+'%',))
        fetch=cursor.fetchall()
        for data in fetch:
            tree.insert('','end',values=(data))
        cursor.close()
        conn.close()

def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")

def Delete():
    if not tree.selection():
        tkMessageBox.showinfo('Jyoti-Narayan-Library','Please select something to delete!',icon='warning')
    else:
        result=tkMessageBox.askquestion('Jyoti-Narayan-Library','Do you want to delete?',icon='warning')
        if result=='yes':
            curItem=tree.focus()
            contents=(tree.item(curItem))
            selecteditem=contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM book WHERE ID=%d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

def ShowView():
    global viewform
    viewform=Toplevel()
    viewform.title("Jyoti-Narayan-Library/View Books")
    width=1280
    height=720
    screen_width=Home.winfo_screenwidth()
    screen_height=Home.winfo_screenheight()
    x=(screen_width/2)-(width/2)
    y=(screen_height/2)-(height/2)
    viewform.geometry("%dx%d+%d+%d"%(width,height,x,y))
    #viewform.resizable(0,0)
    ViewForm()

#login and logout function
'''def Logout():
    result=tkMessageBox.askquestion("Jyoti-Narayan-Library","Are you sure?",icon='warning')
    if result=='yes':
        admin_id=''
        Home.deiconify()
        Home.destroy()'''

def Login(event=None):
    global admin_id
    Database()
    if USERNAME.get=='' or PASSWORD.get()=='':
        lbl_result.config(text="Please Complete the required field!",fg='red')
    else:
        cursor.execute("SELECT * FROM admin WHERE username=? AND password=?",(USERNAME.get(),PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM admin WHERE username=? AND password=?",(USERNAME.get(),PASSWORD.get()))
            data=cursor.fetchone()
            admin_id=data[0]
            USERNAME.set('')
            PASSWORD.set('')
            lbl_result.config(text='')
            ShowHome()
        else:
            lbl_result.config(text='Invalid username or password',fg='red')
            USERNAME.set('')
            PASSWORD.set('')
    cursor.close()
    conn.close()

def ShowHome():
    root.withdraw()
    Home()
    loginform.destroy()

#widgets and initialization
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label='Account',command=ShowLoginForm)
filemenu.add_command(label='Exit',command=Exit)
menubar.add_cascade(label='File',menu=filemenu)
root.config(menu=menubar)

Title=Frame(root,bd=1,relief=SOLID)
Title.pack(pady=10)

pic=PhotoImage(file=resource_path('lib.gif'))
lbl=Label(image=pic)
lbl.image=pic
lbl.pack()

lbl_display=Label(Title,text='JYOTI NARAYAN DBMS',font=('arial',60))
lbl_display.pack()

if __name__ =='__main__':
    root.mainloop()
