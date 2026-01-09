vowels="aeiou"

str1=input("Enter String :")
if str1 =="":
    print("String Is Empty")
else:
    count=0
    str1=str1.lower()
    for char in str1:
        if char in vowels:
            count+=1
    print("The Number vowels in string: ",count)