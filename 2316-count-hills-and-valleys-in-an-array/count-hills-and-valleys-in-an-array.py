class Solution(object):
    def countHillValley(self, nums):
        
        

        new=[nums[0]]
        for i in nums[1:]:
            if new[-1]!=i:
                new.append(i)

        if len(new)<3:
            return 0
        
        i=1
        count=0

        while(i<len(new)-1):
            if (new[i-1]<new[i] and new[i]>new[i+1]) or (new[i-1]>new[i] and new[i]<new[i+1]):
                count+=1
            
            i+=1

        return count