def max_sum(nums):
    def ma_max(num):
        return max(str(num))

    ms = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if ma_max(nums[i]) == ma_max(nums[j]):
                ms.append(nums[i] + nums[j])

    if not ms:
        return -1
    else:
        return max(ms)

ls=[112,131,411]

print(max_sum(ls))