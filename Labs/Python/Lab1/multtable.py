num = input("Please Enter Your Number: ")
ln=""
if not num.isdigit():
    print("Invalid Input! Please Try Again")
else:
    num = int(num)
    for i in range(1, num + 1):

        for j in range(1, i + 1):
            ln+=str(i * j)+" "

    print(ln)

