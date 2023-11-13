#HACK-8 
#//agregar tú alias al final
#[100,200,300,400,500,600,700]  result >  [100,200,300,400,500,600,700,foo]

def hack_8(lista):
    lista.append("Delta")
    return lista

print(hack_8([100,200,300,400,500,600,700]))