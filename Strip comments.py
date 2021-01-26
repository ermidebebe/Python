def solution(string,markers):
    strip=''
    valid=True
    for i in range(len(string.split('\n'))):
        for j in range(len(markers)):
            if  string.split('\n')[i].find(markers[j])!=-1:
                text=string.split('\n')[i].replace(markers[j],'er')
                if i==0:
                    strip+=text[:text.find('er')].rstrip()
                else:
                    strip+='\n'+text[:text.find('er')].rstrip()
                valid=False
                break
        if valid:
            if i==0:
                 strip+=string.split('\n')[i].rstrip()
            else:
                strip+='\n'+string.split('\n')[i].rstrip()
        valid=True
    return strip
print("apples, pears # and bananas\ngrapes\nbananas !apples\n\n")
print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
