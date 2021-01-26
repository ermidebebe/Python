def assemble(file):
    word=file.split('\n')
    word2=[]
    for code in word:
        if code!='':
            word2.append(code.split(' '))
    opcode={'MOVI':0,'MOVR':1,'LDR':2,'STR':3,'ADD':4,'SUB':4,'SHL':4,'AND':4\
            ,'BRZ':5,'BR':6,'OUT':7}
    for code in word2:
        if opcode[code[0].upper()]==4:
            word2[word2.index(code)]=ALU(code,opcode[code[0].upper()])
        else:
            word2[word2.index(code)]=Memory_access_and_data_transfer(code,opcode[code[0].upper()]) 
            
    return word2
def ALU(code,opcode):
    function_code={'ADD':0,'SUB':1,'SHL':2,'AND':3}
    register={'A':0,'B':1}
    executable=str(opcode*2+register[code[1].upper()])+str(function_code[code[0].upper()])+'0'
    return executable                
    
def Memory_access_and_data_transfer(code,opcode):
    register={'A':0,'B':1}
    if opcode==2 or opcode==3:
        if code[1].endswith(';'):
            executable=format(opcode*2+1,'x')+code[1].strip(';')
        else:
            executable=format(opcode*2,'x')+code[1]
            
        
    elif opcode==0:
        executable=str(opcode*2+register[code[1].upper()])+format(int(code[2]),'x')
    elif opcode==5 or opcode==6:
        executable=format(opcode*2,'x')+code[1]
    else:
        executable=format(opcode*2,'x')+'00'
    return executable

       
def main():

    print('WARNING\n**addres must be hexadecimal and intermediate must be integer'+\
              '\n**if indirect addressing only for  load and store enter semicolon at end of address field'+\
              '\n**separate instructions with newline\n\n')
        
    print('please enter your input filename if necessary specify path with /')
    filename=input('filename: ')
        
    print('please enter your destination filename if necessary specify path with /')
    destination=input('filename: ')
        
    try:
        word=open(filename,'r')
        name=assemble(word.read())
        hex=open(destination,'w')
        hex.write('v2.0 raw\n')
        for i in name:
            hex.write(i+'\n')
            hex.close()
    except:
        print('file not found or specify the path correctly')
        main()

       
main()
