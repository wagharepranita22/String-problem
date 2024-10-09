# counting the vowels
string =input("Enter your string :")
count_vowel=0
count_consonent=0
for i in string:
    if i in "aeiouAEIOU":
        count_vowel+=1
    else:
        count_consonent+=1

print(f"Vowel = {count_vowel}")
print(f"consonent = {count_consonent}")