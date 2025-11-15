num = input("Please Enter Your Number: ")

ll=[]
if not num.isdigit():
    print("Invalid Input! Please Try Again")
else:
    num = int(num)
    for i in range(1, num + 1):#1---->2
        ln = []
        for j in range(1, i + 1):#1---->2
            s=i*j
            ln.append(s)#[1]
        ll.append(ln)
    print(ll)

