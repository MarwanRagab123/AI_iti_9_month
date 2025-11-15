def containsDuplicate(ls):
   
   if(len(ls)!=len(set(ls))):
      return True
   return False

ls=[1,2,3,4,5,9,1]
print(containsDuplicate(ls))
    