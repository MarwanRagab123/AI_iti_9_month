num=int(input("Please Enter Your Number:"))

for i in range(num):
    for j in range(num*num):
        if num==i:
            j+=num
        print("*",end=" ")
    print()