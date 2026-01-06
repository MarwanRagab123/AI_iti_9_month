# def missing_val(ls):
#     ls=sorted(ls)
#     n=len(ls)
#     for i in range(len(ls)):
#         if i not in ls:
#             return i
#     return n

def missing_val(nums):
    n = len(nums)
    total = n * (n + 1) // 2
    return total - sum(nums)

l=[0,1,2]

print(missing_val(l))