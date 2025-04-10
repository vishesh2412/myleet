class Solution(object):
    def decodeString(self, s):
        stack=[]
        num=0
        output=''
        for i in s:
            if i.isdigit():
                num=num*10+int(i)
            elif i=='[':
                stack.append((num,output))
                num=0
                output=''
            elif i==']':
                new,add=stack.pop()
                output=add+(new*output)
            else:
                output+=i
        return output