    #  * HACK-9
    #  //agregar tú alias al inicio
    #  [100,200,300,400,500,600,700]  result >  [foo,100,200,300,400,500,600,700]

def fn_hack_9(result):
    result.insert(0,"charlie")
    return result

result = fn_hack_9([100,200,300,400,500,600,700])
print(result)