
import json
import os
def login_user(email=None, password=None, silent=False):
    if email is None:
        email = input("Enter your email: ")
    if password is None:
        password = input("Enter your password: ")
    if not os.path.exists("users.jsonl"):
        if not silent:
            print("No users registered yet.")
        return None
    try:
        with open("users.jsonl","r") as file:
            for line in file:
                user_data=json.loads(line)
                if user_data["email"]==email and user_data["password"]==password:
                    if not silent:
                        print("Login successful!")
                    return user_data["user_id"]
    except Exception as e:
        if not silent:
            print(f"An error occurred during login: {e}")
        return None
