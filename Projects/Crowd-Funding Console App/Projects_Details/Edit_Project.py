import json

def edit_project(user_id,project_id):

    with open("projects.jsonl","r")as file:
        projects=[json.loads(line) for line in file]

        flag=None
    for idx,val in enumerate(projects):
        if val["user_id"]==user_id and val["project_id"]==project_id:
            flag=val
            break
    if not flag:
        print("No projects found for this user.")
        return

    print("this Project which to update it: ",flag)
    print("press Enter If don't Update")
    new_title=input("Enter The New Project Title: ").strip()
    new_details=input("Enter The New Project details: ").strip()
    new_target=input("Enter The New Project target: ").strip()

    if new_title:
        flag["project_title"]=new_title
    if new_details:
        flag["project_details"]=new_details
    if new_target:
        flag["project_target"]=new_target



    with open("projects.jsonl","w")as file:
        for line in projects:
            file.write(json.dumps(line)+ "\n")

    print("Project updated successfully!")



# Edit_file("user0","p2")
