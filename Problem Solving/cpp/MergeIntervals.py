def merge(ls):
    ls.sort(key=lambda i :i[0])
    merged=[]

    for i in ls:
        if not merged or merged[-1][1]<i[0]:
            merged.append(i)
        else:
            merged[-1][1]=max(merged[-1][1],i[1])
    return merged

print(merge([[1,3],[2,6],[8,10],[15,18]]))

