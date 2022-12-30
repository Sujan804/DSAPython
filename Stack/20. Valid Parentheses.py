from queue import LifoQueue


class Solution:
    def isValid(self, s: str) -> bool:
        stack =LifoQueue()
        
        left = 0
        while left<len(s):
            if s[left] == '(' or s[left] == '{' or s[left] == '[':
                stack.put(s[left])
                left += 1
            else:
                if(stack.empty()):
                    return False

                top = stack.get()

                if (s[left]==')' and top == '(') or (s[left]=='}' and top=='{') or (s[left]==']' and top =='['):
                    left += 1
                else :
                    return False
        if stack.empty():
            return True
        else:
            return False