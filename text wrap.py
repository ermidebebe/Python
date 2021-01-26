def wrap(string, max_width):
    string2=[]
    i=0
    while i<=len(string):
        string2.append(string[i:i+max_width])
        i+=max_width
    return '\n'.join(string2)
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
