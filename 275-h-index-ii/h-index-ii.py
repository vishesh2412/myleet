class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations=sorted(citations,reverse=True)
        i=0
        while(i<len(citations) and citations[i]>i):
            i+=1
        return i