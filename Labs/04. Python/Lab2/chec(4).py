text = input("Please Enter Your Name: ")
if text == "" or text.isdigit():
    print("Invalid String! Please Try Again")
else:
    email = input("Please Enter Your Email: ")
    email = email.split()
    for i in email:
        if "@" in i and "." in i:
            print(f"Your Name is {text} and Your Email is {i}")
        else:
            print("Invalid Email! Please Try Again")
