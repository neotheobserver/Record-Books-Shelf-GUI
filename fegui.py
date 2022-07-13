"""
A program that stores book information:
Title, Author, Year, ISBN
User can: View, Search, Add, Update, Delete, and Close

"""
from tkinter import *
import besqlite

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except:
        pass



def view_command():
    list1.delete(0,END)
    for row in besqlite.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in besqlite.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def insert_command():
    besqlite.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def delete_command():
    besqlite.delete(selected_tuple[0])

def update_command():
    besqlite.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

box=Tk()

box.wm_title("Book database")

l1=Label(box,text="Title")
l1.grid(row=0,column=0)

l2=Label(box,text="Author")
l2.grid(row=0,column=2)

l3=Label(box,text="Year")
l3.grid(row=1,column=0)

l4=Label(box,text="ISBN")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(box,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(box,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(box,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(box,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1=Listbox(box, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(box)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(box,text='View all',width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(box,text='Search entry',width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(box,text='add entry',width=12,command=insert_command)
b3.grid(row=4,column=3)

b4=Button(box,text='update',width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(box,text='delete',width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(box,text='close',width=12,command=box.destroy)
b6.grid(row=7,column=3)



box.mainloop()
