from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Principal as Mn
import tkinter as tk
from datetime import date
import Entradas as et
import Productos as pts


class Fac:
    def __init__(self):
        self.fact=Tk()
        self.fact.title("SAMI - Software de Apoyo de MicroMercado")
        self.fact.config(bg="light cyan")
        self.fact.geometry("920x700")
        self.fact.resizable(0,0)

        #titulo
        Label(self.fact, text="Facturas", bg="light cyan",font=('Rockwell Extra Bold', 48,'bold'),
              fg="violet red").place(x=270,y=60)
        self.log=PhotoImage(file="media/Facturas.png")
        Label(self.fact, image=self.log, bg="light cyan").place(x=120,y=28)

        #imagenes
        self.im1=PhotoImage(file="media/Nuevo.png")
        self.im2=PhotoImage(file="media/Guardar.png")
        self.im3=PhotoImage(file="media/Buscar.png")
        self.im4=PhotoImage(file="media/Listas.png")
        self.im5=PhotoImage(file="media/Cerrar.png")
        self.im6=PhotoImage(file="media/Productos.png")



                 #FONDO
        bg = PhotoImage(file = "media/factt.png") 
        canvas1 = Canvas( self.fact, width = 920, height = 700)  
        canvas1.pack(fill = "both", expand = True) 
        canvas1.create_image( 0, 30, image = bg, anchor = "nw")


        #Titulos
        tl1=Label(self.fact,text="➤ Número:",bg="light cyan",font=("Arial",14,"bold"),fg="black")
        tl1.place(x=170,y=197)
        tl2=Label(self.fact,text="➤ Fecha:",bg="light cyan",font=("Arial",14,"bold"),fg="black")
        tl2.place(x=170,y=247)
        tl3=Label(self.fact,text="➤ Cliente:",bg="light cyan",font=("Arial",14,"bold"),fg="black")
        tl3.place(x=170,y=297)
        tl5=Label(self.fact,text="Productos:",bg="light cyan",font=("Arial",14,"bold"),fg="black")
        tl5.place(x=230,y=397)
        tl6=Label(self.fact,text="Cantidad:",bg="light cyan",font=("Arial",14,"bold"),fg="black")
        tl6.place(x=430,y=397)
        tl4=Label(self.fact,text="➤ Tipo:",bg="mint cream",font=("Arial",14,"bold"),fg="black")
        tl4.place(x=170,y=347)
        tl7=Label(self.fact,text="Valor unitario:",bg="mint cream",font=("Arial",14,"bold"),fg="black")
        tl7.place(x=580,y=397)
        tl8=Label(self.fact,text="Total:",bg="mint cream",font=("Arial",14,"bold"),fg="black")
        tl8.place(x=540,y=590)
            
        #IntVar,DoubleVar,StringVar
        self.x=IntVar()

        #Radiobutton, es de selección única
        rb1=Radiobutton(self.fact,text="1. Crédito",variable=self.x,value=1,bg="mint cream",
                        font=("Arial",14,"bold"),fg="black")
        rb1.place(x=300,y=347)
        rb2=Radiobutton(self.fact,text="2. Efectivo",variable=self.x,value=2,bg="mint cream",
                        font=("Arial",14,"bold"),fg="black")
        rb2.place(x=500,y=347)
     
        #combobox

        self.tb1=Entry(self.fact,width=20,justify=LEFT,font=("Arial",12),bg="gray98")
        self.tb1.place(x=320,y=200)
        self.tb2=Entry(self.fact,width=20,justify=LEFT,font=("Arial",12),bg="gray98")
        self.tb2.place(x=320,y=250)
        self.acu=0
        with open("data/facturas.txt") as f:
            for linea in f:
                x=linea.split(";")
                self.acu+=1
            
        self.tb1.insert(0,str(self.acu))
        self.tb1.config(state=tk.DISABLED)
        
        self.tb2.insert(0,date.today())
        self.tb2.config(state=tk.DISABLED)

        clientes=[""]
        with open("data/clientes.txt") as f:
            for linea in f:
                x=linea.split(";")
                clientes.append(x[1])
                
        self.combo = ttk.Combobox(values=clientes,font=("Arial",12,"bold"),width=40)
        self.combo.place(x=320,y=300)

        self.cod=[""]
        self.productos=[""]
        self.V_U=[""]
        self.cantidad=[""]
        with open("data/hproduct.txt") as f:
            for linea in f:
                x=linea.split(";")
                self.cod.append(x[0])
                self.productos.append(x[1])
                self.V_U.append(x[3])
                self.cantidad.append(x[4])
        self.compras=[]
        def seleccion(event):
            
            def ciclo(x):
                cont=0
                for i in self.productos:
                    if x==i:
                        pos=cont
                        break
                    cont+=1
                return(pos)

            def tot(*_):
                if not(a:=n3.get())or not(b:=n4.get())or not(c:=n5.get())or not(a1:=n6.get())or not(b1:=n7.get())or not(c1:= n8.get()):
                    return
                try:
                    a,b,c,a1,b1,c1 = float(a),float(b),float(c),float(a1),float(b1),float(c1)
                except ValueError:
                    n9.set("0")
                else:
                    if n3.get()=="": a,a1=0
                    if n4.get()=="": b,b1=0
                    if n5.get()=="": c,c1=0
                    n9.set(str(a*a1 + b*b1 + c*c1))

            n3.trace_add("write",tot)
            n4.trace_add("write",tot)
            n5.trace_add("write",tot)
            n6.trace_add("write",tot)
            n7.trace_add("write",tot)
            n8.trace_add("write",tot)
                
            if self.combo2.get()!="" or self.combo3.get()!="" or self.combo4.get()!="":
                self.tb6.config(state=tk.NORMAL)
                self.tb6.delete(0,tk.END)
                x=self.combo2.get()
                pos=ciclo(x)
                if pos==0:
                    self.tb6.insert(0,"0")
                else:
                    self.tb6.insert(0,self.V_U[pos])
                self.tb6.config(state=tk.DISABLED)
                self.tb7.config(state=tk.NORMAL)
                self.tb7.delete(0,tk.END)
                x=self.combo3.get()
                pos=ciclo(x)
                if pos==0:
                    self.tb7.insert(0,"0")
                else:
                    self.tb7.insert(0,self.V_U[pos])
                self.tb7.config(state=tk.DISABLED)
                self.tb8.config(state=tk.NORMAL)
                self.tb8.delete(0,tk.END)
                x=self.combo4.get()
                pos=ciclo(x)
                if pos==0:
                    self.tb8.insert(0,"0")
                else:
                    self.tb8.insert(0,self.V_U[pos])
                self.tb8.config(state=tk.DISABLED)
                
                if self.combo2.get()!="":
                    self.compras.append(self.combo2.get())
                    if self.combo3.get()!="":
                        self.compras.append(self.combo3.get())
                        if self.combo4.get()!="":

                            self.compras.append(self.combo4.get())
                
                ####
                
        
        self.combo = ttk.Combobox(values=clientes,font=("Arial",12,"bold"),width=40)
        self.combo.place(x=320,y=300)
        self.combo2 = ttk.Combobox(values=self.productos,font=("Arial",12,"bold"))
        self.combo2.place(x=180,y=450)
        self.combo2.bind("<<ComboboxSelected>>", seleccion)
        self.combo3 = ttk.Combobox(values=self.productos,font=("Arial",12,"bold"))
        self.combo3.place(x=180,y=500)
        self.combo3.bind("<<ComboboxSelected>>", seleccion)
        self.combo4 = ttk.Combobox(values=self.productos,font=("Arial",12,"bold"))
        self.combo4.place(x=180,y=550)
        self.combo4.bind("<<ComboboxSelected>>", seleccion)


        n3,n4,n5,n6,n7,n8,n9=StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
        
        self.tb3=Entry(self.fact,width=4,justify=LEFT,textvariable=n3,font=("Arial",12),bg="gray98")
        self.tb3.place(x=460,y=450)
        self.tb3.insert(0,"0")
        self.tb4=Entry(self.fact,width=4,justify=LEFT,textvariable=n4,font=("Arial",12),bg="gray98")
        self.tb4.place(x=460,y=500)
        self.tb4.insert(0,"0")
        self.tb5=Entry(self.fact,width=4,justify=LEFT,textvariable=n5,font=("Arial",12),bg="gray98")
        self.tb5.place(x=460,y=550)
        self.tb5.insert(0,"0")
        self.tb6=Entry(self.fact,width=10,justify=LEFT,textvariable=n6,font=("Arial",12),bg="gray98")
        self.tb6.place(x=600,y=450)
        self.tb6.insert(0,"0")
        self.tb6.config(state=tk.DISABLED)
        self.tb7=Entry(self.fact,width=10,justify=LEFT,textvariable=n7,font=("Arial",12),bg="gray98")
        self.tb7.place(x=600,y=500)
        self.tb7.insert(0,"0")
        self.tb7.config(state=tk.DISABLED)
        self.tb8=Entry(self.fact,width=10,justify=LEFT,textvariable=n8,font=("Arial",12),bg="gray98")
        self.tb8.place(x=600,y=550)
        self.tb8.insert(0,"0")
        self.tb8.config(state=tk.DISABLED)
        self.tb9=Entry(self.fact,width=10,justify=LEFT,textvariable=n9,font=("Arial",12),bg="gray98")
        self.tb9.place(x=600,y=592)
        self.tb9.insert(0,"0")
        self.tb9.config(state=tk.DISABLED)

        
        def Close():
            self.fact.destroy() 
            Mn.Mnu()
            
        def valid():
            j=0
            for i in self.productos:
                if self.cantidad[j]=="0":
                    if self.combo2.get()==i or self.combo3.get()==i or self.combo4.get()==i:
                        x=1
                        return x,i
                    break
                else:
                    x=0
                j+=1
            return x,i
           

        def Guardar():
            
            if self.combo.get()!="":
                if self.x.get()!=0:
                    if self.tb3.get()!="0" or self.tb4.get()!="0" or self.tb5.get()!="0":
                        if self.combo2.get()!="" or self.combo3.get()!="" or self.combo4.get()!="":
                            valcontrol,i=valid()
                            if valcontrol==0:
                                val=int(self.tb1.get())-1
                                nombre="facturas"
                                p=0
                                ret=et.Ent.Guardar(self,nombre)
                                if ret!=1:
                                    self.factura(val)
                            else:
                                messagebox.showinfo(message="No hay suficiente inventario \ndel producto "+i,
                                            title='Validación de datos')
                        else:
                            messagebox.showinfo(message="Falta seleccionar un producto",title='Validación de datos')
                    else:
                        messagebox.showinfo(message="Debe comprar un producto",title='Validación de datos')
                        
                else:
                    messagebox.showinfo(message="Falta elegir el tipo de pago",title='Validación de datos')
                    
            else:
                messagebox.showinfo(message="Falta digitar el nombre del cliente",title='Validación de datos')

        def Buscar():
            
            self.bus=Toplevel()
            self.bus.title("SAMI - Software de Apoyo de MicroTienda")
            self.bus.config(bg="slategray1")
            self.bus.geometry("520x200")
            self.bus.resizable(0,0)
            
            self.numero=[]
            self.fecha=[]
            self.cliente=[]
            self.pr=[]
            self.cn=[]
            self.tipo=[]
            self.vl=[]
            self.total=[]
            
            with open("data/facturas.txt") as f:
                for linea in f:
                    x=linea.split(";")
                    self.numero.append(x[0])
                    self.fecha.append(x[1])
                    self.cliente.append(x[2])
                    self.tipo.append(x[3])
                    self.pr.append(x[4])
                    self.cn.append(x[5])                    
                    self.vl.append(x[6])
                    self.total.append(x[7])

           
            
            Label(self.bus, text="  ☞ Buscar factura", bg="slategray1",font=('Rockwell Extra Bold', 30,'bold'),
                  fg="gray3").place(x=20,y=15)
            
            self.combo9 = ttk.Combobox(self.bus,state="readonly",font=("Arial",14),
                                 values=self.numero,width=24)
            self.combo9.place(x=100,y=100)
            
            def Aceptar():
                lol=int(self.combo9.get())
                self.factura(lol)
                self.bus.destroy()

            def Cancelar():
                self.bus.destroy()
                
            self.bt1=Button(self.bus,text="Aceptar",font=('Eras Bold ITC',12),
                            bg="slategray3",compound="top",width="12",command=Aceptar)
            self.bt1.place(x=100,y=150)
            self.bt2=Button(self.bus,text="Cancelar",font=('Eras Bold ITC',12),
                            bg="slategray3",compound="top",width="12",command=Cancelar)
            self.bt2.place(x=255,y=150) 
        
        #botones
        self.bt1=Button(self.fact,text="Nuevo",font=('Eras Bold ITC',12),
                        bg="lightsteelblue2",image=self.im1,compound="top",command=self.Nuevo)
        self.bt1.place(x=5,y=100)
        self.bt2=Button(self.fact,text="Guardar",font=('Eras Bold ITC',12),
                        bg="lightsteelblue2",image=self.im2,compound="top",command=Guardar)
        self.bt2.place(x=5,y=210)
        self.bt3=Button(self.fact,text="Buscar",font=('Eras Bold ITC',12),
                        bg="lightsteelblue2",image=self.im3,compound="top",command=Buscar)
        self.bt3.place(x=5,y=320)
        self.bt4=Button(self.fact,text="Listado",font=('Eras Bold ITC',12),
                        bg="lightsteelblue2",image=self.im4,compound="top",command=lambda:Mn.Mnu.Tabla(self,"facturas"))
        self.bt4.place(x=5,y=430)
        self.bt5=Button(self.fact,text="Cerrar",font=('Eras Bold ITC',12),
                        bg="lightsteelblue2",image=self.im5,
                   compound="top",command=Close)
        self.bt5.place(x=5,y=540)

        

        #menus
        self.img1 = PhotoImage(file="media/img2.png")
        self.img2 = PhotoImage(file="media/img1.png")
        self.img3 = PhotoImage(file="media/img3.png")
        self.img4 = PhotoImage(file="media/img4.png")
        self.img5 = PhotoImage(file="media/img5.png")
        
        archivo=ttk.Style()
        archivo.configure("TMenubutton",font="Arial 14")
        menu=ttk.Menubutton(self.fact,text="Archivo")
        ItemMenu=Menu(menu,font="Arial 12",tearoff=0)
        ItemMenu.add_command(label="Nuevo",compound="left",accelerator="F8",image=self.img1,command=self.Nuevo)
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Guardar",compound="left",accelerator="F8",image=self.img2,command=Guardar)
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Buscar",compound="left",accelerator="F8",image=self.img3,command=Buscar)
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Listados",compound="left",accelerator="F8",image=self.img4,command=lambda:Mn.Mnu.Tabla(self,"facturas"))
        ItemMenu.add_separator()
        ItemMenu.add_command(label="Cerrar ",compound="left",image=self.img5,command=Close)

        menu.configure(menu=ItemMenu)
        menu.place(x=0,y=0)


        self.fact.mainloop()

    def Nuevo(self):
            
            acu=0
            with open("data/facturas.txt") as f: 
                for linea in f:
                    x=linea.split(";")
                    acu+=1
            
            self.tb1.config(state=tk.NORMAL)
            self.tb1.delete(0, tk.END)    
            self.tb1.insert(0,str(acu))
            self.tb1.config(state=tk.DISABLED)
            
            self.x.set(0)
            
                
                
            self.combo.current(0);self.combo2.current(0);self.combo3.current(0);self.combo4.current(0)

            self.tb2.config(state=tk.NORMAL);self.tb6.config(state=tk.NORMAL)
            self.tb7.config(state=tk.NORMAL);self.tb8.config(state=tk.NORMAL);self.tb9.config(state=tk.NORMAL)

            self.tb2.delete(0, tk.END);self.tb3.delete(0, tk.END)
            self.tb4.delete(0, tk.END);self.tb5.delete(0, tk.END);self.tb6.delete(0, tk.END)
            self.tb7.delete(0, tk.END);self.tb8.delete(0, tk.END);self.tb9.delete(0, tk.END)

            self.tb2.insert(0, date.today());self.tb3.insert(0, "0")
            self.tb4.insert(0, "0");self.tb5.insert(0, "0");self.tb6.insert(0, "0");self.tb7.insert(0, "0")
            self.tb8.insert(0, "0");self.tb9.insert(0, "0")
            
            self.tb1.config(state=tk.DISABLED);self.tb2.config(state=tk.DISABLED);self.tb6.config(state=tk.DISABLED)
            self.tb7.config(state=tk.DISABLED);self.tb8.config(state=tk.DISABLED);self.tb9.config(state=tk.DISABLED)

  

    

    def factura(self,i):
        lisfa=[]
        with open("data/facturas.txt") as r:
            for linea in r:
                x=linea.split(";")
                a=x[4].split(',');b=x[5].split(',');c=x[6].split(',')
                x[4]=a;x[5]=b;x[6]=c
                lisfa.append(x)
                
        archivo="data/factura.txt"
        f=open(archivo,'w')
        f.write("S A M I"+'\n'*2)
        f.write(str(lisfa[i][1])+" _ "*12+"N°"+str(lisfa[i][0])+'\n'*2)
        f.write(" _ "*19+'\n'*2)
        f.write("Producto _ _ _ Cantidad _ _ _ V.U. _ _ _ Valor"+'\n'*2)

        if lisfa[i][4][0]!='':
            f.write(lisfa[i][4][0]+str("_"*(15-len(lisfa[i][4][0])))+str(lisfa[i][5][0])+
                    str("_"*(9-len(lisfa[i][5][0])))+str(lisfa[i][6][0])+str("_"*(8-len(lisfa[i][6][0])))
                    +str(int(lisfa[i][5][0])*int(lisfa[i][6][0]))+'\n'*2)
                
        if lisfa[i][4][1]!='':
            f.write(lisfa[i][4][1]+str("_"*(15-len(lisfa[i][4][1])))+str(lisfa[i][5][1])+
                    str("_"*(9-len(lisfa[i][5][1])))+str(lisfa[i][6][1])+str("_"*(8-len(lisfa[i][6][1])))
                    +str(int(lisfa[i][5][1])*int(lisfa[i][6][1]))+'\n'*2)
                
        if lisfa[i][4][2]!='':
            f.write(lisfa[i][4][2]+str("_"*(15-len(lisfa[i][4][2])))+str(lisfa[i][5][2])+
                    str("_"*(9-len(lisfa[i][5][2])))+str(lisfa[i][6][2])+str("_"*(8-len(lisfa[i][6][2])))
                    +str(int(lisfa[i][5][2])*int(lisfa[i][6][2]))+'\n'*2)
        if lisfa[i][3]==1:
            f.write("Pago:Credito"+" _ "*8)
        else:
            f.write("Pago:Efectivo"+" _ "*8)

        total=lisfa[i][7].replace('\n','')
        f.write("Total:$"+str(total))
        f.close()

        factur=Toplevel()
        factur.title("Factura...")

        Fat='';cont=0
        with open("data/factura.txt") as f:
            for linea in f:
                x=linea
                Fat+=x
                cont+=1

        label2=LabelFrame(factur,font=20,text="Factura",fg="black")
        label2.place(x=20,y=20)

        left = Label(label2,font=20,text = Fat)
        left.pack()

        if cont==11:
            factur.geometry("380x280")
        if cont==13:
            factur.geometry("380x315")
        if cont==15:
            factur.geometry("380x350")
            
if __name__=="__main__":
    Fac()        


    

