x=int(input("X="))
y=int(input("y="))
z=int(input("z="))
if(x%2!=0):
    print("x is Odd")
if(y%2!=0):
    print("y is Odd")
if(z%2!=0):
    print("z is Odd")
if(x%2!=0 and y%2!=0 and z%2!=0 ):
   if(x>y and x>z):
      print("x is the greatest of all")
   elif(y>x and y>z):
      print("y is the greatest")
   else :
      print("z is largest")
elif(x%2!=0 and y%2!=0):
     if(x>y):
      print("x is the greater than y") 
     else :
      print("y is greater than x")
elif(x%2!=0 and z%2!=0):
     if(x>z):
      print("x is the greater than z") 
     else :
      print("z is greater than x")
elif(y%2!=0 and z%2!=0):
     if(y>z):
      print("y is the greater than z") 
     else :
      print("z is greater than y") 