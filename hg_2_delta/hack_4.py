#HACK-4
#//eliminar los items 300 y 500
#[100,200,300,400,500,600,700]  result >  [100,200,400,600,700]

def hack_4(lista):
    lista.pop(2)
    lista.pop(3)
    return lista

print(hack_4([100,200,300,400,500,600,700]))