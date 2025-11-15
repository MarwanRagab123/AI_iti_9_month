def max_pair(ls):
    nums=[]
    max_n=max(ls)
    nums.append(max_n)
    ls.remove(max_n)

    j=0
    for i in range(len(ls)):
        if j<ls[i]:
            j=ls[i]
    nums.append(j)

    return sum(nums)

ls=[2, 15, 10, 3, 50]

print(max_pair(ls))
