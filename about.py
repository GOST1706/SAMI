from tkinter import*
#from tkinter.font import tkFont
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox as MessageBox

class About:
    def __init__(self):
        self.about=Toplevel()
        self.about.title("SAMI - Software Apoyo Micromercado")
        #about.iconbitmap("icono.ico")
        self.about.geometry("380x660")
        self.about.config(bg="ivory") 
        self.about.resizable(1,1)
        self.imagen99=PhotoImage(file="media/SAMIN.png")

        def version(event):
            if self.combo.get()==tversion[0]:
                lb61= Label(self.about, text="Creado por:\n \nJuan Manuel Torres Melo\nMichel Dayanna Salazar Gómez\nEstudiantes Ingenieria Electrónica",bg="ivory",font=('Arial', 12),fg="black")
                lb61.place(x=50,y=320)
            else:
                lb63= Label(self.about, text="Actualizado por:\n \nAndrés Felipe Velasquez Gómez \nFabián Camilo Chacón Vargas \nEstudiantes Ingenieria Electrónica",bg="ivory",font=('Arial', 12),fg="black")
                lb63.place(x=50,y=320)
                
        
        tversion=["Sami version 1.0", "Sami version1.1"]
        self.combo = ttk.Combobox(self.about,values=tversion,state='readonly')
        self.combo.place(x=110, y=285)
        self.combo.current(0)
        self.combo.bind("<<ComboboxSelected>>", version)

        

        fondo=Label(self.about,image=self.imagen99,compound=tk.CENTER,bg="white").place(x=27,y=12)

        panel11=Frame(self.about)
        panel11.config(width="550",height="3",bg="ivory2")
        panel11.place(x=0,y=130)

        panel21=Frame(self.about)
        panel21.config(width="550",height="3",bg="ivory2")
        panel21.place(x=0,y=278)

        panel31=Frame(self.about)
        panel31.config(width="550",height="3",bg="ivory2")
        panel31.place(x=0,y=308)

        lb21= Label(self.about, text="Sofware de apoyo a micromercados ", bg="ivory",font=('Arial', 12),fg="black",anchor="w")
        lb21.place(x=50,y=100)
        lb31= Label(self.about, text="  Terminos y condiciones de uso ", bg="ivory",font=('Arial', 12,'bold'),fg="black",anchor="w")
        lb31.place(x=50,y=150)
        lb41= Label(self.about, text="1. Este programa fue creado con la \nintención de ayudar en \nel manejo de micromercados \n2. Es un software de\n uso libre", bg="ivory",font=('Arial', 12),fg="black",anchor="w")
        lb41.place(x=50,y=180)
        #lb51= Label(self.about, text="Sami version: 1.1", bg="ivory",font=('Arial', 12),fg="black",anchor="center")
        #lb51.place(x=110,y=280)
        lb61= Label(self.about, text="Creado por:\n \nJuan Manuel Torres Melo\nMichel Dayanna Salazar Gómez\nEstudiantes Ingenieria Electrónica",bg="ivory",font=('Arial', 12),fg="black")
        lb61.place(x=50,y=320)
       
        lb6= Label(self.about, text="Asesor técnico:\n \n Jaiver Josept Buitrago Graterón ",bg="ivory",font=('Arial', 12),fg="black",anchor="center")
        lb6.place(x=60,y=420)
        lb62= Label(self.about, text="Docente:\n \n Roney Armando Suarez Suarez",bg="ivory",font=('Arial', 12),fg="black",anchor="center")
        lb62.place(x=60,y=480)
        

        self.imagen98=PhotoImage(file="media/imagen14.png")
        fondo=Label(self.about,image=self.imagen98,compound=tk.CENTER,bg="white").place(x=70,y=550)
        
        
        
        def Crr():
            
            self.about.destroy()
            bt1=Button(self.about,text="Cerrar",font=('Arial',12),compound="top",command=Crr)
            bt1.place(x=150,y=750)
        
if __name__=="__main__":
    About()
    

        


