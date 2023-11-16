#    * HACK-4
#      //eliminar los items 300 y 500
#      [100,200,300,400,500,600,700]  result >  [100,200,400,600,700]

def fn_hack_4(result):

    del result[2]
    result.pop(3)

    return result

result = fn_hack_4([100,200,300,400,500,600,700])
print(result)