class Solution(object):
    def lengthOfLongestSubstring(self, s):
        answer=[]
        final=0
        for i in s:
            if i in answer:
                answer = answer[answer.index(i) + 1:]
            answer.append(i)
            final=max(len(answer),final)
        return final