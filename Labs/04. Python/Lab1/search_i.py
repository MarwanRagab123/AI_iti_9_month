str1=input("Enter String of You :")
if str1 =="" or str1.isdigit():
    print("Invalid String! Please Try Again")
else:
    str1=str1.lower()
    count=0
    for char in str1:
        if char=="i":
            print(count)
        count += 1
        print("")