def Container_Water(ls):
    max_areea=0
    left=0
    right=len(ls)-1

    while left<right:
        st=right-left # 1 -7 =6
        ht=min(ls[left],ls[right]) # min(1,7)=1
        max_areea=max(max_areea,st*ht) # max(0,6*1)=6
        if ls[left]<ls[right]: #1<7
            left+=1 
        else:
            right-=1

    return max_areea

print(Container_Water([1,1]))  # Output: 49