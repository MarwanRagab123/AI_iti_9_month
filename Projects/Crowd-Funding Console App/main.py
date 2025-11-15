from Authentication_System.Registration import register_user
from Authentication_System.Login import login_user
from Projects_Details.add_projects import add_project
from Projects_Details.delete_project import delete_project
from Projects_Details.View_projects import view_projects
from tabulate import tabulate
from helper.shape import show_banner
import msvcrt

user_id_global = None

if __name__ == "__main__":
   
    show_banner()
    while True:
        print("\n=== Main Menu ===")
            
        choice = input("1) if you have an account, Login \n"
                "2) if you don't have an account, Register \n" \
                "3) Exit The Program \n"
                "Enter your choice (1, 2 or 3): ")

        # ================== Register ===================
        if choice == "1":
            print("\n--- Register ---")
            print(register_user())
            continue

        # ================== Login ===================
        elif choice == "2":
            print("\n--- Login ---")
            user_id = login_user()
            if not user_id:
                print("Login failed.")
                continue

            user_id_global = user_id
            print(f"Welcome {user_id_global}!")

       

        
            
            # ========== Project Menu ==========
            while True:
                print("\n=== Projects Menu ===")
                views = input(
                    "Choose an action:\n"
                    "1) Add Project\n"
                    "2) Display Projects\n"
                    "3) Delete Project\n"
                    "4) Logout\n"
                    "Enter your choice: "
                )

                # ----- Add Project -----
                if views == "1":
                    print("\n--- Add Project ---")
                    add_project(user_id_global)

                # ----- Display Projects -----
                elif views == "2":
                    print("\n--- Your Projects ---")
                    view_projects(user_id_global)

                # ----- Delete Project -----
                elif views == "3":
                    print("\n--- Delete Project ---")
                    project_id = input("Enter project ID to delete (e.g., p0): ")
                    print(delete_project(user_id_global, project_id))

                    print("\n--- Your Projects ---")
                    view_projects(user_id_global)

                # ----- Logout -----
                elif views == "4":
                    print("Logging out...")
                    break

                else:
                    print("Invalid choice.")
        elif choice=="3":
            print("Thank you To Use The Program \n")
            break
        else:
            print("Invalid Choice! Enter your choice (1, 2 or 3)")