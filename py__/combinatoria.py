lista=['20000','50000']

def potencia(c):
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]

def combinaciones(c, n):
    return [s for s in potencia(c) if len(s) == n]

pal=combinaciones(lista,6)

print(pal)
