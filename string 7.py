# reverser string in upper ,lower and copy in another string
string = input("Give your string  :")
copy=string
print("lower :",string.lower())
print("Upper : ",string.upper())
print("Copy string " ,copy)
sum=""
for i in range(len(string),0,-1):
    sum+=string[i-1]

print(f"Reversed = {sum}")