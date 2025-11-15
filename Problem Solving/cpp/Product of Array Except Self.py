def product_of_arr(ls):
    n=len(ls)
    p=[1]*n
    s=[1]*n
    print(n)
    for i in range(1,n):
        p[i]=p[i-1]*ls[i-1] #1*1=1  
    
    for i in range(n-2,-1,-1):
        s[i]=s[i+1]*ls[i+1] #1*1=1

    res=[]
    for i in range(n):
        res.append(p[i]*s[i])
    return res

ls=[1,2,3,4]
print(product_of_arr(ls))

