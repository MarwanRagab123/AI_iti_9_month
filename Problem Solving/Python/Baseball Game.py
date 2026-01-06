
def  baseball_game(opertions):
    list_ops=[]
    for i in range(len(opertions)):
        if opertions[i].lstrip('-').isdigit():
            list_ops.append(int(opertions[i]))
            print(list_ops)
        elif opertions[i]=="C" :
            if list_ops:
                list_ops.pop()

        elif opertions[i]=="+":
            if len(list_ops)>=2:
                new_mem=sum(list_ops[-2:])
                list_ops.append(new_mem)
        elif opertions[i]=="D":
            list_ops.append(list_ops[-1]*2)

    return sum(list_ops)



ops=["1","D","D","D"]

print(baseball_game(ops))
