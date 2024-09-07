from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import Principal as Mn
class AjuUser():
    def __init__(self):
        self.ajustes=Tk()
        self.ajustes.title("SAMI - Software de Apoyo de MicroTienda")
        self.ajustes.config(bg="LightCyan2")
        self.ajustes.geometry("580x500")
        self.ajustes.resizable(0,0)

        
        
        #Titulo
        Titulo=Label(self.ajustes,text=' Ajustes ',bg='LightCyan2',font=('Rockwell Extra Bold', 48,'bold'),fg='black')
        Titulo.place(x=180,y=10)
        self.foto=PhotoImage(file="media/Ajustes.png")
        Label(self.ajustes, image=self.foto, bg="LightCyan2").place(x=15,y=15)

        #Datos de inicio
        Userr=Label(self.ajustes,text=' Usuario ',bg='LightCyan2',font=('Lucida',14,'bold'),fg='black')
        Userr.place(x=220,y=140)
        Userr2=Entry(self.ajustes,width=24,font=('Lucida',14),bg='white')
        Userr2.place(x=140,y=190)
        Userr2.focus()
        Passr=Label(self.ajustes,text='Contraseña ',bg='LightCyan2',font=('Lucida',14,'bold'),fg='black')
        Passr.place(x=200,y=240)
        Passrw=Entry(self.ajustes,width=24,show=('*'),font=('Lucida',14),bg='white')
        Passrw.place(x=140,y=280)

        lb1=Label(self.ajustes,text='Estado',bg='LightCyan2',font=('Lucida',14,'bold'),fg='black')
        lb1.place(x=230,y=330)

        #Radiobutton
        self.x=IntVar()
        rb1=Radiobutton(self.ajustes,text="Activo",variable=self.x,value=1,bg="LightCyan2",
                        font=("Arial",14,"bold"),fg="black")
        rb1.place(x=220,y=365)
        self.x.set(1)
        
        #Boton de registro
        
        def Close():
            self.ajustes.destroy()
            Mn.Mnu()

                

        def Guardar():
            
            if Userr2.get()!="":
                if Passrw.get()!="":
                    
                    f=open("data/Usuarios.txt",'a')
                    f.write('\n'+str(Userr2.get())+" "+str(Passrw.get())+" "+str(self.x.get()))
                    f.close()
                    tk.messagebox.showinfo(message="Se ha guardado con éxito",title="Usuario nuevo")

                    Userr2.delete(0,tk.END)
                    Passrw.delete(0,tk.END)
                    Userr2.focus()

                else:
                    messagebox.showinfo(message="Falta digitar la contraseña",title="Validación de datos")
                    
            else:
                messagebox.showinfo(message="Falta digitar el nombre de usuario",title="Validación de datos")
                
                    
                            
        Ingreso=Button(self.ajustes,width=12,text='   Guardar  ',font=('Eras Bold ITC',12),bg='LightBlue3',
                       command=Guardar)
        Ingreso.place(x=140,y=430)
        
        self.bt3=Button(self.ajustes,width=12,text="Cerrar",font=('Eras Bold ITC',12),
                        bg='LightBlue3',compound="top",command=Close)
        self.bt3.place(x=280,y=430)
 
        

        self.ajustes.mainloop()
if __name__=="__main__":
    AjuUser()




















    '''def Ajustes(vent,archivo,user,pas):

            a=250
            b=370
            if len(user.get())==0 or len(pas.get())==0:
                vl=Label(vent,text='Los Campos No Pueden Estar Vacios',bg='azure',fg='red')
                vl.place(x=a,y=b)
            else:
                plog={}
                with open(str(archivo)) as f:
                    for line in f:
                        (us,pasw)=line.split()
                        plog[str(us)] = pasw
                c=0
                for key in plog:
                    c+=1
                comp=0
                x=0
                for key in plog:
                    comp+=1
                    if str(key)==str(user.get()):
                        #x válida si el usuario ingresado existe
                        x=1
                    if str(key)==str(user.get()) and plog[key]==pas.get():
                        #comp me válida que el usuario y la contraseña sean correctos
                        comp=c+1
                        self.ajustes.destroy()
                        prin.Mnu()

                if x==0:
                    vl=Label(vent,text='           Usuario no encontrado             ',bg='azure',fg='red')
                    vl.place(x=a,y=b)
                else:
                    if c==comp:
                        vl=Label(vent,text='Usuario y/o contraseña incorrectos       ',bg='azure',fg='red')
                        vl.place(x=a,y=b)'''



