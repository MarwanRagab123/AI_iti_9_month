from Validate.validate_email import validate_email
from Validate.validate_name import validate_name
from Validate.validate_mobileEgy import validate_mobile_egy
from Validate.validate_passwd import validate_password, confirm_password
import json



def get_last_count():
    try:
        with open("users.jsonl", "r") as f:
            lines = f.readlines()
            if not lines:
                return -1  
            last = json.loads(lines[-1])
            last_id = last["user_id"]  # e.g. "user4"
            number = int(last_id.replace("user", ""))  # extract 4
            return number
    except FileNotFoundError:
        return -1  # if file doesn't exist yet


#validate ech step  in regester such email not valid repeat email using while loop
def register_user():
    while True:
        Fname = input("Enter your First name: ")
        if not validate_name(Fname):
            print("Invalid name. Name must contain only letters and spaces, and be at least 2 characters long.")
            continue
        else:
            break
    while True:
        Lname = input("Enter your Last name: ")
        if not validate_name(Lname):
            print("Invalid name. Name must contain only letters and spaces, and be at least 2 characters long.")
            continue
        else:
            break
    while True:
        email = input("Enter your email: ")
        if not validate_email(email):
            print("Invalid email format.")
            continue
        else:
            break
    while True:
        mobile = input("Enter your mobile number: ")
        if not validate_mobile_egy(mobile):
            print("Invalid Egyptian mobile number.")
            continue
        else:
            break
    while True:
        password = input("Enter your password: ")
        if not validate_password(password):
            print("Invalid password. Password must be at least 8 characters long and include uppercase, lowercase, digit, and special character.")
            continue
        else:
            break
    while True:
        confirm = input("Confirm your password: ")
        if not confirm_password(password, confirm):
            print("Passwords do not match.")
            continue
        else:
            break
    

    if not validate_name(Fname) or not validate_name(Lname):
        return "Invalid name. Name must contain only letters and spaces, and be at least 2 characters long."
    
    if not validate_email(email):
        return "Invalid email format."
    
    if not validate_mobile_egy(mobile):
        return "Invalid Egyptian mobile number."
    
    if not validate_password(password):
        return "Invalid password. Password must be at least 8 characters long and include uppercase, lowercase, digit, and special character."
    
    if not confirm_password(password, confirm):
        return "Passwords do not match."
    
    last_count = get_last_count()
    user_id = f"user{last_count + 1}"

    user_data={
        "user_id": user_id,
        "Fname": Fname,
        "Lname": Lname,
        "email": email,
        "mobile": mobile,
        "password": password
    }
    with open("users.jsonl", "a") as file:
        file.write(json.dumps(user_data) + "\n")
    return "Registration successful!"