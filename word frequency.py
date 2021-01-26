def main():
    file=open(r'C:\Users\Ermi_D\Desktop\practice\practice.txt','r')
    lines=[]
    word_frequency={};
    while(True):
        t=file.readline()
        if t=='':
            break
        lines.append(t)
    for i in  range(len(lines)):
        lines[i]=lines[i].rstrip('\n')
        lines[i]=lines[i].split()
        for j in range(len(lines[i])):
            if lines[i][j] in word_frequency:
                word_frequency[lines[i][j]]=word_frequency[lines[i][j]]+1
            else:
                word_frequency[lines[i][j]]=1
    for i in range(len(word_frequency)):
        print(format(list(word_frequency.keys())[i],'10s'),\
              format(list(word_frequency.values())[i],'2d'),sep='=')
    
main()
