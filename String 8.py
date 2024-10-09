# arrange string character such that lower letter should come first in another string
string = input("Give your string ")
upper=""
lower=""
for i in string:
    if i.islower():
        lower+=i
    else:
        upper+=i

print(f"{lower}{upper}")
