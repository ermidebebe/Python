def print_formatted(number):
    string=[]
    space=len(format(number,'b'))
    deci=len(format(number,'d'))
    for i in range(1,number+1):
                  string.append(format(i,str(deci)+'d')+format(i,str(space+1)+'o')+\
                                format(i,str(space+1)+'X')+format(i,str(space+1)+'b'))
    return '\n'.join(string)
