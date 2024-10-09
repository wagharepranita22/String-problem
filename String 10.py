# count vowel
string = input( "Give your string :")
vowel = 0
const = 0
space= 0
for i in string:
    if i in "AIOUEaioue":
        vowel += 1
    elif i in " ":
        space +=1
    else:
        const += 1

print(f"Vowel = {vowel}\nSpace = {space}\nconstant = {const}")


