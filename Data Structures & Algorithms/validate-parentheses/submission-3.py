class Solution:
    def isValid(self, s: str) -> bool:
        valid=True
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
                    valid = False
                    break
                if stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    valid = False
                    break
    
        if valid and len(stack)==0:
            return True
        else:
            return False
