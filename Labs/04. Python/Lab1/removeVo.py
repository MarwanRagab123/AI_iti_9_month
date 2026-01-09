vowels="aeiou"
str1=input("Enter String of You :")
if str1 =="" or str1.isdigit():
    print("Invalid String! Please Try Again")
else:
    str1=str1.lower()
    for i in str1:
        if i in vowels:
            str1=str1.replace(i,"")
    print("New String After Removing vowels :",str1)
