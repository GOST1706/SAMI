"""
En primer lugar analizo el problema; es decir miro que es lo que me entregan
y de que forma. Al hacer eso segun el enunciado obtenemos que:

#valhora=salbase/192

#hextr=valhora+valhora*25/100

#bonif=salbase*0,5/100

#saltotal=salbase+nhextr*hextr+nbonif*bonif
                //nhextr y nbonif es el N° de horas extras o bonificaciones

#salud=saltotal*3.5/100

#pension=0,04*saltotal

#cajacomp=0,01*saltotal

#descuentos=salud+pension+cajacomp

Ya una vez hecho este analisis puedo proceder a programar...

salario=saltotal-descuentos
"""

print("ingrese el salario base, numero de horas extras y numero de bonificaciones")
print("separados por un espacio")
salbase,nhextr,nbonif=input().split() #pido los datos que requiero para ejecutar
#luego hay que declarar las variables como numeros debido a que se ingresaron como cadena

salbase=float(salbase) #este se trabaja con float porque pueden haber decimales
nhextr=int(nhextr);nbonif=int(nbonif) #se trabaja int por ser enteros

#primero hallo el salario total para luego poder hacer los descuentos
#para esto hay que definir el valor por hora, hora extra y bonificaciones

valhora=salbase/192
hextr=valhora+valhora*25/100
bonif=salbase*0.05/100

#a partir de esto puedo hallar el salario total antes de descuentos

saltotal=salbase+nhextr*hextr+nbonif*bonif

#una vez tengo el salario total procedo a revisar los descuentos y a sumarlos

salud=saltotal*3.5/100
pension=saltotal*4/100
cajacomp=saltotal*1/100

descuento=salud+pension+cajacomp

#ya que se tenga el descuento procede a restarse de el salario total
#y de esa forma obtengo el salario real que recibe el empleado

salario=saltotal-descuento

#por ultimo muestro el valor obtenido

print("El salario a recibir es: ",salario)
