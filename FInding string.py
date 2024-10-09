
# FInding sub string
string = input("Enter your string :")
string1 = input("Enter your second string :")
# if string1 in string:
#     print("Substring is found")
# else:k
#     print("Substring is not found")


# 2 find index
# index =string.find(string1)
# if index != -1:
#     print(f"Substring have been found the index is {index}")
# else:
#     print("Not found")

# 3 Using Regular Expressions (Regex)
import  re
if re.search(string1,string):
    print("Found the sub string")
else:
    print("Not found the substring")