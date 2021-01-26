import re
def main():
    file=open('program.cs','r')
    line=file.readline().strip("ï»¿")
    lexems=[]
    i=1
    print("Line","Tokens","Type",sep='\t\t\t')
    while(line!=''):
        line=line.split("//")[0]
        line=line.split(";")[0]
        tokenize(line,i)
        line=file.readline()
        i=i+1
def tokenize(line,lineNumber):
    x=re.compile(r'\+|\-|\*|/|=')
    y=line
    z=x.findall(y)
    for i in z:
        print(lineNumber,i,"Operator",sep='\t\t\t')
    x=re.compile(r'\b(?!using\b)\b(?!namespace\b)\b(?!class\b)\b(?!static\b)\b(?!void\b)\b(?!Console\b)\b(?!int\b)\b(?!float\b)\b(?!char\b)\b(?!String\b)\b(?!WriteLine\b)([a-zA-Z](\w)*)|(_(\w)+)$')
    z=x.findall(y)
    for i in z:
            print(lineNumber,i[0],"identifier",sep='\t\t\t')
    x=re.compile(r'(\d)+$')
    z=x.findall(y)
    for i in z:
        print(lineNumber,i,"integer literal",sep='\t\t\t')
    x=re.compile(r'[(){}.]')
    z=x.findall(y)
    for i in z:
        print(lineNumber,i,"delimiter",sep='\t\t\t')
    x=re.compile(r'using|namespace|class|static|void|Console|int|float|char|String|WriteLine')
    z=x.findall(y)
    for i in z:
        print(lineNumber,i,"keyword",sep='\t\t\t')
    x=re.compile(r'''(?x)(?<!\\)".*?(?<!\\)"''',re.VERBOSE)
    z=x.findall(y)
    for i in z:
        print(lineNumber,i,"string literal",sep='\t\t\t')
    x=re.compile(r'''(?x)(?<!\\)'.?(?<!\\)' ''',re.VERBOSE)
    z=x.findall(y)
    for i in z:
        print(lineNumber,i,"character literal",sep='\t\t\t')
    x=re.compile(r'[0-9]+\.[0-9]+')
    z=x.findall(y)
    for i in z:
        print(lineNumber,i,"floating point literal",sep='\t\t\t')
main()

    
