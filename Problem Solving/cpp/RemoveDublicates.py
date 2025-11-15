def RemoveDublicates(nums):
    n=len(nums)

    lf=0

    for r in range(1,len(nums)):
        if(nums[r]!=nums[lf]): #0==0
            lf+=1
            nums[lf]=nums[r]
    #for i in range(lf+1,n):
    # nums[i]="_"
    return lf+1,nums

ls=[0,0,1,1,1,2,2,3,3,4] #
print(RemoveDublicates(ls))