import json
def view_projects(user_id):
    try:
        with open("projects.jsonl", "r") as file:
            projects=[json.loads(line) for line in file]
            projects = [p for p in projects if p["user_id"] == user_id]
            if not projects:
                print("No projects found for this user.")
                return
            for project in projects:
                print(f"Project ID: {project['project_id']}")
                print(f"Title: {project['project_title']}")
                print(f"Details: {project['project_details']}")
                print(f"Target Amount: {project['project_target']}")
                print("-" * 20)
    except FileNotFoundError:
        print("No projects found.")