def isAnagram(str1, str2):

    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    if sorted(str1)==sorted(str2):
        return True
    else:
        return False