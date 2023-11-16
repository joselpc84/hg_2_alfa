    #  * HACK-8 
    #  //agregar tú alias al final
    #  [100,200,300,400,500,600,700]  result >  [100,200,300,400,500,600,700,foo]

def fn_hack_8(result):

    result.append("charlie")

    return result

result = fn_hack_8([100,200,300,400,500,600,700])
print(result)