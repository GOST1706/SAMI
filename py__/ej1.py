def cajero(valor):
    c=valor//50000
    a=valor//20000
    val=0
    if c>=1:
        valor=valor-50000*c
        if valor==0:
            x=True
            val+=1
        else:
            if valor%20000==0:
                b=valor/20000
                x=True
                val+=1
            else:
                x=False
                v1=50000*c
                valor=valor+50000*c
                
    if a>=1:
        valor=valor-20000*a
        if valor==0:
            x=True
            val+=1
        else:
            if valor%50000==0:
                b=valor/50000
                x=True
                val+=1
            else:
                x=False
                v2=20000*c
                    
    if x==True:
        return x,val
    if x==False:
        if v1>v2:
            return x,v1
        else:
            return x,v2

print(cajero(200000))
