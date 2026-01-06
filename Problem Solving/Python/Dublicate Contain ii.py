# def dublicate_ii(nums,k):
#     for i in range(len(nums)):
#
#         for j in range(i+1,len(nums)):
#
#             if abs(i-j)<=k and nums[i]==nums[j]:
#
#                 print(f"{i,j} nums {nums[i],nums[j]}")
#
#     return False

#this solution has a time limit problem


class Solution:
    def containsNearbyDuplicate_optimized(self, nums: list[int], k: int) -> bool:

        last_index = {}

        for i, num in enumerate(nums):

            if num in last_index:

                previous_i = last_index[num]
                distance = i - previous_i

                if distance <= k:
                    return True

            last_index[num] = i

        return False


ls=[1,2,3,1]
print(dublicate_ii(ls,3))