str1=input("Enter String of You :")
if str1 =="" or str1.isdigit():
    print("Invalid String! Please Try Again")
else:
    str1=str1.lower()
    str1=str1.split()
    print(str1.count("iti"))