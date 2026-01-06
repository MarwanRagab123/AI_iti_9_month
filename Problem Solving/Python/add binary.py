def addbinary(a, b):
    carry=0
    result=[]
    i=len(a)-1
    j=len(b)-1
    while i>=0 or j>=0 or carry:
        sum=carry
        if i>=0:
            sum+=int(a[i])
            i-=1
        if j>=0:
            sum+=int(b[j])
            j-=1
        carry=sum//2
        result.append(str(sum%2))
    return ''.join(reversed(result))

if __name__ == "__main__":
    a = "1010"
    b = "1011"
    print(addbinary(a, b))  # Output: "10101"
