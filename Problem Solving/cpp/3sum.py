def three_sum(ls):
    ls.sort()
    res=[]

    for i in range(len(ls)):
        if i>0 and ls[i]==ls[i-1]:
            continue
        elif ls[i]>0:
            break

        left,right=i+1,len(ls)-1

        while left<right:
            curr_res=ls[i]+ls[left]+ls[right]
            if curr_res==0:
                res.append([ls[i],ls[left],ls[right]])
                left+=1
                right-=1
                while left<right and ls[left]==ls[left-1]:
                    left+=1
                while left<right and ls[right]==ls[right+1]:
                    right-=1
            elif curr_res<0:
                left+=1

            else:
                right-=1
    return res

ls=[-1,0,1,2,-1,-4]
print(three_sum(ls))