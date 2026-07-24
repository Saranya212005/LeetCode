class Solution:
    def isValid(self, s: str) -> bool:
        is_valid=True
        stack=[]
        for i in s:
            if i in '{[(':
                stack.append(i)
            else:
                if len(stack)!=0:
                    if  ((stack[-1]=='{')and i=='}') or ((stack[-1]=='[')and i==']') or ((stack[-1]=='(')and i==')'):
                        stack.pop()
                    else:
                        is_valid=False
                        break
                else:
                    is_valid=False
                    break
        if len(stack)!=0:
            is_valid=False
        return is_valid
            