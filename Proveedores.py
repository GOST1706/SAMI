from tkinter import *
from tkinter import ttk
import tkinter as tk
import Principal as Mn

class Prv:
    
    def __init__(self):
        
        self.Proveedores=Tk()
        self.Proveedores.title("SAMI - Software de Apoyo de MicroMercado")
        self.Proveedores.config(bg="light cyan")
        self.Proveedores.geometry("920x700")
        self.Proveedores.resizable(0,0)

        #imagenes
        self.im1=PhotoImage(file="media/Nuevo.png")
        self.im2=PhotoImage(file="media/Guardar.png")
        self.im3=PhotoImage(file="media/Buscar.png")
        self.im4=PhotoImage(file="media/Listas.png")
        self.im5=PhotoImage(file="media/Cerrar.png")
        self.im6=PhotoImage(file="media/Prveedores.png")

       
           #FONDO
        bg = PhotoImage(file = "media/proveedor.png") 
        canvas1 = Canvas( self.Proveedores, width = 920, height = 700)  
        canvas1.pack(fill = "both", expand = True) 
        canvas1.create_image( 0, 30, image = bg, anchor = "nw")      

   

        

        #Titulos
        tl1=Label(self.Proveedores,text="➤ Nit:",bg="light cyan",font=("Arial",14,"bold"),fg="black")
        tl1.place(x=100,y=297)
        tl2=Label(self.Proveedores,text="➤ Nombre:",bg="light cyan",font=("Arial",14,"bold"),fg="black")
        tl2.place(x=100,y=397)
        tl3=Label(self.Proveedores,text="➤ Dirección:",bg="light cyan",font=("Arial",14,"bold"),fg="black")
        tl3.place(x=470,y=297)
        tl4=Label(self.Proveedores,text="➤ Telefono:",bg="light cyan",font=("Arial",14,"bold"),fg="black")
        tl4.place(x=470,y=397)
        tl5=Label(self.Proveedores,text="➤ Cartera:",bg="light cyan",font=("Arial",14,"bold"),fg="black")
        tl5.place(x=100,y=497)



        #Completar
        self.tb1=Entry(self.Proveedores,width=25,justify=LEFT,font=("Arial",12),bg="gray93")
        self.tb1.place(x=220,y=300)
        self.tb2=Entry(self.Proveedores,width=25,justify=LEFT,font=("Arial",12),bg="gray93")
        self.tb2.place(x=220,y=400)
        self.tb3=Entry(self.Proveedores,width=25,justify=LEFT,font=("Arial",12),bg="gray93")
        self.tb3.place(x=600,y=300)
        self.tb4=Entry(self.Proveedores,width=25,justify=LEFT,font=("Arial",12),bg="gray93")
        self.tb4.place(x=600,y=400)
        self.tb5=Entry(self.Proveedores,width=25,justify=LEFT,font=("Arial",12),bg="gray93")
        self.tb5.place(x=220,y=500)
        self.y=0

        def seleccion(event):
            self.tb1.delete(0,tk.END)
            self.tb2.delete(0,tk.END)
            self.tb3.delete(0,tk.END)
            self.tb4.delete(0,tk.END)
            self.tb5.delete(0,tk.END)
            cont=0
            x=self.combo.get()
            for i in self.privedores:
                if x==i:
                    pos=cont
                    break
                cont+=1
            self.tb1.insert(0,self.nit[pos])
            self.tb2.insert(0,self.privedores[pos])
            self.tb3.insert(0,self.direccion[pos])
            self.tb4.insert(0,self.telefono[pos])
            self.tb5.insert(0,self.cartera[pos])
            

        def Close():
            self.Proveedores.destroy()
            Mn.Mnu()
            
        def Nuevo():
            self.tb1.delete(0, tk.END)
            self.tb2.delete(0, tk.END)
            self.tb3.delete(0, tk.END)
            self.tb4.delete(0, tk.END)
            self.tb5.delete(0, tk.END)
        def Guardar():
            ps=0
            NIT=[]
            with open("data/provedores.txt") as f:
                for linea in f:
                    x=linea.split(";")
                    NIT.append(x[0])
                    if self.tb1.get()==NIT[ps]:
                        self.y=1
                        posi=ps
                    ps+=1
                    
           
            if self.y==1:
                Mn.Mnu.Alterno(self,"data/provedores.txt",posi)
                return
            
            if self.tb1.get()!="":
                if self.tb2.get()!="":
                    if self.tb3.get()!="":
                        if self.tb4.get()!="":
                            archivo="data/provedores.txt"
                            f=open(archivo,"a")
                            f.write(str(self.tb1.get())+";"+str(self.tb2.get())+";"+str(self.tb3.get())+
                                    ";"+str(self.tb4.get())+";"+str(self.tb5.get())+"\n")
                            f.close()
                            tk.messagebox.showinfo(message="Se ha guardado con éxito",title='Proveedores')
                            Nuevo()
                        else:
                            tk.messagebox.showinfo(message="Falta digitar el Telefono",title='Validación de datos')
                    else:
                       tk.messagebox.showinfo(message="Falta digitar el Dirección",title='Validación de datos')
                else:
                   tk.messagebox.showinfo(message="Falta digitar el Nombre",title='Validación de datos')
            else:
                tk.messagebox.showinfo(message="Falta digitar el NIT",title='Validación de datos')
        def Buscar():
            
            self.bus=Toplevel()
            self.bus.title("SAMI - Software de Apoyo de MicroTienda")
            self.bus.config(bg="white")
            self.bus.geometry("520x200")
            self.bus.resizable(0,0)
            self.privedores=[""]
            self.nit=[""]
            self.telefono=[""]
            self.direccion=[""]
            self.cartera=[""]
        
            with open("data/provedores.txt") as f:
                for linea in f:
                    x=linea.split(";")
                    self.nit.append(x[0])
                    self.privedores.append(x[1])
                    self.telefono.append(x[3])
                    self.direccion.append(x[2])
                    self.cartera.append(x[4])
                    
      
            Label(self.bus, text="☞Buscar Proveedores", bg="white",font=('Rockwell Extra Bold', 29,'bold'),
                  fg="chartreuse4").place(x=0,y=15)
            
            self.combo = ttk.Combobox(self.bus,state="readonly",font=("Arial",14),
                                 values=self.privedores,width=24)
            self.combo.place(x=100,y=100)
            self.combo.bind("<<ComboboxSelected>>", seleccion)
            
            def Aceptar():
                self.bus.destroy()

            def Cancelar():
                self.bus.destroy()
            self.bt1=Button(self.bus,text="Aceptar",font=('Eras Bold ITC',12),
                            bg="darkolivegreen2",compound="top",width="12",command=Aceptar)
            self.bt1.place(x=100,y=150)
            self.bt2=Button(self.bus,text="Cancelar",font=('Eras Bold ITC',12),
                            bg="darkolivegreen2",compound="top",width="12",command=Cancelar)
            self.bt2.place(x=255,y=150)     
        #botones
            
        x=self.tb1
        self.bt1=Button(self.Proveedores,text="Nuevo",font=('Eras Bold ITC',12),
                        bg="gray65",image=self.im1,compound="top", command=Nuevo)
        self.bt1.place(x=290,y=565)
        self.bt2=Button(self.Proveedores,text="Guardar",font=('Eras Bold ITC',12),
                        bg="gray65",image=self.im2,compound="top",command=Guardar)
        self.bt2.place(x=395,y=565)
        self.bt3=Button(self.Proveedores,text="Buscar",font=('Eras Bold ITC',12),
                        bg="gray65",image=self.im3,compound="top",command=Buscar)
        self.bt3.place(x=80,y=565)
        self.bt4=Button(self.Proveedores,text="Listado",font=('Eras Bold ITC',12),
                        bg="gray65",image=self.im4,compound="top",command=lambda:Mn.Mnu.Tabla(self,"provedores"))
        self.bt4.place(x=185,y=565)   
        self.bt5=Button(self.Proveedores,text="Cerrar",font=('Eras Bold ITC',12),
                        bg="gray65",image=self.im5,compound="top",command=Close)
        self.bt5.place(x=780,y=565)
        #menus

        self.img1 = tk.PhotoImage(file="media/img2.png")
        self.img2 = tk.PhotoImage(file="media/img1.png")
        self.img3 = tk.PhotoImage(file="media/img3.png")
        self.img4 = tk.PhotoImage(file="media/img4.png")
        self.img5 = tk.PhotoImage(file="media/img5.png")

        archivo=ttk.Style()
        archivo.configure("TMenubutton",font="Arial 14")
        menu=ttk.Menubutton(self.Proveedores,text="Archivo")
        ItemMenu=tk.Menu(menu,font="Arial 12",tearoff=0)
        ItemMenu.add_command(label="Nuevo",compound="left",accelerator="F8",command=self.Nuevo,image=self.img1)
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Guardar",compound="left",accelerator="F8",image=self.img2,command=Guardar)
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Buscar",compound="left",accelerator="F8",image=self.img3,command=Buscar)
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Listados",compound="left",accelerator="F8",image=self.img4,command=lambda:Mn.Mnu.Tabla(self,"provedores"))
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Cerrar ",command=Close,image=self.img5,compound="left")

        menu.configure(menu=ItemMenu)
        menu.place(x=0,y=0)
        
        self.Proveedores.mainloop()

    def Nuevo(self):
        self.tb1.delete(0, tk.END)
        self.tb2.delete(0, tk.END)
        self.tb3.delete(0, tk.END)
        self.tb4.delete(0, tk.END)
        self.tb5.delete(0, tk.END)
        self.tb1.focus()

if __name__=="__main__":
    Prv()
    


