import json

def get_last_project_count(user_id):
    try:
        with open("projects.jsonl", "r") as f:
            projects = [json.loads(line) for line in f]

        user_projects = [p for p in projects if p["user_id"] == user_id]

        if not user_projects:
            return -1
        
        max_id = max(int(p["project_id"].replace("p", "")) for p in user_projects)
        return max_id
    except FileNotFoundError:
        return -1

def add_project(user_id):
    last=get_last_project_count(user_id=user_id)
    new_id = last + 1
    project_id = f"p{new_id}"
    
    title = input("Enter the project title: ")
    details = input("Enter the project details: ")
    target = input("Enter the project target amount: ")
    project_data = {
        "user_id":user_id,
        "project_id":project_id,
        "project_title": title,
        "project_details": details,
        "project_target": target
    }

    with open("projects.jsonl", "a") as file:
        file.write(json.dumps(project_data) + "\n")
    print("Project added successfully!")
    

# def view_projects(user_id):
#     try:
#         with open("projects.jsonl", "r") as file:
#             projects=[json.loads(line) for line in file]
#             projects = [p for p in projects if p["user_id"] == user_id]
#             if not projects:
#                 print("No projects found for this user.")
#                 return
#             for project in projects:
#                 print(f"Project ID: {project['project_id']}")
#                 print(f"Title: {project['project_title']}")
#                 print(f"Details: {project['project_details']}")
#                 print(f"Target Amount: {project['project_target']}")
#                 print("-" * 20)
#     except FileNotFoundError:
#         print("No projects found.")



# def delete_project(user_id, project_id):
#     try:
#         with open("projects.jsonl", "r") as file:
#            projects=[json.loads(line) for line in file]
#         projects = [p for p in projects if not (p["user_id"] == user_id and p["project_id"] == project_id)]


#         with open("projects.jsonl", "w") as file:
#             for project in projects:
#                 file.write(json.dumps(project) + "\n")
#         print("Project deleted successfully.")
#     except FileNotFoundError:
#         print("No projects found.")
           