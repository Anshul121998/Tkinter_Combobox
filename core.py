from tkinter import *
import tkinter as tk 
from tkinter import ttk
import pandas as pd

# Creating tkinter window 
window = tk.Tk() 
window.title('Dropdown') 
window.geometry('500x250') 
  
# Combobox creation 
n = tk.StringVar() 
dropdown_menu = ttk.Combobox(window, width = 10, textvariable = n) 

o = tk.StringVar() 
dropdown_menu1 = ttk.Combobox(window, width = 10, textvariable = o)

p = tk.StringVar() 
dropdown_menu2 = ttk.Combobox(window, width = 10, textvariable = p)


q = tk.StringVar() 
dropdown_menu3 = ttk.Combobox(window, width = 10, textvariable = q)

r = tk.StringVar() 
dropdown_menu4 = ttk.Combobox(window, width = 10, textvariable = r)

#dependent drop down list function
def callback(eventObject):
    abc = eventObject.widget.get()
    car = dropdown_menu1.get()
    index=dropdown_menu1.index(car)
    dropdown_menu2.config(values=dropdown_menu2[index])


dropdown_menu2.bind('<Button-1>', callback)

  
# Adding combobox drop down list 
dropdown_menu['values'] = ('A',  
                          'B', 
                          'C', 
                          'D', 
                          'E',) 
  
dropdown_menu.grid(column = 1, row = 0) 

#Label and Dropdown Section
# Label1 
ttk.Label(window, text = "Label1",font = ("Times New Roman", 10)).grid(column = 0,row = 1) 

# Combobox1
dropdown_menu1 = ttk.Combobox(window, width = 10, textvariable = o) 
dropdown_menu1['values'] = (['Australia','India', 'USA'])

#brands = ["Bugatti","VW","Opel","Porsche"]


dropdown_menu1.grid(column = 1, row = 1) 
# Label2 
ttk.Label(window, text = "Label2",font = ("Times New Roman", 10)).grid(column = 2,row = 1) 

# Combobox2
dropdown_menu2 = ttk.Combobox(window, width = 10, textvariable = p) 
dropdown_menu2['values'] = ([["Tasmania","New South Wales","Queensland"],
          ["UttarPradesh","Maharashtra","Rajasthan"],
          ["Florida","California","Texas"]]) 
  
dropdown_menu2.grid(column = 3, row = 1) 

# Label3 
ttk.Label(window, text = "Label3",font = ("Times New Roman", 10)).grid(column = 4,row = 1) 

# Combobox3
dropdown_menu3 = ttk.Combobox(window, width = 10, textvariable = q) 
dropdown_menu3['values'] = ([[["Hobart"],["Sydney"],["Brisbane"]],
          [["Lucknow"],["Mumbai"],["Jaipur"]],
          [["Tallahassee"],["Sacramento"],["Austin"]]]) 
  
dropdown_menu3.grid(column = 5, row = 1) 

# Label4 
ttk.Label(window, text = "Label4",font = ("Times New Roman", 10)).grid(column = 6,row = 1) 


# Combobox4
dropdown_menu4 = ttk.Combobox(window, width = 7, textvariable = r) 
dropdown_menu4['values'] = ('A',  
                          'B', 
                          'C', 
                          'D', 
                          'E',) 
  
dropdown_menu4.grid(column = 7, row = 1) 

def delete():
    dropdown_menu.current(0)
    dropdown_menu1.current(0)
    dropdown_menu2.current(0)
    dropdown_menu3.current(0)
    dropdown_menu4.current(0)
    dropdown_menu5.current(0)
    dropdown_menu6.current(0)
    dropdown_menu7.current(0)
    dropdown_menu8.current(0)


# Clear button
btn1 = Button(window,text="Clear",command=delete,height=1,width=7).grid(column=0,row=2,padx=2,pady=2)


    
###### False Table Creation
ttk.Label(window, text = "HEADER1",font = ("Times New Roman", 10,'bold','underline')).grid(column = 1,row = 3) 
ttk.Label(window, text = "HEADER2",font = ("Times New Roman", 10,'bold','underline')).grid(column = 2,row = 3) 
ttk.Label(window, text = "HEADER3",font = ("Times New Roman", 10,'bold','underline')).grid(column = 3,row = 3) 
ttk.Label(window, text = "HEADER4",font = ("Times New Roman", 10,'bold','underline')).grid(column = 4,row = 3)
#  Labels 
ttk.Label(window, text = "Entry1.1",font = ("Times New Roman", 10)).grid(column = 1,row = 4) 
ttk.Label(window, text = "Entry1.2",font = ("Times New Roman", 10)).grid(column = 2,row = 4) 
ttk.Label(window, text = "Entry1.3",font = ("Times New Roman", 10)).grid(column = 3,row = 4) 

# Combobox
x = tk.StringVar() 
dropdown_menu5 = ttk.Combobox(window, width = 10, textvariable = x)
dropdown_menu5 = ttk.Combobox(window, width = 7, textvariable = x) 
dropdown_menu5['values'] = ('A',  
                          'B', 
                          'C', 
                          'D', 
                          'E',) 
  
dropdown_menu5.grid(column = 4, row = 4) 

#  Labels 
ttk.Label(window, text = "Entry2.1",font = ("Times New Roman", 10)).grid(column = 1,row = 5) 
ttk.Label(window, text = "Entry2.2",font = ("Times New Roman", 10)).grid(column = 2,row = 5) 
ttk.Label(window, text = "Entry2.3",font = ("Times New Roman", 10)).grid(column = 3,row = 5) 

# Combobox
y = tk.StringVar() 
dropdown_menu6 = ttk.Combobox(window, width = 10, textvariable = y)
dropdown_menu6 = ttk.Combobox(window, width = 7, textvariable = y) 
dropdown_menu6['values'] = ('A',  
                          'B', 
                          'C', 
                          'D', 
                          'E',) 
    
dropdown_menu6.grid(column = 4, row = 5) 

#  Labels 
ttk.Label(window, text = "Entry3.1",font = ("Times New Roman", 10)).grid(column = 1,row = 6) 
ttk.Label(window, text = "Entry3.2",font = ("Times New Roman", 10)).grid(column = 2,row = 6) 
ttk.Label(window, text = "Entry3.3",font = ("Times New Roman", 10)).grid(column = 3,row = 6) 

# Combobox
z = tk.StringVar() 
dropdown_menu7 = ttk.Combobox(window, width = 10, textvariable = z)
dropdown_menu7 = ttk.Combobox(window, width = 7, textvariable = z) 
dropdown_menu7['values'] = ('A',  
                          'B', 
                          'C', 
                          'D', 
                          'E',) 
  
dropdown_menu7.grid(column = 4, row = 6) 

#  Labels 
ttk.Label(window, text = "Entry4.1",font = ("Times New Roman", 10)).grid(column = 1,row = 7) 
ttk.Label(window, text = "Entry4.2",font = ("Times New Roman", 10)).grid(column = 2,row = 7) 
ttk.Label(window, text = "Entry4.3",font = ("Times New Roman", 10)).grid(column = 3,row = 7) 

# Combobox
l = tk.StringVar() 
dropdown_menu8 = ttk.Combobox(window, width = 10, textvariable = l)
dropdown_menu8 = ttk.Combobox(window, width = 7, textvariable = l)  
dropdown_menu8['values'] = ('A',  
                          'B', 
                          'C', 
                          'D', 
                          'E',) 
    
dropdown_menu8.grid(column = 4, row = 7) 

btn2 = Button(window,text="Save",height=1,width=7).grid(column=0,row=8,padx=2,pady=2)


    
dropdown_menu.current(0)
dropdown_menu1.current(0)
dropdown_menu2.current(0)
dropdown_menu3.current(0)
dropdown_menu4.current(4)
dropdown_menu5.current(0)
dropdown_menu6.current(1)
dropdown_menu7.current(2)
dropdown_menu8.current(3)
window.mainloop() 
