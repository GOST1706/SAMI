from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Principal as Mn
from datetime import date
import tkinter as tk
import Productos as pts

class Ent:
    def __init__(self):
        self.cli=Tk()
        self.cli.title("SAMI - Software de Apoyo de MicroMercado")
        self.cli.config(bg="mint cream")
        self.cli.geometry("920x700")
        self.cli.resizable(0,0)

        
         #FONDO
        bg = PhotoImage(file = "media/entradass.png") 
        canvas1 = Canvas( self.cli, width = 920, height = 700)  
        canvas1.pack(fill = "both", expand = True) 
        canvas1.create_image( 0, 0, image = bg, anchor = "nw")
        #imagenes
        self.im1=PhotoImage(file="media/Nuevo.png")
        self.im2=PhotoImage(file="media/Guardar.png")
        self.im3=PhotoImage(file="media/Buscar.png")
        self.im4=PhotoImage(file="media/Listas.png")
        self.im5=PhotoImage(file="media/Cerrar.png")
        self.im6=PhotoImage(file="media/Productos.png")

       


        #Titulos
        tl1=Label(self.cli,text="➤ Número:",bg="mint cream",font=("Arial",14,"bold"),fg="black")
        tl1.place(x=500,y=250)
        tl2=Label(self.cli,text="➤ Fecha:",bg="mint cream",font=("Arial",14,"bold"),fg="black")
        tl2.place(x=80,y=250)
        tl3=Label(self.cli,text="➤ Proveedor:",bg="mint cream",font=("Arial",14,"bold"),fg="black")
        tl3.place(x=80,y=300)
       
        tl5=Label(self.cli,text="Producto:",bg="mint cream",font=("Arial",14,"bold"),fg="black")
        tl5.place(x=230,y=347)
        tl6=Label(self.cli,text="Cantidad:",bg="mint cream",font=("Arial",14,"bold"),fg="black")
        tl6.place(x=430,y=347)
        tl7=Label(self.cli,text="Valor unitario:",bg="mint cream",font=("Arial",14,"bold"),fg="black")
        tl7.place(x=580,y=347)
        
        def seleccion(event):
            self.tb1.config(state=tk.NORMAL)
            self.tb2.config(state=tk.NORMAL)
            self.tb1.delete(0,tk.END)
            self.tb2.delete(0,tk.END)
            self.combo.delete(0,tk.END)

            
            
            self.combo2.delete(0,tk.END)
            self.combo3.delete(0,tk.END)
            self.combo4.delete(0,tk.END)
            self.tb3.delete(0,tk.END)
            self.tb4.delete(0,tk.END)
            self.tb5.delete(0,tk.END)
            
            self.tb6.config(state=tk.NORMAL)
            self.tb7.config(state=tk.NORMAL)
            self.tb8.config(state=tk.NORMAL)
            
            self.tb6.delete(0,tk.END)
            self.tb7.delete(0,tk.END)
            self.tb8.delete(0,tk.END)
            
            cont=0
            x=self.combo9.get()
            self.pos=int(self.combo9.get())-1
            self.prs=[]
            pal=""
            for i in self.pr[self.pos]:                
                m=i.split(",")                
                if i!=",":                   
                    pal+=i                    
                    for j in range(len(self.productos)):                        
                        if pal==self.productos[j]:                            
                            self.prs.append(pal)
                            pal=""                            
                            if len(self.prs)==1:
                                self.pr1=self.prs[0]
                                self.pr2=""
                                self.pr3=""           
                            if len(self.prs)==2:
                                self.pr1=self.prs[0]
                                self.pr2=self.prs[1]
                                self.pr3=""
                            if len(self.prs)==3:
                                self.pr1=self.prs[0]
                                self.pr2=self.prs[1]
                                self.pr3=self.prs[2]
                            else:
                                if len(self.prs)==0:
                                    self.pr1=""
                                    self.pr2=""
                                    self.pr3=""
                                    
            pal=""
            self.cns=[]
            acu=0
            print(len(self.cn[self.pos]))
            
            for i in self.cn[self.pos]:                
                m=i.split(",")
                
                acu+=1
                
                if i!=",":
                    pal+=i
                    
                if acu==len(self.cn[self.pos]):
                    self.cns.append(pal)
                    if len(self.cns)==3:
                        cn1=self.cns[0]
                        cn2=self.cns[1]
                        cn3=self.cns[2]
                    
                if i=="," or i=="":
                   
                    self.cns.append(pal)
                    
                    pal=""
                   
                    if len(self.cns)==1:
                        cn1=self.cns[0]
                        cn2=""
                        cn3=""
                    if len(self.cns)==2:
                        cn1=self.cns[0]
                        cn2=self.cns[1]
                        cn3=""
                    
                    else:
                        if len(self.cns)==0:
                            cn1=""
                            cn2=""
                            cn3=""
            pal=""
            self.vls=[]
            m=[]
            for i in self.vl[self.pos]:                
                m=i.split(",")
                if i!=",":
                    pal+=i
                if i=="\n":
                    self.vls.append(pal)
                    if len(self.vls)==3:
                            vl1=self.vls[0]
                            vl2=self.vls[1]
                            vl3=self.vls[2]
                    
                if i=="," or i=="":
                    self.vls.append(pal)
                    pal=""
                    if len(self.vls)==1:
                        vl1=self.vls[0]
                        vl2=""
                        vl3=""
                    if len(self.vls)==2:
                        vl1=self.vls[0]
                        vl2=self.vls[1]
                        vl3=""
                    else:
                        if len(self.vls)==0:
                            vl1=""
                            vl2=""
                            vl3=""
                            
            self.tb1.insert(0,self.numero[self.pos])
            self.tb1.config(state=tk.DISABLED)
            self.tb2.insert(0,self.fecha[self.pos])
            self.tb2.config(state=tk.DISABLED)
            self.combo.set(self.proveedor[self.pos])
            self.combo2.set(self.pr1)
            self.combo3.set(self.pr2)
            self.combo4.set(self.pr3)
            self.tb3.insert(0,cn1)
            self.tb4.insert(0,cn2)
            self.tb5.insert(0,cn3)
            self.tb6.insert(0,vl1)
            self.tb7.insert(0,vl2)
            self.tb8.insert(0,vl3)

            
        #combobox
        self.acu=0
        with open("data/Entradas.txt") as f:
            for linea in f:
                x=linea.split(";")
                self.acu+=1
        self.tb1=Entry(self.cli,width=20,justify=LEFT,font=("Arial",12),bg="gray98")
        self.tb1.place(x=630,y=250)
        self.tb2=Entry(self.cli,width=20,justify=LEFT,font=("Arial",12),bg="gray98")
        self.tb2.place(x=220,y=250)

        provedores=[""]
        with open("data/provedores.txt") as f:
            for linea in f:
                x=linea.split(";")
                provedores.append(x[1])
                
        self.combo = ttk.Combobox(values=provedores,font=("Arial",12,"bold"),width=40)
        self.combo.place(x=220,y=300)

        self.productos=[""]
        with open("data/hproduct.txt") as f:
            for linea in f:                
                x=linea.split(";")
                self.productos.append(x[1])
                
        self.combo2 = ttk.Combobox(values=self.productos,font=("Arial",12,"bold"))
        self.combo2.place(x=180,y=370)
        self.combo3 = ttk.Combobox(values=self.productos,font=("Arial",12,"bold"))
        self.combo3.place(x=180,y=420)
        self.combo4 = ttk.Combobox(values=self.productos,font=("Arial",12,"bold"))
        self.combo4.place(x=180,y=470)

        self.tb3=Entry(self.cli,width=4,justify=LEFT,font=("Arial",12),bg="gray98")
        self.tb3.place(x=460,y=370)
        self.tb4=Entry(self.cli,width=4,justify=LEFT,font=("Arial",12),bg="gray98")
        self.tb4.place(x=460,y=420)
        self.tb5=Entry(self.cli,width=4,justify=LEFT,font=("Arial",12),bg="gray98")
        self.tb5.place(x=460,y=470)
        self.tb6=Entry(self.cli,width=10,justify=LEFT,font=("Arial",12),bg="gray98")
        self.tb6.place(x=600,y=370)
        self.tb7=Entry(self.cli,width=10,justify=LEFT,font=("Arial",12),bg="gray98")
        self.tb7.place(x=600,y=420)
        self.tb8=Entry(self.cli,width=10,justify=LEFT,font=("Arial",12),bg="gray98")
        self.tb8.place(x=600,y=470)

        self.Nuevo()
        
        
        def Close():            
            self.cli.destroy()
            Mn.Mnu()
            
        def Buscar():
            self.bus=Toplevel()
            self.bus.title("SAMI - Software de Apoyo de MicroTienda")
            self.bus.config(bg="light goldenrod")
            self.bus.geometry("520x200")
            self.bus.resizable(0,0)
            self.numero=[]
            self.fecha=[]
            self.proveedor=[]
            self.pr=[]
            self.pr1=[]            
            self.cn=[]
            self.vl=[]          
            with open("data/entradas.txt") as f:
                for linea in f:
                    x=linea.split(";")
                    self.numero.append(x[0])
                    self.fecha.append(x[1])
                    self.proveedor.append(x[2])
                    self.pr.append(x[3])
                    self.cn.append(x[4])
                    self.vl.append(x[5])
        
                
                

            
                    
            Label(self.bus, text=" ☞ Buscar entradas", bg="light goldenrod",font=('Rockwell Extra Bold', 30,'bold'),
                  fg="midnight blue").place(x=10,y=15)
            
            self.combo9 = ttk.Combobox(self.bus,state="readonly",font=("Arial",14),
                                 values=self.numero,width=24)
            self.combo9.place(x=100,y=100)
            self.combo9.bind("<<ComboboxSelected>>", seleccion)
            
            def Aceptar():
                self.bus.destroy()

            def Cancelar():
                self.bus.destroy()
            self.bt1=Button(self.bus,text="Aceptar",font=('Eras Bold ITC',12),
                            bg="goldenrod",compound="top",width="12",command=Aceptar)
            self.bt1.place(x=100,y=150)
            self.bt2=Button(self.bus,text="Cancelar",font=('Eras Bold ITC',12),
                            bg="goldenrod",compound="top",width="12",command=Cancelar)
            self.bt2.place(x=255,y=150)

            
        #botones
        self.bt1=Button(self.cli,text="Nuevo",font=('Eras Bold ITC',12),
                        bg="gray65",image=self.im1,compound="top", command=self.Nuevo)
        self.bt1.place(x=290,y=535)
        self.bt2=Button(self.cli,text="Guardar",font=('Eras Bold ITC',12),
                        bg="gray65",image=self.im2,compound="top",command=lambda:self.Guardar("Entradas"))
        self.bt2.place(x=395,y=535)
        self.bt3=Button(self.cli,text="Buscar",font=('Eras Bold ITC',12),
                        bg="gray65",image=self.im3,compound="top",command=Buscar)
        self.bt3.place(x=80,y=535)
        self.bt4=Button(self.cli,text="Listado",font=('Eras Bold ITC',12),
                        bg="gray65",image=self.im4,compound="top",command=lambda:Mn.Mnu.Tabla(self,"Entradas"))
        self.bt4.place(x=185,y=535)   
        self.bt5=Button(self.cli,text="Cerrar",font=('Eras Bold ITC',12),
                        bg="gray65",image=self.im5,compound="top",command=Close)
        self.bt5.place(x=780,y=535)

        #menus
        self.img1 = PhotoImage(file="media/img2.png")
        self.img2 = PhotoImage(file="media/img1.png")
        self.img3 = PhotoImage(file="media/img3.png")
        self.img4 = PhotoImage(file="media/img4.png")
        self.img5 = PhotoImage(file="media/img5.png")
        
        archivo=ttk.Style()
        archivo.configure("TMenubutton",font="Arial 14")
        menu=ttk.Menubutton(self.cli,text="Archivo")
        ItemMenu=Menu(menu,font="Arial 12",tearoff=0)
        ItemMenu.add_command(label="Nuevo",compound="left",accelerator="F8",image=self.img1,command=self.Nuevo)
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Guardar",compound="left",accelerator="F8",image=self.img2,command=lambda:self.Guardar("Entradas"))
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Buscar",compound="left",accelerator="F8",image=self.img3,command=Buscar)
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Listados",compound="left",accelerator="F8",image=self.img4,command=lambda:Mn.Mnu.Tabla(self,"Entradas"))
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Cerrar ",compound="left",image=self.img5,command=Close)

        menu.configure(menu=ItemMenu)
        menu.place(x=0,y=0)

        self.cli.mainloop()
 

    def Nuevo(self):
        self.tb1.focus()
        self.combo.current(0);self.combo2.current(0);self.combo3.current(0);self.combo4.current(0)

        self.acu=0
        with open("data/Entradas.txt") as f:
            
            for linea in f:
                x=linea.split(";")
                self.acu+=1
                        
        self.tb1.config(state=tk.NORMAL)
        self.tb1.delete(0, tk.END)
        self.tb1.insert(0, str(self.acu))
        self.tb1.config(state=tk.DISABLED)
        self.tb2.config(state=tk.NORMAL)
        self.tb2.delete(0, tk.END);self.tb3.delete(0, tk.END);self.tb4.delete(0, tk.END)
        self.tb5.delete(0, tk.END);self.tb6.delete(0, tk.END);self.tb7.delete(0, tk.END);self.tb8.delete(0, tk.END)

        self.tb1.insert(0, str(self.acu))
        self.tb2.insert(0, date.today()),self.tb1.config(state=tk.DISABLED);self.tb2.config(state=tk.DISABLED)

    def Guardar(self,nombre):
        if self.tb1.get()!="":
            if self.tb2.get()!="":
                if self.combo.get()!="":
                    if self.combo2.get()!="" or self.combo2.get()!="" or self.combo2.get()!="":
                        if nombre=="facturas":
                            tipo=str(self.x.get())+";"; total=";"+str(self.tb9.get())
                        else:
                            tipo=""; total=""

                        pro1=self.combo2.get();c1=self.tb3.get();vu1=self.tb6.get()
                        if self.combo2.get()=="":
                            pro1=""; c1=0; vu1=0
                        pro2=self.combo3.get();c2=self.tb4.get();vu2=self.tb7.get()
                        if self.combo3.get()=="":
                            pro2=""; c2=0; vu2=0
                        pro3=self.combo4.get();c3=self.tb5.get();vu3=self.tb8.get()
                        if self.combo4.get()=="":
                            pro3=""; c3=0; vu3=0
                        
                        archivo="data/"+str(nombre)+".txt"
                        if nombre=="Entradas":
                            archivo=="data/Entradas.txt"
                            
                            f=open(archivo,"a")
                            f.write(str(self.tb1.get())+";"+str(self.tb2.get())+";"+str(self.combo.get())+";"+
                                    str(pro1)+","+str(pro2)+","+str(pro3)+";"+str(c1)+","+str(c2)+","+str(c3)+";"+
                                    str(vu1)+","+str(vu2)+","+str(vu3)+'\n')
                            f.close()
                            
                        if nombre=="facturas":
                            f=open(archivo,"a")
                            f.write(str(self.tb1.get())+";"+str(self.tb2.get())+";"+str(self.combo.get())+";"+tipo+
                                    str(pro1)+","+str(pro2)+","+str(pro3)+";"+str(c1)+","+str(c2)+","+str(c3)+";"+
                                    str(vu1)+","+str(vu2)+","+str(vu3)+total+'\n')
                            f.close()                        
                        posicion=int(self.acu)
                        ret=pts.Prd.Actualizar(self,nombre,posicion)
                        self.Nuevo()
                        if ret!=1:
                            messagebox.showinfo(message="Se ha guardado con éxito",title=nombre)
                        else:
                            return(1)
                            
                    else:
                        tk.messagebox.showinfo(message="Falta selesccionar un producto",title='Validación de datos')
                else:
                   tk.messagebox.showinfo(message="Falta seleccionar el provedor",title='Validación de datos')
            else:
               tk.messagebox.showinfo(message="Falta digitar la Fecha",title='Validación de datos')
        else:
            tk.messagebox.showinfo(message="Falta digitar el Numero",title='Validación de datos')
        
        
if __name__=="__main__":
    Ent()
    
