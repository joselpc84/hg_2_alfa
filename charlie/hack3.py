# * HACK-3
#      //eliminar el último item
#      [100,200,300,400,500,600,700]  result >  [100,200,300,400,500,600]

def fn_hack_2(result):

    result.pop(-1)

    return result

result = fn_hack_2([100,200,300,400,500,600,700])
print(result)