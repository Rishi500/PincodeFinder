import json
from tkinter import *
from tkinter import ttk
data = json.load(open("indiapincodes.json"))

def search_city():
    list1.delete(0,END)
    list2.delete(0,END)
    s1 = str(e1.get())
    s1=s1.lower()
    s1=s1.title()
    flag=0
    for i in data['city']:
        if str(i['taluk']) == str(s1):
            if str(i['districtName']==str(s1)):
                s2="                          "+str(i['officeName'])
                s2=s2+", "+str(i['taluk'])
                s2= s2+", "+str(i['pincode'])
                s2 =s2+", "+str(i['stateName'])+"."
                list1.insert(END,s2)
                flag=1


    if flag==0:
        list2.insert(0,"Please Enter correct City")
def clear_search():
    e1.delete(0,END)
    list1.delete(0,END)
    list2.delete(0,END)

window=Tk()
window.title("Pincode & City Search App")
window.configure(bg="#e0e2e5")

l1=Label(window,text="Enter the city to search Pincode & State")
l1.grid(row=0,column=0)

l2=Label(window,text="The Pincode and State is :")
l2.grid(row=3,column=0,columnspan=10)

l3=Label(window,text="Message :")
l3.grid(row=8,column=0,columnspan=10)


l4=Label(window,text="About :")
l4.grid(row=12,column=0,columnspan=10)

scrollbar = Scrollbar(window)
scrollbar.grid(row=5,column=10)

scity=StringVar()
global e1
e1=Entry(window,width=60,textvariable=scity)
e1.grid(row=0,column=5,columnspan=5)

b1=ttk.Button(window,text="Find Pincode.",command=search_city)
b1.grid(row=1,column=5,columnspan=2)


b2=ttk.Button(window,text="Clear ",command=clear_search)
b2.grid(row=1,column=8,columnspan=2)

global list1
global list2
list1=Listbox(window, height=10, width=120)
list1.grid(row=5,column=0, rowspan=1,columnspan=10)
list1.insert(0,"")

list1.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list1.yview)
list2=Listbox(window, height=2, width=60)
list2.grid(row=10,column=0, rowspan=1,columnspan=10)
list2.insert(0,"")

l5=Label(window, text="--This software is Developed by Rishi Jain--")
l5.grid(row=13,column=0, rowspan=1,columnspan=10)

window.mainloop()
