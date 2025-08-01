class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]

        answer=[[1]]
        i=2
        while(i<numRows+1):
            new=[1]*i
            prev=answer[-1]
            for j in range(1,i-1):
                new[j]=prev[j-1]+prev[j]
            answer.append(new)
            i+=1
        return answer