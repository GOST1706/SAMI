from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import Principal as Mn
class Aju():
    def __init__(self):
        self.ajustes=Tk()
        self.ajustes.title("SAMI - Software de Apoyo de MicroTienda")
        self.ajustes.config(bg="LightCyan2")
        self.ajustes.geometry("580x500")
        self.ajustes.resizable(0,0)

        
        
        #Titulo
        Titulo=Label(self.ajustes,text=' Ajustes ',bg='LightCyan2',font=('Rockwell Extra Bold', 48,'bold'),fg='black')
        Titulo.place(x=140,y=10)
        self.foto=PhotoImage(file="media/Ajustes.png")
        Label(self.ajustes, image=self.foto, bg="LightCyan2").place(x=15,y=15)
        def Close():
            self.ajustes.destroy()
        #Datos de inicio

        

        lb1=Label(self.ajustes,text='Estado',bg='LightCyan2',font=('Lucida',14,'bold'),fg='black')
        lb1.place(x=220,y=330)

        #Radiobutton
        
        self.x=IntVar()
        rb1=Radiobutton(self.ajustes,text="Activo",variable=self.x,value=1,bg="LightCyan2",
                        font=("Arial",14,"bold"),fg="black")
        rb1.place(x=140,y=365)
        rb2=Radiobutton(self.ajustes,text="Inactivo",variable=self.x,value=2,bg="LightCyan2",
                        font=("Arial",14,"bold"),fg="black")
        rb2.place(x=300,y=365)

        self.user=[""]
        self.contra=[""]
        self.estado=[""]

        with open("data/Usuarios.txt") as f:
            for linea in f:
                x=linea.split(" ")
                self.user.append(x[0])
                self.contra.append(x[1])
                self.estado.append(x[2].replace('\n',''))

        def seleccion(event):
            self.Passrw.delete(0,tk.END)
            user=[""]
            contra=[""]
            estado=[""]
            with open("data/Usuarios.txt") as f:
                for linea in f:
                    x=linea.split(" ")
                    user.append(x[0])
                    contra.append(x[1])
                    estado.append(x[2].replace('\n',''))

            cont=0
            x=self.combo.get()
            for i in user:
                if x==i:
                    pos=cont
                    break
                cont+=1

            self.Passrw.insert(0,contra[pos])
            if int(estado[pos])==2:
                self.x.set(2)
            else:
                self.x.set(1)

                    

                
        #Boton de registro
        
        def Close():
            self.ajustes.destroy()
            Mn.Mnu()

        Tb=Label(self.ajustes,text=' Usuario ',bg='LightCyan2',font=('Lucida',14,'bold'),fg='black')
        Tb.place(x=220,y=140)

        Passr=Label(self.ajustes,text='Contraseña ',bg='LightCyan2',font=('Lucida',14,'bold'),fg='black')
        Passr.place(x=200,y=240)
        self.Passrw=Entry(self.ajustes,width=24,show=('*'),font=('Lucida',14),bg='white')
        self.Passrw.place(x=140,y=280)

        self.combo = ttk.Combobox(values=self.user,font=("Arial",12,"bold"),width=27)
        self.combo.place(x=140,y=190)
        self.combo.bind("<<ComboboxSelected>>", seleccion)

 

        def Guardar():
            plog={}
            if self.Passrw.get()!="":
                archivo="data/Usuarios.txt"
                with open(archivo) as f:
                    for line in f:
                        (us,pasw,estado)=line.split()
                        plog[str(us)] = [pasw,estado]
                for key in plog:
                    if self.combo.get()==key:
                        x=[self.Passrw.get(),self.x.get()]
                        plog.update({key:x})
                        break
                print(plog)
                f=open(archivo,'w')
                for key in plog:
                    f.write(str(key)+' '+str(plog[key][0])+' '+str(plog[key][1])+'\n')
                f.close()
                self.Passrw.delete(0,tk.END)
                self.combo.current(0)
                self.x.set(0)
                tk.messagebox.showinfo(message="Se ha actualizado con éxito",title="Validación de datos")

                        
        #lambda se usa para botones que tienen funciones que reciben parametros               
        Ingreso=Button(self.ajustes,width=12,text='   Guardar  ',font=('Eras Bold ITC',12),bg='LightBlue3',
                       compound="top",command=Guardar)
        Ingreso.place(x=140,y=430)
        
        self.bt3=Button(self.ajustes,width=12,text="Cerrar",font=('Eras Bold ITC',12),
                        bg='LightBlue3',compound="top",command=Close)
        self.bt3.place(x=280,y=430)
 
        

        self.ajustes.mainloop()
if __name__=="__main__":
    Aju()


