def main():
    name=input('Name:')
    print('your encrypted name is '+encrypter(name))
def encrypter(name):
    letters_Ascii={'o':111,'U':85,'Q':81,'j':106,'P':80,'i':105,'O':79,'h':104,'N':78,
             'n':110,'T':84,chr(32):32,'m':109,'S':83 ,'l':108,'R':82,'k':107,
             'Z':90,'s':115,'Y':89,'r':114,'X':88 ,'q':113,'W':87,'p':112,'V':86,
             'y':121,'E':69,'w':119,'C':67,'v':118,'B':66,'u':117,'A':65,'t':116,
             'I':73,'x':120,'D':68,'b':98,'H':72,'a':97,'G':71,'z':122,'F':70,
             'g':103,'M':77,'e':101,'K':75,'d':100,'J':74,'f':102,'L':76,'c':99}
    letters_english={'A':1,'e':5,'r':18,'R':18,'m':13,'i':9,'E':5,'a':1,'y':25,'s':19,'D':4,'b':2,chr(32):32,'b':2,'B':2,'c':3
                     ,'d':4,'f':6,'g':7,'G':7,'H':8,'h':8,'P':16,'p':16,'O':17,'o':17,'T':20,'t':20,
                     'B':2,'N':14,'n':14,'i':9,'I':9}
    name2=''
    for i in range(len(name)):
        name2=name2+str(format(round(letters_Ascii[name[i]]/letters_english[name[i]]),'X'))
    return name2    
        
    
main()            
        
         
         
       
 
       
    
      
        
      
     
     

    
     
      
    
      
      
      
    
