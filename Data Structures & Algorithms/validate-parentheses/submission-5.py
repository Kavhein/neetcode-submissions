class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]
        pairs={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                    break
                if stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    return False
                    break
    
        return True if len(stack) == 0 else False
