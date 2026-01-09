ls=[]
while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    if not user_input.isdigit():
        print("Invalid Input! Please Try Again")
        continue
    else:
        ls.append(user_input)

print(ls)