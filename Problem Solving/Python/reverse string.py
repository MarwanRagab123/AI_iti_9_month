def rev(ls):
    left,right=0,len(ls)-1

    while right>left:
        ls[left],ls[right]=ls[right],ls[left]
        left+=1
        right-=1

    return ls

s = ["h","e","l","l","o"]
print(rev(s))