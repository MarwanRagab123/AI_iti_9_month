def search_for_number(ls1 , ls2):
    tr=[]

    for i in range(len(ls2)):
        last = -1
        for j in range(len(ls1)):
            if ls2[i]==ls1[j]:
                last=j
        tr.append(last)

    return tr

ls=[1,2,7,3,7]
ls2=[7,9,2]
print(search_for_number(ls,ls2))