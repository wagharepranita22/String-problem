# Write a program to create a new string made of an input string’s first, middle, and last character.
str1 = input("Enter your first name :")

res=str1[0]

# middel string
l=len(str)
mi = int(l/2)

# last
res+=str1[mi]

res+=str[l-1]
print(res)