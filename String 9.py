# count all digit special symbol and character
string = input("Give your String :")
digit=""
alpha=""
symbol=""
for i in string:
    if i.isdigit():
        digit+=i
    elif i.isalpha():
        alpha+=i
    else:
        symbol+=i
print(f"Digit = {digit}\nCharacter = {alpha}\nSymbol = {symbol}")