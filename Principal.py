from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from about import *
import Productos as Pro
import clientes as cln
import Proveedores as prve
import Entradas as ent
import Facturas as fact
import AjuAdmin as AjA
import AjUsers as AjU
import inicio as log



class Mnu:
    def __init__(self):
        self.principal=Tk()
        self.principal.title("SAMI - Software de Apoyo de MicroTienda")
        self.principal.config(bg="white")
        self.principal.geometry("920x750")
        self.principal.resizable(0,0)
        
      
        #FONDO
        bg = PhotoImage(file = "media/principal.png") 
        canvas1 = Canvas( self.principal, width = 920, height = 700)  
        canvas1.pack(fill = "both", expand = True) 
        canvas1.create_image( 0, 0, image = bg, anchor = "nw")

      
        

        #BT1 IMAGEN
        self.im1=PhotoImage(file="media/mini/Productos.png")
        self.im2=PhotoImage(file="media/mini/Clientes.png")
        self.im3=PhotoImage(file="media/mini/Prveedores.png")
        self.im4=PhotoImage(file="media/mini/Entradas.png")
        self.im5=PhotoImage(file="media/mini/Facturas.png")
        self.im6=PhotoImage(file="media/mini/Ajustes.png")
                
        def Pr(x):
            self.principal.destroy()
            if x==0:
                log.Login()
            if x==1:
                Pro.Prd()
            if x==2:
                cln.Clt()
            if x==3:
                prve.Prv()
            if x==4:
                ent.Ent()
            if x==5:
                fact.Fac()    
        def Acerca():
            About()
            
        self.bt1=Button(self.principal,text="  Productos  ",font=('Verdana',13),image=self.im1,
                        compound="top",command=lambda:Pr(1),bd=6,activebackground='gray',bg='DodgerBlue4',fg="white")
        self.bt1.place(x=105,y=230)
        self.bt2=Button(self.principal,text="  Clientes   ",font=('Verdana',13),image=self.im2,
                        compound="top",command=lambda:Pr(2),bd=6,activebackground='gray',bg='DodgerBlue4',fg="white")
        self.bt2.place(x=300,y=420)
        self.bt3=Button(self.principal,text="Proveedores",font=('Verdana',13),image=self.im3,
                        compound="top",command=lambda:Pr(3),bd=6,activebackground='gray',bg='DodgerBlue4',fg="white")
        self.bt3.place(x=300,y=230)
        self.bt4=Button(self.principal,text="   Entradas   ",font=('Verdana',13),image=self.im4,
                        compound="top",command=lambda:Pr(4),bd=6,activebackground='gray',bg='DodgerBlue4',fg="white")
        self.bt4.place(x=495,y=230)
        self.bt5=Button(self.principal,text="  Facturas   ",font=('Verdana',13),image=self.im5,
                        compound="top",command=lambda:Pr(5),bd=6,activebackground='gray',bg='DodgerBlue4',fg="white")
        self.bt5.place(x=690,y=230)
        self.bt6=Button(self.principal,text="  Ajustes    ",font=('Verdana',13),image=self.im6,
                        compound="top",command=self.Ajust,bd=6,activebackground='gray',bg='DodgerBlue4',fg="white")
        self.bt6.place(x=495,y=420)

        self.imm1=PhotoImage(file="media/productosm.png")
        self.imm2=PhotoImage(file="media/clientesm.png")
        self.imm3=PhotoImage(file="media/proveedoresm.png")
        self.imm4=PhotoImage(file="media/entradasm.png")
        self.imm5=PhotoImage(file="media/facturasm.png")
        self.imm6=PhotoImage(file="media/ajustesm.png")
        self.imm7=PhotoImage(file="media/img5.png")

        archivo=ttk.Style()
        archivo.configure("TMenubutton",font="Arial 14")
        menu=ttk.Menubutton(self.principal,text="Archivo")
        ItemMenu=Menu(menu,font="Arial 12",tearoff=False)
        ItemMenu.add_command(label="Productos",image=self.imm1,compound="left",accelerator="F2",
                             command=lambda:Pr(1))
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Clientes",image=self.imm2,compound="left",accelerator="F3",
                             command=lambda:Pr(2))
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Proveedores",image=self.imm3,compound="left",accelerator="F5",
                             command=lambda:Pr(3))
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Entradas",image=self.imm4,compound="left",accelerator="F6",
                             command=lambda:Pr(4))
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Facturas",image=self.imm5,compound="left",accelerator="F7",
                             command=lambda:Pr(5))
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Ajustes",image=self.imm6,compound="left",accelerator="F8")
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Cerrar",image=self.imm7,compound="left",command=lambda:Pr(0))
        menu.configure(menu=ItemMenu)
        menu.place(x=0,y=0)
        
        Acercade=ttk.Style()
        Acercade.configure("TMenubutton2",font="Arial 14")
        menu=ttk.Menubutton(self.principal,text="Ayuda")
        ItemMenu=Menu(menu,font="Arial 12",tearoff=0)
        ItemMenu.add_command(label="Acerca de ",command=Acerca)
        menu.configure(menu=ItemMenu)
        menu.place(x=96,y=0)
        
        self.principal.mainloop()
        

######metodo     

    def Ajust(self):
        ajustes=Toplevel()
        ajustes.title("SAMI - Software de Apoyo de MicroTienda")
        ajustes.config(bg="white")
        ajustes.geometry("520x320")
        ajustes.resizable(0,0)

        self.img1=PhotoImage(file=("media/Ajustes.png"))
        self.img2=PhotoImage(file=("media/Clientesm.png"))
        self.img3=PhotoImage(file=("media/Proveedoresm.png"))
        def Close():
            ajustes.destroy()     
               
        def AnadirU():
            ajustes.destroy()
            self.principal.destroy()
            AjU.AjuUser()
                
        def AjustesU():
            ajustes.destroy()
            self.principal.destroy()
            AjA.Aju()
                
                
        lb1= Label(ajustes, image=self.img1, bg="white")
        lb1.place(x=20,y=5)
        lb2=Label(ajustes, text="Ajustes", bg="white",font=('Rockwell Extra Bold', 48,'bold'),
                fg="gold")
        lb2.place(x=170,y=40)

            
        self.bt1=Button(ajustes,text="Añadir Usuario",font=('Eras Bold ITC',12),
                        bg="Khaki",compound="top",width="50",command=AnadirU)
        self.bt1.place(x=5,y=160)
            
        self.bt2=Button(ajustes,text="Configurar Usuarios",font=('Eras Bold ITC',12),
                        bg="Khaki",compound="top",width="50",command=AjustesU)
        self.bt2.place(x=5,y=200)
        self.bt3=Button(ajustes,text="Cerrar",font=('Eras Bold ITC',12),
                        bg="Khaki",compound="top",command=Close)
        self.bt3.place(x=450,y=280)
##########Botoneeeeeesss

    def Tabla(self,name): 
        self.root = Toplevel()
        self.root.title("LISTADOS")
        if name=="hproduct":
            self.p1=["CODIGO"]
            self.p2=["PRODUCTOS"]
            self.p3=["UNIDAD"]
            self.p4=["V.UNITARIO"]
            self.p5=["SALDO"]
            self.p6=["PRECIO VENTA"]
            self.p7=[""]

        if name=="clientes":
            self.p1=["CODIGO"]
            self.p2=["NOMBRE"]
            self.p3=["DIRECCIÓN"]
            self.p4=["TELEFONO"]
            self.p5=["SALDO"]
            self.p6=[""]
            self.p7=[""]
        #command=lambda:Mn.Mnu.Tabla(self,"facturas")

        if name=="provedores":
            self.p1=["NIT"]
            self.p2=["NOMBRE"]
            self.p3=["DIRECCIÓN"]
            self.p4=["TELEFONO"]
            self.p5=["CARTERA"]
            self.p6=[""]
            self.p7=[""]

        if name=="Entradas":
            self.p1=["NUMERO"]
            self.p2=["FECHA"]
            self.p3=["PROVEEDOR"]
            self.p4=["PRODUCTOS"]
            self.p5=["CANTIDAD"]
            self.p6=["V.UNITARIO"]
            self.p7=[""]
            
        if name=="facturas":
            self.p1=["NUMERO"]
            self.p2=["FECHA"]
            self.p3=["CLIENTES"]
            self.p4=["TIPO"]
            self.p5=["PRODUCTOS"]
            self.p6=["CANTIDAD"]
            self.p7=["V.UNITARIO"]

        self.y=0
        self.z=0   
        with open("data/"+name+".txt") as f:
             
            for self.linea in f:
                listax=self.linea.split(";")
                self.p1.append(listax[0])
                self.p2.append(listax[1])
                self.p3.append(listax[2])
                self.p4.append(listax[3])
                self.p5.append(listax[4])
                if self.p6[0]!="":self.p6.append(listax[5])
                else:self.y=5
                if self.p7[0]!="":self.p7.append(listax[6])
                else:self.z=6
                
                
                    
        self.lis=[self.p1,self.p2,self.p3,self.p4,self.p5,self.p6,self.p7]               
        
        
        if self.y==5:
            self.lis.pop(self.lis.index(self.p6))
        if self.z==6:
            self.lis.pop(self.lis.index(self.p7))

        
        self.total_rows =len(self.lis[0])
        self.total_columns =len(self.lis)
        
        for i in range(self.total_rows): 
            for j in range(self.total_columns):             
                self.e = Entry(self.root, width=15,justify=CENTER, fg='black', 
                                    font=('Arial',12,'bold')) 
                self.e.grid(row=i, column=j) 
                self.e.insert(END, self.lis[j][i])
        

    def Alterno(self,archivo,ps):
        actualizar=[]
        c=0
        with open(archivo) as f:
            for linea in f:
                x=linea.split(";")
                actualizar.append(x)
                c+=1
        if archivo=="data/hproduct.txt":
            text=[str(self.tb1.get())+";"+str(self.tb2.get())+";"+str(self.combo1.get())+
                  ";"+str(self.tb4.get())+";"+str(self.tb5.get())+";"+str(self.tb6.get())]
            cant=5
        if archivo=="data/clientes.txt" or archivo=="data/provedores.txt":
            text=[str(self.tb1.get())+";"+str(self.tb2.get())+";"+str(self.tb3.get())+";"+
                  str(self.tb4.get())+";"+str(self.tb5.get())]
            cant=4
            
        actualizar[ps]=text
            
        pal=""
        datos=[]
        c=0
        for i in actualizar:
            for x in i:
                if c==ps:
                    pal+=x.replace('\n','')
                else:
                    if x==i[cant]:
                        pal+=x.replace('\n','')
                    else:
                        pal+=x+';'
            pal+='\n'            
            datos.append(pal)
            c+=1

        f=open(archivo,'w')
        for i in datos[c-1]:
            
            f.write(str(i))
            
        f.close()
        messagebox.showinfo(message="El producto se ha actualizado",title="Productos")
        self.Nuevo()
                
if __name__=="__main__":
    Mnu()
    
        

    
