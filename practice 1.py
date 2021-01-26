import re
x=re.compile(r'using|namespace|class|static|void|Console|int|float|char|String')
y=input("token:")
z=x.findall(y)
print(z)
print(y)
