#Python program to check whether the string is Symmetrical or Palindrome
str = input("Enter your string :")
copy=str
reversed=""
for i in range (len(str),0,-1):
    reversed+=str[i-1]
print(reversed)
if reversed == copy:
    print("""The entered string is symmetrical,\nThe entered string is palindrome""")

else:
    print("""The entered string is not symmetrical,\nThe entered string is not palindrome""")
