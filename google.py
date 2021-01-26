def main(string) :
    str1=''
    for i in string:
        if i!=' ':
            str1+=i
            print(i)
    string=str1
    print(str1)
    if len(string)!=6:
        return False
    else:
        if(string[0]!='g'and string[0]!='G'):
            return False
        if(string[1]!='o' and  string[1]!='O' and string[1]!='0' and string[1]!='()'and string[1]!='<>' and  string[1]!='[]'):
            return False
        if(string[2]!='o' and  string[2]!='O'and  string[2]!='0'and string[2]!='()'and string[2]!='<>'and string[2]!='[]'):
            return False
        if(string[3]!='g' and string[3]!='G'):
            return False
        if(string[4]!='L' and string[4]!='l'and string[4]!='I'):
            return False
        if(string[5]!='e' and string[5]!='E'and string[5]!='3'):
            return False
        return True


if __name__ == '__main__':
    string = input()
    print(main(string))
