# * HACK-2
#      //eliminar el primer item
#      [100,200,300,400,500,600,700]  result >  [200,300,400,500,600,700] 

def fn_hack_2(result):

    del result[0]

    return result

result = fn_hack_2([100,200,300,400,500,600,700])
print(result)