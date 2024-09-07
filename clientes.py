from tkinter import*
#from tkinter.font import tkFont
from tkinter import ttk #para capturar datos predeterminados
#from tkinter import messagebox as MessageBox
import tkinter as tk
import Principal as Mn



class Clt:
    def __init__(self):
        self.clientes=Tk()
        self.clientes.title("SAMI - Software Apoyo Micromercado")
        self.clientes.geometry("920x700")
        self.clientes.iconbitmap("media/cliente.ico")
        self.clientes.config(bg="lightCyan2")
        self.clientes.resizable(1,1)

 #FONDO
        bg = PhotoImage(file = "media/clientess.png") 
        canvas1 = Canvas( self.clientes, width = 920, height = 700)  
        canvas1.pack(fill = "both", expand = True) 
        canvas1.create_image( 0, 0, image = bg, anchor = "nw")
#Imagenes
        self.imagen1=PhotoImage(file="media/Nuevo.png")
        self.imagen2=PhotoImage(file="media/Guardar.png")
        self.imagen3=PhotoImage(file="media/Buscar.png")
        self.imagen4=PhotoImage(file="media/Listas.png")
        self.imagen5=PhotoImage(file="media/Cerrar.png")
#Titulos
        lb1= Label(self.clientes, text="➤ Código:", bg="lightCyan2",font=('Arial', 14,'bold'),
                   fg="midnight blue")
        lb1.place(x=520,y=270)
        lb2= Label(self.clientes, text="➤ Nombre:", bg="lightCyan2",font=('Arial', 14,'bold'),
                   fg="midnight blue")
        lb2.place(x=100,y=270)
        lb3= Label(self.clientes, text="➤ Dirección:", bg="lightCyan2",font=('Arial', 14,'bold'),
                   fg="midnight blue")
        lb3.place(x=100,y=340)
        lb4= Label(self.clientes, text="➤ Telefono:", bg="lightCyan2",font=('Arial', 14,'bold'),
                   fg="midnight blue")
        lb4.place(x=100,y=410)
        lb5= Label(self.clientes, text="➤ Saldo:", bg="lightCyan2",font=('Arial', 14,'bold'),
                   fg="midnight blue")
        lb5.place(x=100,y=480)
        self.cambios=0

#Combobox
        self.tb1=Entry(self.clientes,width=10, justify=LEFT,font=('Arial',16))
        self.tb1.place(x=650,y=270)
        self.acu=250
        with open("data/clientes.txt") as f:
            for linea in f:
                x=linea.split(";")
                                
                self.acu+=1
            
        self.tb1.insert(0,str(self.acu))
        self.tb1.config(state=tk.DISABLED)
        self.tb2=Entry(self.clientes,width=17, justify=LEFT,font=('Arial',16))
        self.tb2.place(x=260,y=270)
        self.tb3=Entry(self.clientes,width=17, justify=LEFT,font=('Arial',16))
        self.tb3.place(x=260,y=340)
        self.tb4=Entry(self.clientes,width=10, justify=LEFT,font=('Arial',16))
        self.tb4.place(x=260,y=410)
        self.tb5=Entry(self.clientes,width=10, justify=LEFT,font=('Arial',16))
        self.tb5.place(x=260,y=480)


        def seleccion(event):
            self.tb1.config(state=tk.NORMAL)
            self.tb1.delete(0,tk.END)
            self.tb2.delete(0,tk.END)
            self.tb3.delete(0,tk.END)
            self.tb4.delete(0,tk.END)
            self.tb5.delete(0,tk.END)
            
            cont=0
            x=self.combo.get()
            for i in self.nombre:
                if x==i:
                    pos=cont
                    break
                cont+=1
            self.tb1.insert(0,self.codigo[pos])
            self.tb1.config(state=tk.DISABLED)
            self.tb2.insert(0,self.nombre[pos])
            self.tb3.insert(0,self.dirección[pos])
            self.tb4.insert(0,self.telefono[pos])
            self.tb5.insert(0,self.saldo[pos].replace("\n",""))
            self.acu-=1
            self.cambio=1
        
        def Close():
            self.clientes.destroy()
            Mn.Mnu()
        def Guardar():
            ps=0
            codigo=[]
            nombre=[""]
            direccion=[""]
            telefono=[""]
            saldo=[""]
            self.y=0
            with open("data/clientes.txt") as f:
                for linea in f:
                    x=linea.split(";")
                    codigo.append(x[0])
                    nombre.append(x[1])
                    direccion.append(x[2])
                    telefono.append(x[3])
                    saldo.append(x[4])
                  
                    if self.tb1.get()==codigo[ps]:
                        self.y=1
                        posi=ps
                    ps+=1
                    
           
            if self.y==1:
                Mn.Mnu.Alterno(self,"data/clientes.txt",posi)
                return
            
            if self.cambios!=1:
                self.acu+=1
                if self.tb1.get()!="":
                    if self.tb2.get()!="":
                        if self.tb3.get()!="":
                            if len(self.tb4.get())!=0:
                                if self.tb5.get()=="":
                                    self.tb5.insert(0,0)
                                archivo="data/Clientes.txt"
                                f=open(archivo,"a")
                                f.write(str(self.tb1.get())+";"+str(self.tb2.get())+";"+str(self.tb3.get())+
                                        ";"+str(self.tb4.get())+";"+str(self.tb5.get())+"\n")
                                f.close()
                                self.Nuevo()
                                tk.messagebox.showinfo(message="Se ha guardado con éxito",title="Clientes")
                            else:
                                tk.messagebox.showinfo(message="Falta digitar el número de telefono",title="Validación de datos")
                        else:
                            tk.messagebox.showinfo(message="Falta digitar la dirección",title="Validación de datos")
                    else:
                        tk.messagebox.showinfo(message="Falta digitar el nombre",title="Validación de datos")
                else:
                    tk.messagebox.showinfo(message="Falta digitar el código",title="Validación de datos")
            else:
                archivo="data/Clientes.txt"
                f=open(archivo,"a")
                f.write(str(self.tb1.get())+";"+str(self.tb2.get())+";"+str(self.tb3.get())+
                             ";"+str(self.tb4.get())+";"+str(self.tb5.get()))
                
                        
        def Buscar():
            
            self.bb=Toplevel()
            self.bb.title("SAMI - Software de Apoyo de MicroTienda")
            self.bb.config(bg="azure")
            self.bb.geometry("520x200")
            self.bb.resizable(0,0)
            self.codigo=[""]
            self.nombre=[""]
            self.dirección=[""]
            self.telefono=[""]
            self.saldo=[""]
            with open("data/Clientes.txt") as f:
                for linea in f:
                    x=linea.split(";")
                    self.codigo.append(x[0])
                    self.nombre.append(x[1])
                    self.dirección.append(x[2])
                    self.telefono.append(x[3])
                    self.saldo.append(x[4])
    
      
            Label(self.bb, text=" ☞ Buscar Clientes", bg="azure",font=('Rockwell Extra Bold', 30,'bold'),
                  fg="purple").place(x=40,y=10)
            
            self.combo = ttk.Combobox(self.bb,state="readonly",font=("Arial",14),
                                values=self.nombre,width=24)
            self.combo.place(x=120,y=90)
            self.combo.bind("<<ComboboxSelected>>", seleccion)
            
            def Aceptar():
                self.bb.destroy()

            def Cancelar():
                self.bb.destroy()
            self.bt00=Button(self.bb,text="Aceptar",font=('Eras Bold ITC',12),
                            bg="violet",compound="top",width="12",command=Aceptar)
            self.bt00.place(x=120,y=150)
            self.bt01=Button(self.bb,text="Cancelar",font=('Eras Bold ITC',12),
                            bg="violet",compound="top",width="12",command=Cancelar)
            self.bt01.place(x=275,y=150)
#Botones
        self.bt1=Button(self.clientes,text="Nuevo",font=('Eras Bold ITC',12),
                        bg="gray65",image=self.imagen1,compound="top", command=self.Nuevo)
        self.bt1.place(x=290,y=535)
        self.bt2=Button(self.clientes,text="Guardar",font=('Eras Bold ITC',12),
                        bg="gray65",image=self.imagen2,compound="top",command=Guardar)
        self.bt2.place(x=395,y=535)
        self.bt3=Button(self.clientes,text="Buscar",font=('Eras Bold ITC',12),
                        bg="gray65",image=self.imagen3,compound="top",command=Buscar)
        self.bt3.place(x=80,y=535)
        self.bt4=Button(self.clientes,text="Listado",font=('Eras Bold ITC',12),
                        bg="gray65",image=self.imagen4,compound="top",command=lambda:Mn.Mnu.Tabla(self,"clientes"))
        self.bt4.place(x=185,y=535)   
        self.bt5=Button(self.clientes,text="Cerrar",font=('Eras Bold ITC',12),
                        bg="gray65",image=self.imagen5,compound="top",command=Close)
        self.bt5.place(x=780,y=535)


#Menus
        self.img1 = tk.PhotoImage(file="media/img2.png")
        self.img2 = tk.PhotoImage(file="media/img1.png")
        self.img3 = tk.PhotoImage(file="media/img3.png")
        self.img4 = tk.PhotoImage(file="media/img4.png")
        self.img5 = tk.PhotoImage(file="media/img5.png")


        
        archivo=ttk.Style()
        archivo.configure("TMenubutton",font="Arial 14")
        menu=ttk.Menubutton(self.clientes,text="Archivo")
        ItemMenu=Menu(menu,font="Arial 12",tearoff=0)
        ItemMenu.add_command(label="Nuevo",image=self.img1,compound="left",accelerator="F8",command=self.Nuevo)
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Guardar",image=self.img2,compound="left",accelerator="F8",command=Guardar)
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Buscar",image=self.img3,compound="left",accelerator="F8",command=Buscar)
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Listados",image=self.img4,compound="left",accelerator="F8",command=lambda:Mn.Mnu.Tabla(self,"clientes"))
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Cerrar",image=self.img5,compound="left",command=Close)

        menu.configure(menu=ItemMenu)
        menu.place(x=0,y=0)
        
        self.clientes.mainloop()
    def Nuevo(self):
        self.tb1.config(state=tk.NORMAL)
        self.tb1.delete(0, tk.END)
        self.tb1.insert(0,str(self.acu))
        self.tb1.config(state=tk.DISABLED)
        self.tb2.delete(0, tk.END)
        self.tb3.delete(0, tk.END)
        self.tb4.delete(0, tk.END)
        self.tb5.delete(0, tk.END)
        self.tb1.focus()
        self.cambios=0

        
if __name__=="__main__":
    Clt()
