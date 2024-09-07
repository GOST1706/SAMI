from tkinter import *
from tkinter import ttk
from tkinter import messagebox

wind=Toplevel()
wind.title("SAMI - Software Apoyo Micromercado")
wind.config(bg="ivory") 
wind.resizable(1,1)

def lista(event):
   return
                
combo = ttk.Combobox(wind,width=100,state='readonly')
combo.grid(row=0,column=0)
combo.bind("<<ComboboxSelected>>",lista)
combo1 = ttk.Combobox(wind,width=100,state='readonly')
combo1.grid(row=1,column=0)
combo1.bind("<<ComboboxSelected>>",lista)
combo2 = ttk.Combobox(wind,width=100,state='readonly')
combo2.grid(row=2,column=0)
combo2.bind("<<ComboboxSelected>>",lista)

wind.mainloop()