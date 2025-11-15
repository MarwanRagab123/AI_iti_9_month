def RemoveEl(ls:list,num:int):
    left=0
    
    for i in range(len(ls)):
        if ls[i]!=num:
            ls[left]==ls[i]
            left+=1
        
    return left
            

ls=[0,1,2,2,3,0,4,2]
print(RemoveEl(ls,2))