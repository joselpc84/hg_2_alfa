# José Luis Pérez - Alfa
# Hack 4
# Eliminar los items 300 y 500

def fn_hack_4(result):
    while 300 in result:
        result.remove(300)
    while 500 in result:
        result.remove(500)
    return result

# lista = [100,200,300,400,500,600,700,800,900]
# valor = fn_hack_4(lista)
# print(valor)