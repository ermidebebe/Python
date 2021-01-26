print("kph\tmph\n-------------")
for kph in range(60,140,10):
    mph=kph*0.6214
    print(kph,format(mph,'.2f'),sep='\t')
