def reversed_string(text):
    return text[::-1]

text=input("Please Enter The text You Need Reverse: ")
if text =="" or text.isdigit():
    print("Invalid String! Please Try Again")
else:
    print(reversed_string(text))