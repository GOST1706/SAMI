from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Principal as Mn
import tkinter as tk
import os
import Entradas as et
import Facturas as fatt

class Prd:
    def __init__(self):
        self.unidades=[""]
        self.archivo="data/Tunid.txt"
        self.f=open(self.archivo,"r")
        for linea in self.f:
            self.m=linea.split("\n")
            self.unidades.append(self.m[0])
        self.f.close()
        
        self.productos=Tk()
        self.productos.title("SAMI - Software de Apoyo de MicroMercado")
        self.productos.config(bg="white")
        self.productos.geometry("920x720")
        self.productos.resizable(0,0)
                #FONDO
        bg = PhotoImage(file = "media/productoss.png") 
        canvas1 = Canvas( self.productos, width = 920, height = 700)  
        canvas1.pack(fill = "both", expand = True) 
        canvas1.create_image( 0, 30, image = bg, anchor = "nw")

      

        #imagenes
        self.im1=PhotoImage(file="media/Nuevo.png")
        self.im2=PhotoImage(file="media/Guardar.png")
        self.im3=PhotoImage(file="media/Buscar.png")
        self.im4=PhotoImage(file="media/Listas.png")
        self.im5=PhotoImage(file="media/Cerrar.png")
        self.im6=PhotoImage(file="media/Productos.png")

    


        #Titulos
        tl1=Label(self.productos,text="➤ Codigo:",bg="white",font=("Arial",14,"bold"),fg="black")
        tl1.place(x=70,y=397)
        tl2=Label(self.productos,text="➤ Nombre:",bg="white",font=("Arial",14,"bold"),fg="black")
        tl2.place(x=70,y=327)
        tl3=Label(self.productos,text="➤ Unidad:",bg="white",font=("Arial",14,"bold"),fg="black")
        tl3.place(x=535,y=327)
        tl4=Label(self.productos,text="➤ Costo:",bg="white",font=("Arial",14,"bold"),fg="black")
        tl4.place(x=70,y=467)
        tl5=Label(self.productos,text="➤ Saldo:",bg="white",font=("Arial",14,"bold"),fg="black")
        tl5.place(x=535,y=397)
        tl6=Label(self.productos,text="➤ Venta:",bg="white",font=("Arial",14,"bold"),fg="black")
        tl6.place(x=535,y=467)
        #combobox
        #Completar
        self.acu=1
        self.tb1=Entry(self.productos,width=35,justify=LEFT,font=("Arial",12),bg="gray93")
        self.tb1.place(x=200,y=400)
        self.tb2=Entry(self.productos,width=35,justify=LEFT,font=("Arial",12),bg="gray93")
        self.tb2.place(x=200,y=330)
        with open("data/hproduct.txt") as f:
            for linea in f:
                x=linea.split(";")
                self.acu+=1
            
        self.tb1.insert(0,str(self.acu))
        self.tb1.config(state=tk.DISABLED)
        self.combo1 = ttk.Combobox(state="readonly",font=("Arial",12),
                             values=self.unidades)
        self.combo1.place(x=640,y=330)
                             
        self.tb4=Entry(self.productos,width=35,justify=LEFT,font=("Arial",12),bg="gray93")
        self.tb4.place(x=200,y=470)
        self.tb5=Entry(self.productos,width=22,justify=LEFT,font=("Arial",12),bg="gray93")
        self.tb5.place(x=640,y=400)
        self.tb6=Entry(self.productos,width=22,justify=LEFT,font=("Arial",12),bg="gray93")
        self.tb6.place(x=640,y=470)
        self.pos=0
        self.y=0
          
        self.buscar=(str(self.tb1.get())+";"+str(self.tb2.get())+";"+str(self.combo1.get())+
                        ";"+str(self.tb4.get())+";"+""+";"+str(self.tb6.get()))
        self.text=(str(self.tb1.get())+";"+str(self.tb2.get())+";"+str(self.combo1.get())+
                        ";"+str(self.tb4.get())+";"+""+";"+str(self.tb6.get()))
        
        def seleccion(event):
            
            self.tb1.config(state=tk.NORMAL)
            self.tb1.delete(0,tk.END)
            self.tb2.delete(0,tk.END)
            self.tb4.delete(0,tk.END)
            self.tb5.delete(0,tk.END)
            self.tb6.delete(0,tk.END)
            cont=0
            x=self.combo.get()
            for i in self.priductos:
                if x==i:
                    self.pos=cont
                cont+=1
            self.tb1.insert(0,self.codigo[self.pos])
            self.tb1.config(state=tk.DISABLED)
            self.tb2.insert(0,self.priductos[self.pos])
            self.tb4.insert(0,self.costos[self.pos])
            self.tb5.insert(0,self.saldo[self.pos])
            self.tb6.insert(0,self.venta[self.pos])
            self.combo1.set(self.unidad[self.pos])
            
            self.buscar=(str(self.tb1.get())+";"+str(self.tb2.get())+";"+str(self.combo1.get())+
                        ";"+str(self.tb4.get())+";"+str(x)+";"+str(self.tb6.get()))
            
            
            
        def Close():
            self.productos.destroy()
            Mn.Mnu()
        
        
        def Guardar():
            ps=0
            self.priductos=[""]
            self.codigo=[]
            self.unidad=[""]
            self.costos=[""]
            self.saldo=[""]
            self.venta=[""]
            with open("data/hproduct.txt") as f:
                for linea in f:
                    x=linea.split(";")
                    self.codigo.append(x[0])
                    self.priductos.append(x[1])
                    self.unidad.append(x[2])
                    self.costos.append(x[3])
                    self.saldo.append(x[4])
                    self.venta.append(x[5])
                    if self.tb1.get()==self.codigo[ps]:
                        self.y=1
                        posi=ps
                    ps+=1
                    
           
            if self.y==1:
                Mn.Mnu.Alterno(self,"data/hproduct.txt",posi)
                return
                     
            if len(self.tb1.get())!=0:
                if len(self.tb2.get())!=0:
                    for i in range(ps):
                        if self.tb1.get()==self.codigo[i]:
                            self.tb1.config(state=tk.NORMAL)
                            self.tb1.insert(0,self.codigo[i])
                            self.tb1.config(state=tk.DISABLED)
                            self.tb2.insert(0,self.priductos[i])
                            self.tb4.insert(0,self.costos[i])
                            self.tb5.insert(0,self.saldo[i])
                            self.tb6.insert(0,self.venta[i])
                            self.combo1.set(self.unidad[i])
                        if self.tb2.get()==self.priductos[i]:                        
                            messagebox.showinfo(message="El producto ya fue registrado. \nConfigura el producto ó \nAgrega un nuevo Producto.",title="Productos")
                            self.Nuevo()
                        
                    if len(self.combo1.get())!=0:
                        if len(self.tb4.get())!=0:
                            if len(self.tb5.get())!=0:
                                x=self.tb5.get()
                            else:
                                x=0                            
                            if len(self.tb6.get())!=0:
                                archivo="data/hproduct.txt"
                                f=open(archivo,"a")
                                f.write(str(self.tb1.get())+";"+str(self.tb2.get())+";"+str(self.combo1.get())+
                                            ";"+str(self.tb4.get())+";"+str(x)+";"+str(self.tb6.get())+'\n')
                                f.close()
                                self.Nuevo()
                                messagebox.showinfo(message="Se ha guardado con éxito",title="Productos")
                                
                            else:
                                messagebox.showinfo(message="Falta digitar venta",title="Validación de datos")
                        else:
                            messagebox.showinfo(message="Falta digitar costo",title="Validación de datos")
                    else:
                        messagebox.showinfo(message="Falta seleccionar unidad",title="Validación de datos")
                else :
                    messagebox.showinfo(message="Falta digitar nombre",title="Validación de datos")     
            else:
                messagebox.showinfo(message="Falta digitar codigo",title="Validación de datos")
        
        def Buscar():
            
            self.bus=Toplevel()
            self.bus.title("SAMI - Software de Apoyo de MicroTienda")
            self.bus.config(bg="white")
            self.bus.geometry("520x200")
            self.bus.resizable(0,0)
            self.priductos=[""]
            self.codigo=[""]
            self.unidad=[""]
            self.costos=[""]
            self.saldo=[""]
            self.venta=[""]
            with open("data/hproduct.txt") as f:
                for linea in f:
                    x=linea.split(";")
                    self.codigo.append(x[0])
                    self.priductos.append(x[1])
                    self.unidad.append(x[2])
                    self.costos.append(x[3])
                    self.saldo.append(x[4])
                    self.venta.append(x[5])
            f.close()
            
              
            Label(self.bus, text="Buscar Productos", bg="white",font=('Rockwell Extra Bold', 30,'bold'),
                  fg="firebrick2").place(x=40,y=10)
            
            self.combo = ttk.Combobox(self.bus,state="readonly",font=("Arial",14),
                                 values=self.priductos,width=24)
            self.combo.place(x=100,y=100)
            self.combo.bind("<<ComboboxSelected>>", seleccion)
            
            def Aceptar():
                self.bus.destroy()

            def Cancelar():
                self.bus.destroy()
            self.bt1=Button(self.bus,text="Aceptar",font=('Eras Bold ITC',12),
                            bg="salmon2",compound="top",width="12",command=Aceptar)
            self.bt1.place(x=100,y=150)
            self.bt2=Button(self.bus,text="Cancelar",font=('Eras Bold ITC',12),
                            bg="salmon2",compound="top",width="12",command=Cancelar)
            self.bt2.place(x=255,y=150)

                
        #botones
        self.bt1=Button(self.productos,text="Nuevo",font=('Eras Bold ITC',12),
                        bg="gray65",image=self.im1,compound="top", command=self.Nuevo)
        self.bt1.place(x=270,y=580)
        self.bt2=Button(self.productos,text="Guardar",font=('Eras Bold ITC',12),
                        bg="gray65",image=self.im2,compound="top",command=Guardar)
        self.bt2.place(x=375,y=580)
        self.bt3=Button(self.productos,text="Buscar",font=('Eras Bold ITC',12),
                        bg="gray65",image=self.im3,compound="top",command=Buscar)
        self.bt3.place(x=60,y=580)
        self.bt4=Button(self.productos,text="Listado",font=('Eras Bold ITC',12),
                        bg="gray65",image=self.im4,compound="top",command=lambda:Mn.Mnu.Tabla(self,"hproduct"))
        self.bt4.place(x=165,y=580)   
        self.bt5=Button(self.productos,text="Cerrar",font=('Eras Bold ITC',12),
                        bg="gray65",image=self.im5,compound="top",command=Close)
        self.bt5.place(x=780,y=580)

        #menus
        self.img1 = tk.PhotoImage(file="media/img2.png")
        self.img2 = tk.PhotoImage(file="media/img1.png")
        self.img3 = tk.PhotoImage(file="media/img3.png")
        self.img4 = tk.PhotoImage(file="media/img4.png")
        self.img5 = tk.PhotoImage(file="media/img5.png")
        archivo=ttk.Style()
        archivo.configure("TMenubutton",font="Arial 14")
        menu=ttk.Menubutton(self.productos,text="Archivo")
        ItemMenu=Menu(menu,font="Arial 12",tearoff=0)
        ItemMenu.add_command(label="Nuevo",image=self.img1,compound="left",accelerator="F8", command=self.Nuevo)
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Guardar",image=self.img2,compound="left",accelerator="F8",command=Guardar)
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Buscar",image=self.img3,compound="left",accelerator="F8",command=Buscar)
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Listados",image=self.img4,compound="left",accelerator="F8",command=lambda:Mn.Mnu.Tabla(self,"hproduct"))
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Cerrar",image=self.img5,compound="left",command=Close)
        menu.configure(menu=ItemMenu)
        menu.place(x=0,y=0)
        self.productos.mainloop()
        
    def Nuevo(self):
        acu=0
        with open("data/hproduct.txt") as f: 
            for linea in f:
                x=linea.split(";")
                acu+=1
            
        self.tb1.config(state=tk.NORMAL)
        self.tb1.delete(0, tk.END)    
        self.tb1.insert(0,str(acu+1))
        self.tb1.config(state=tk.DISABLED)
        self.tb2.delete(0, tk.END)
        self.combo1.current(0)
        self.tb4.delete(0, tk.END)
        self.tb5.delete(0, tk.END)
        self.tb6.delete(0, tk.END)
            
    def Actualizar(self,archivo,pos):
        c=0
        x=[]
        lista=[]
        pal=""
        productos=[]
        sld=[]
        cod=[]
        cos=[]
        vent=[]
        actualizar=[]
        uni=[]
        with open("data/hproduct.txt") as f:
            for linea in f:
                x=linea.split(";")
                cod.append(x[0])
                productos.append(x[1])
                uni.append(x[2])
                cos.append(x[3])
                sld.append(x[4])
                vent.append(x[5])
        with open("data/hproduct.txt") as f:
            for linea in f:
                x=linea.split("\n")
                actualizar.append(x)
        cns=[]
        acu=0
        pros=[]
        pr=[] 
        cn=[]
        pr1=""
        pr2=""
        pr3=""
        cn1=""
        cn2=""
        cn3=""
        if archivo=="Entradas":
            with open("data/"+str(archivo)+".txt") as f:
                    for linea in f:
                        x=linea.split(";")
                        pr.append(x[3])
                        cn.append(x[4])
        if archivo=="facturas":
            with open("data/"+archivo+".txt") as f:
                    for linea in f:
                        x=linea.split(";")
                        pr.append(x[4])
                        cn.append(x[5])
        
        pal=""            
        for i in cn[pos]:                
            m=i.split(",")
            acu+=1                
            if i!=",":
                pal+=i
            if acu==len(cn[pos]):
                cns.append(pal)
                if len(cns)==3:
                    cn1=cns[0]
                    cn2=cns[1]
                    cn3=cns[2]                    
            if i=="," or i=="":                   
                cns.append(pal)                    
                pal=""
                if len(cns)==1:
                    cn1=cns[0]
                    cn2="0"
                    cn3="0"
                if len(cns)==2:
                    cn1=cns[0]
                    cn2=cns[1]
                    cn3="0"                    
                else:
                    if len(cns)==0:
                        cn1="0"
                        cn2="0"
                        cn3="0"          

        pal=""
        for i in pr[pos]:                
                m=i.split(",")                
                if i!=",":                   
                    pal+=i                    
                    for j in range(len(productos)):                        
                        if pal==productos[j]:                            
                            pros.append(pal)
                            
                            pal=""                            
                            if len(pros)==1:
                                pr1=pros[0]
                                pr2=""
                                pr3=""           
                            if len(pros)==2:
                                pr1=pros[0]
                                pr2=pros[1]
                                pr3=""
                            if len(pros)==3:
                                pr1=pros[0]
                                pr2=pros[1]
                                pr3=pros[2]
                            else:
                                if len(pros)==0:
                                    pr1=""
                                    pr2=""
                                    pr3=""
        lis=[]
        if archivo=="facturas":
            for i in range(len(productos)):
                print(i)
                if pr1==productos[i]:
                    sld[i]=-int(cn1)+int(sld[i])
                    print(sld[i])
                    if int(sld[i])<0:
                        messagebox.showinfo(message="No hay Prodcutos suficientes",title="Inventario")
                        return(1)
                    lis.append(sld[i])
                if pr2==productos[i]:
                    sld[i]=-int(cn2)+int(sld[i])
                    if int(sld[i])<0:
                        messagebox.showinfo(message="No hay Prodcutos suficientes",title="Inventario")
                        return(1)
                    lis.append(sld[i])
                if pr3==productos[i]:
                    sld[i]=-int(cn3)+int(sld[i])
                    if int(sld[i])<0:
                        messagebox.showinfo(message="No hay Prodcutos suficientes",title="Inventario")
                        return(1)
                    lis.append(sld[i])
            for i in range(len(productos)):
                if int(sld[i])>0:
                    if pr1==productos[i]:
                        texto=str(cod[i])+";"+str(productos[i])+";"+str(uni[i])+";"+str(cos[i])+";"+str(lis[0])+";"+str(vent[i])
                        actualizar[i]=texto
                        if int(cn2)==0:
                            texto=str(cod[i+1])+";"+str(productos[i+1])+";"+str(uni[i+1])+";"+str(cos[i+1])+";"+str(0)+";"+str(vent[i+1])
                            actualizar[i+1]=texto
                        if int(cn3)==0:
                            texto=str(cod[i+2])+";"+str(productos[i+2])+";"+str(uni[i+2])+";"+str(cos[i+2])+";"+str(0)+";"+str(vent[i+2])
                            actualizar[i+2]=texto
                    if pr2==productos[i]:
                        texto=str(cod[i])+";"+str(productos[i])+";"+str(uni[i])+";"+str(cos[i])+";"+str(lis[1])+";"+str(vent[i])
                        actualizar[i]=texto
                        if int(cn3)==0:
                            texto=str(cod[i+1])+";"+str(productos[i+1])+";"+str(uni[i+1])+";"+str(cos[i+1])+";"+str(0)+";"+str(vent[i+1])
                            actualizar[i+1]=texto
                    if pr3==productos[i]:
                        texto=str(cod[i])+";"+str(productos[i])+";"+str(uni[i])+";"+str(cos[i])+";"+str(lis[2])+";"+str(vent[i])
                        actualizar[i]=texto
                else:
                    break
                
        elif archivo=="Entradas":
            for i in range(len(productos)):
                if pr1==productos[i]:
                    sld[i]=int(cn1)+int(sld[i])                    
                   
                    lis.append(sld[i])
                if pr2==productos[i]:
                    sld[i]=int(cn2)+int(sld[i])
                   
                    lis.append(sld[i])
                if pr3==productos[i]:
                    sld[i]=int(cn3)+int(sld[i])
                  
                    lis.append(sld[i])
            for i in range(len(productos)):
                if pr1==productos[i]:
                    texto=str(cod[i])+";"+str(productos[i])+";"+str(uni[i])+";"+str(cos[i])+";"+str(lis[0])+";"+str(vent[i])
                    actualizar[i]=texto
                if pr2==productos[i]:
                    texto=str(cod[i])+";"+str(productos[i])+";"+str(uni[i])+";"+str(cos[i])+";"+str(lis[1])+";"+str(vent[i])
                    actualizar[i]=texto
                if pr3==productos[i]:
                    texto=str(cod[i])+";"+str(productos[i])+";"+str(uni[i])+";"+str(cos[i])+";"+str(lis[2])+";"+str(vent[i])
                    actualizar[i]=texto      
        c=0
        datos=[]
        for j in actualizar:                        
            for x in j:
                pal+=x.replace('\n','')
            pal+='\n'            
            datos.append(pal)
            c+=1
        f=open("data/hproduct.txt",'w')
        for i in datos[len(actualizar)-1]:
            f.write(str(i))
        f.close()
        Mn.Mnu.Tabla(self,"hproduct")  
   
     
        
if __name__=="__main__":
    Prd()
