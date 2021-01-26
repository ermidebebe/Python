number_of_peaple=int(input("peaple="))
number_of_each=int(input("each="))

hot_dog_package=number_of_peaple*number_of_each//10+1
hot_dogbun_package=number_of_peaple*number_of_each//8+1
hot_leftover=10-number_of_peaple*number_of_each%10
bun_leftover=8-number_of_peaple*number_of_each%8

print("the minnimum Hot dogs required =",hot_dog_package)

print("the minnimum Hot dogs bun required =",hot_dogbun_package)

print("Hot dogs leftover=",hot_leftover)

print("Hot dogs buns leftover=",bun_leftover)
