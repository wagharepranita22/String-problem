# taking input from user as string
# string = input("Enter your String :")
#
# # using the len method
# l=len(string)
# print(l)
#
# # assessing  the string using index
# print(string[::-1])
#
# # conctination of string
# string1=input("Give your second String :")
# string3=string+string1
# print(string3)
# # Changing Case
# print(string3.lower())
# print(string3.upper())
# print(string3.capitalize())
# print(string3.count("a"))
#
#
# # Replacing Substrings:
# print(string.replace("prani","proop"))
#
#
# # Finding Substrings:
# print(string.find("ra"))
# print(string3.index("santo"))


# FInding sub string
string = input("Enter your string :")
string1 = input("Enter your second string :")
if string1 in string:
    print("Substring is found")
else:
    print("Substring is not found")