import json
def delete_project(user_id,project_id):
    try:
        with open("projects.jsonl","r")as file:
            projects=[json.loads(line) for line in file]
        projects = [p for p in projects if not (p["user_id"] == user_id and p["project_id"] == project_id)]
        with open("projects.jsonl", "w") as file:
            for project in projects:
                file.write(json.dumps(project) + "\n")
        print("Project deleted successfully.")
    except FileNotFoundError:
        print("No projects found.")