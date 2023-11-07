# José Luis Pérez - Alfa
# Hack 7
# Reemplazar el item 300 por tu alias

def fn_hack_7(result):
    for i in range(len(result)):
        if result[i] == 300:
            result[i] = "alfa"
    return result

# lista = [100,200,300,400,500,600,700,800,900]
# valor = fn_hack_7(lista)
# print(valor)