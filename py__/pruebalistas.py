with open("data/facturas.txt") as r:
    for linea in r:
        x=linea.split(";")
        a=x[4].split(',')
        print(a)
        lisfa.append(x)
        cont+=1
