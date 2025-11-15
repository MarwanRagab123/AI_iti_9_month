def max_sub_arr(ls):
    curr_sum=ls[0]
    max_sum=ls[0]

    for i in range(1,len(ls)):
        curr_sum=max(ls[i],curr_sum+ls[i])
        max_sum=max(max_sum,curr_sum)
    
    return max_sum

nums =[5,4,-1,7,8]
print(max_sub_arr(nums))