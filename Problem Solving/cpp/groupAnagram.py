def groupAnagrams(list_of_strings):

    new={}
    for i in range(len(list_of_strings)):
        sorted_str=''.join(sorted(list_of_strings[i])) 
        if sorted_str in new:
            new[sorted_str].append(list_of_strings[i]) #new[aet]=[]
        else:
            new[sorted_str] = [list_of_strings[i]] # 
    return list(new.values())


       

ls=["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(ls))