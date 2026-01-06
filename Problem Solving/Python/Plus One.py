def plusOne( digits):
    for i in range(len(digits)-1,-1,-1):
        if digits[i]<9:
            digits[i]+=1
            return digits
        digits[i]=0 #[1,5,0]

    return [1]+digits


d=[1,5,9]
print(plusOne(d))