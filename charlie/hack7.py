#   * HACK-7 
#      //remplazar el item 300 
#      //por tú alias
#      [100,200,300,400,500,600,700]  result >  [100,200,foo,400,500,600,700]

def fn_hack_7(result):

    result[2] = str(result[2])
    
    result[2] = result[2].replace("300","charlie")

    return result

result = fn_hack_7([100,200,300,400,500,600,700])
print(result)