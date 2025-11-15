def move_zero(ls):

    left=0
    for r in range(len(ls)):
        if(ls[r]!=0):
            ls[left],ls[r]=ls[r],ls[left]
            left+=1
    
    return ls

nums = [0,1,0,3,12]
print(move_zero(nums))