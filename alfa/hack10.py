# José Luis Pérez - Alfa
# Hack 10
# Agregar después del item 500
# los alias qux y thud

def fn_hack_10(result):
    indice = 0
    for i in range(len(result)):
        if result[i] == 500:        
            indice = i
    result.insert(indice+1,"qux")
    result.insert(indice+2,"thud")    
    return result

# lista = [100,200,300,400,500,600,700,800,900]
# valor = fn_hack_10(lista)
# print(valor)