def Valid_Parentheses(s:str):
    
    stack=[]
    dic={")":"(","}":"{","]":"["}

  

    for i in s:
        if i in "({[":
            stack.append(i)
        else:
            if  not stack or stack[-1]!=dic[i]:
                return False
            
            stack.pop()
        
    if( not stack):
        return True
    else:
        return False
    

print(Valid_Parentheses("[["))
        