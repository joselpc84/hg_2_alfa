#HACK-9
#//agregar tú alias al inicio
#[100,200,300,400,500,600,700]  result >  [foo,100,200,300,400,500,600,700]

def hack_9(lista):
    lista.insert(0, "Delta")
    return lista

print(hack_9([100,200,300,400,500,600,700]))