ch = input("Enter any character : ")
if ch[0].isalpha() :
    print("\n" + ch[0], "is A ALPHABET.")
elif ch[0].isdigit() :
    print("\n" + ch[0], "is A DIGIT.")
else :
    print("\n" + ch[0], "is A SPECIAL CHARACTER.")