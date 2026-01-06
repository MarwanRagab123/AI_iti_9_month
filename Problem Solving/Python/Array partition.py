def array_partion(ls):

    check_ls=0
    ls2=sorted(ls)
    print(ls2)
#0 ,2 2 4
    for i in range(0,len(ls2),2):
        check_ls+=ls2[i]

    return check_ls

ls=[6,2,6,5,1,2]
print(array_partion(ls))