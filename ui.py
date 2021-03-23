from tkinter import *
import tkinter as tk 
from tkinter import ttk
import pandas as pd
import constants
import service

def get_width(values):
    return len(max(values, key = len)) + 2

def pick_expiry_date(e):
    constants.dropdown_expiry_date = []
    dropdown_menu2.config(value=[" "], width=10)
    dropdown_menu2.current(0)
    constants.dropdown_option_type = []
    dropdown_menu3.config(value=[" "], width=10)
    dropdown_menu3.current(0)
    constants.dropdown_strike_price = []
    dropdown_menu4.config(value=[" "], width=10)
    dropdown_menu4.current(0)
    for script_name in constants.dropdown_scipt_name:
        if dropdown_menu1.get() == script_name:
            constants.dropdown_expiry_date = service.expiry_date_service(script_name)
            dropdown_menu2.config(value=constants.dropdown_expiry_date, width=get_width(constants.dropdown_expiry_date))
            dropdown_menu2.current(0)

def pick_option_type(e):
    constants.dropdown_option_type = []
    dropdown_menu3.config(value=[" "], width=10)
    dropdown_menu3.current(0)
    constants.dropdown_strike_price = []
    dropdown_menu4.config(value=[" "], width=10)
    dropdown_menu4.current(0)
    for expiry_date in constants.dropdown_expiry_date:
        if dropdown_menu2.get() == expiry_date:
            constants.dropdown_option_type = service.option_type_service(expiry_date)
            dropdown_menu3.config(value=constants.dropdown_option_type, width=get_width(constants.dropdown_option_type))
            dropdown_menu3.current(0)

def pick_strike_price(e):
    constants.dropdown_strike_price = []
    dropdown_menu4.config(value=[" "], width=10)
    dropdown_menu4.current(0)
    for option_type in constants.dropdown_option_type:
        if dropdown_menu3.get() == option_type:
            constants.dropdown_strike_price = service.strike_price_service(option_type)
            dropdown_menu4.config(value=constants.dropdown_strike_price, width=get_width(constants.dropdown_strike_price))
            dropdown_menu4.current(0)

def delete():
    dropdown_menu.current(0)
    dropdown_menu1.current(0)
    dropdown_menu2.config(value=[" "], width=10)
    dropdown_menu2.current(0)
    dropdown_menu3.config(value=[" "], width=10)
    dropdown_menu3.current(0)
    dropdown_menu4.config(value=[" "], width=10)
    dropdown_menu4.current(0)

# Tkinter window configs
window = tk.Tk() 
window.title(constants.title) 
window.geometry(str(constants.window_width) + 'x' + str(constants.window_height))
# Leg Dropdown
dropdown_menu = ttk.Combobox(window, state='readonly', width=get_width(constants.dropdown_leg), value=constants.dropdown_leg)
dropdown_menu.grid(column = 1, row = 0)
dropdown_menu.current(0)
# Script Name Label
ttk.Label(window, text = constants.script_name_label, font = ("Times New Roman", 14)).grid(column = 0, row = 1)
# Script Name Dropdown
dropdown_menu1 = ttk.Combobox(window, state='readonly', width=get_width(constants.dropdown_scipt_name), value=constants.dropdown_scipt_name)
dropdown_menu1.bind("<<ComboboxSelected>>", pick_expiry_date)
dropdown_menu1.grid(column = 1, row = 1)
dropdown_menu1.current(0)
# Strike Price Label
ttk.Label(window, text = constants.expiry_date_label, font = ("Times New Roman", 14)).grid(column = 2, row = 1)
# Strike Price Dropdown
dropdown_menu2 = ttk.Combobox(window, state = 'readonly', width=10, value=[" "])
dropdown_menu2.bind("<<ComboboxSelected>>", pick_option_type)
dropdown_menu2.grid(column = 3, row = 1) 
# Option Type Label
ttk.Label(window, text = constants.option_type_label, font = ("Times New Roman", 14)).grid(column = 4, row = 1)
# Option Type Dropdown
dropdown_menu3 = ttk.Combobox(window, state = 'readonly', width=10, value=[" "])
dropdown_menu3.bind("<<ComboboxSelected>>", pick_strike_price)
dropdown_menu3.grid(column = 5, row = 1) 
# Strike Price Label
ttk.Label(window, text = constants.strike_price_label, font = ("Times New Roman", 14)).grid(column = 6, row = 1)
# Strike Price Dropdown
dropdown_menu4 = ttk.Combobox(window, state = 'readonly', width=10, value=[" "])
dropdown_menu4.grid(column = 7, row = 1) 
# Clear button
Button(window,text="Clear",command=delete,height=1,width=7).grid(column=0,row=2,padx=2,pady=2)


    
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

window.mainloop() 
