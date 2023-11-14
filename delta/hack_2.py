#HACK-2
#//eliminar el primer item
#[100,200,300,400,500,600,700]  result >  [200,300,400,500,600,700]

def hack_2(lista):
    lista.pop(0)
    return lista

print(hack_2([100,200,300,400,500,600,700]))