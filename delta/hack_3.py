#HACK-3
#//eliminar el ultimo item
#[100,200,300,400,500,600,700]  result >  [100,200,300,400,500,600]

def hack_2(lista):
    lista.pop(6)
    return lista

print(hack_2([100,200,300,400,500,600,700]))