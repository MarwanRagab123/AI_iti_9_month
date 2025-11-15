def lengthOfLongestSubstring(s):
    max_len=0
    left=0
    dic={}
    for right,ch in enumerate(s):
        if ch in dic and dic[ch]>=left:
            left=dic[ch]+1
        
        dic[ch]=right
        max_len=max(max_len,right-left+1)
    return max_len

print(lengthOfLongestSubstring("abcabcbb"))

            