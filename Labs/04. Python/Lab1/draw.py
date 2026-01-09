num=input("Please Enter Your Number:")

if not num.isdigit():
    print("Invalid Input! Please Try Again")
else:
    line = ""
    num=int(num)
    for i in range(num+1):
        for j in range(num+1):
            if j >= num - i + 1:
                line += '*'
            else :
                line += ' '
        line += '\n'
    print(line)


