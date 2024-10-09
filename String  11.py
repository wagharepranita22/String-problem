# Pallindrome
string = input("GIve your string  :")
copy=string
sum=""
for i in range(len(string),0,-1):
    sum+=string[i-1]
print(sum)
if sum == copy :
    print("String is pallindrome")
else:
    print("String is not pallindrome")