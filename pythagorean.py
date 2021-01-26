print("side_1\tside_2\thypotenuse")
for hypotenuse in range(1,20):
    for side_1 in range(1,20):
        for side_2 in range(1,20):
            if hypotenuse**2==side_1**2+side_2**2:
                print(side_1,side_2,hypotenuse,sep='\t')
    
