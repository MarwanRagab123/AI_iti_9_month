def revers(ls):
    ls1 = list(reversed(ls))
    ls2 = sorted(ls)
    return ls1, ls2


ls = []
for i in range(5):
    i = input(f"Please Enter number {i+1}:")
    ls.append(i)
ls1,ls2=revers(ls)

print("Sort Asc :",ls2)
print("Sort dsc :",ls1)
