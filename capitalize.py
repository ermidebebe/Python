def capitalize(string):
    array=string.split(' ')
    for i in range(len(array)):
        if array[i].isalpha() and array[i][0].isalpha():
            array[i]=array[i][0].upper()+array[i].lstrip(array[i][0])
    return ' '.join(array)
string=input('sentence>>')
print(capitalize(string))