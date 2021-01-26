def number(bus_stops):
    sum=0;
    for i in range(len(bus_stops)):
        sum+=bus_stops[i][0]-bus_stops[i][1]
    return sum    
   
print(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]))       
def is_leap(year):
    leap = False
    if (year%4==0 and year%100!=0):
        leap=True
    if (year%400==0 and year%100==0):
        leap=True
    return leap   

print(is_leap(2007))        
