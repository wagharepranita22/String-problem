#  WAP to input a string and print the frequency of the characters.
str = input("Enter your string : ")
a=0
b=0
c=0
y=0

for i in str:
    if i == "a" :
        a += 1
    elif i == "b" :
        b += 1
    elif i == "c" :
        c += 1
    elif i == "y":
        y += 1
print(f"a = {a}\nb = {b} \nc = {c} \ny = {y}")
