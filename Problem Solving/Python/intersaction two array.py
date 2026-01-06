def intersaction(ls1,ls2):
    p=[]
    for i in ls1:
        if i in ls2:
            p.append(i)
    return list(set(p))


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(intersaction(nums1,nums2))
