# José Luis Pérez - Alfa
# Hack 1
# Vaciar la lista

def fn_hack_1(result):
    tope = len(result)
    i = 0
    while i < tope: 
        result.pop()
        i += 1
    return result

# lista = [100,200,300,400,500,600,700,800,900]
# valor = fn_hack_1(lista)
# print(valor)