class Solution(object):
    def maxArea(self, height):
        #logic
        # i=left
        # j=right
        # i increase
        # j decrese
        # new_area> previous_area:
        #     previous_area=new_area

        i=0
        j=len(height)-1

        final_area=min(height[i],height[j])*(j-i)

        while(i<j):
            new_area=min(height[i],height[j])*(j-i)
            if new_area>final_area:
                final_area=new_area
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return final_area