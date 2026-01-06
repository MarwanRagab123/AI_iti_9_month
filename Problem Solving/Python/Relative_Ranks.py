def relative(ls):
    index=list(enumerate(ls))

    scored=sorted(index,key=lambda x:x[1],reverse=True)

    final_res=[""]*len(ls)
    for i,(original_index,val) in enumerate(scored):
        if i==0:
            final_res[original_index]="Gold Medal"
        elif i==1:
            final_res[original_index]="Silver Medal"
        elif i==2:
            final_res[original_index]="Bronze Medal"
        else:
            final_res[original_index]=f"{i+1}"

    return final_res

s=[10,3,8,9,4]

print(relative(s))