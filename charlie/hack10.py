#  * HACK-10 
#      //agregar después del item 500
#      //los alias qux y thud
#      [100,200,300,400,500,600,700]  result >  [100,200,300,400,500,qux,thud,600,700]

def fn_hack_10(result):
    result.insert(5,"qux")
    result.insert(6,"thud")
    return result

result = fn_hack_10([100,200,300,400,500,600,700])
print(result)