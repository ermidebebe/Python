color_1=input("color1=")
color_2=input("color2=")
t=True
if color_1!='yellow' and color_1!='blue' and color_1!='red':
     t=False
if color_2!='yellow' and color_2!='blue' and color_2!='red':
     t=False
if t:
    if  color_1=='blue' and  color_2=='yellow' or color_2=='blue' and  color_1=='yellow':
        print("Green")
    if  color_1=='red' and  color_2=='yellow' or color_2=='red' and  color_1=='yellow' :
        print("Orange")
    if  color_1=='blue' and  color_2=='red'or color_2=='blue' and  color_1=='red':
        print("Purple")
else:
    print("please enter three basic colors")
    
  
