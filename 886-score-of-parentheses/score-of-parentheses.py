class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score=0
        stack=[0]
        for i in s:
            if i=='(':
                stack.append(0)
            else:
                last=stack.pop()
                if last==0:
                    stack[-1]+=1
                else:
                    stack[-1]+=2*last
        return stack[-1]