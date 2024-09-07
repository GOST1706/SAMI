from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
import Principal as prin
import tkinter.font as tkFont

#Ventana de Inicio
class Login:
    def __init__(self):
        self.login=Tk()
        self.login.title('Login')
        self.login.geometry('1024x650')
        self.login.config(bg='azure')
        self.login.resizable(0,0)
        imagen23=PhotoImage(file="media/imagen12.png")

        bg = PhotoImage(file = "media/malla2.png") 
        canvas1 = Canvas( self.login, width = 1024, height = 650)  
        canvas1.pack(fill = "both", expand = True) 
        canvas1.create_image( 0, 0, image = bg, anchor = "nw")
        canvas1.create_image( 40, 560, image = imagen23, anchor = "nw")


        #Datos de inicio
        Usuario2=Entry(self.login,width=26,font=('Lucida',14),bg='white')
        Usuario2.place(x=630,y=340)
        Usuario2.focus()
        ContraR=Entry(self.login,width=26,show=('*'),font=('Lucida',14),bg='white')
        ContraR.place(x=630,y=455)
        
        #Boton de registro
        def inicio(event):

            a=125
            b=550
            if len(Usuario2.get())==0 or len(ContraR.get())==0:
                vl=Label(self.login,text='Los Campos No Pueden Estar Vacios',bg='azure',fg='red',font=('Lucida',11))
                vl.place(x=a,y=b)
            else:
                plog={}
                with open('data/Usuarios.txt') as f:
                    for line in f:
                        (us,pasw,estado)=line.split()
                        plog[str(us)] = [pasw,estado]
                c=0
                for key in plog:
                    c+=1
                comp=0
                x=0
                for key in plog:
                    comp+=1
                    if str(key)==str(Usuario2.get()):
                        #x válida si el usuario ingresado existe
                        x=1
                    if str(key)==str(Usuario2.get()) and plog[key][0]==ContraR.get():
                        if int(plog[key][1])==1:
                            #comp me válida que el usuario y la contraseña sean correctos
                            comp=c+1
                            self.login.destroy()
                            prin.Mnu()
                        else:
                            comp=5
                            vl=Label(self.login,text='                    Usuario inactivo                    ',bg='azure',fg='red',font=('Lucida',11))
                            vl.place(x=a,y=b)


                if x==0:
                    vl=Label(self.login,text='           Usuario no encontrado             ',bg='azure',fg='red',font=('Lucida',11))
                    vl.place(x=a,y=b)
                else:
                    if c==comp:
                        vl=Label(self.login,text='Usuario y/o contraseña incorrectos       ',bg='azure',fg='red',font=('Lucida',11))
                        vl.place(x=a,y=b)

        #función que enlaza y desenlaza el return para que funcione el enter
        def bind_return(event):
            Usuario2.unbind('<Return>')
            ContraR.unbind('<Return>')
            inicio(event)
            Usuario2.bind('<Return>', bind_return)
            ContraR.bind('<Return>', bind_return)

        #enlazar el return
        Usuario2.bind('<Return>', bind_return)
        ContraR.bind('<Return>', bind_return)

        def Close():
            r= MessageBox.askquestion("Close","¿Está seguro que desea cerrar la aplicación?")
            if r=="yes":
                self.login.quit()
                self.login.destroy()
            else:
                #showwarning, showinfo, entre otras
                r= MessageBox.showinfo("Close","Continua en el programa")

                
        archivo="data/Usuarios.txt"
        aceptar=PhotoImage(file="media/aceptarr.png")
        cerrar=PhotoImage(file="media/cerrarr.png")
        
        Ingreso = Button( width=148, height=52, image=aceptar,command=lambda:inicio(0))
        Ingreso.place(x=570, y=550)
        Ingreso2 = Button( width=150, height=52, image=cerrar,command=Close)
        Ingreso2.place(x=840, y=550)
        self.login.bind('<Return>',inicio) #enter = a inicio
        self.login.mainloop()
#logo uis
        
        
        

if __name__=="__main__":
    Login()
