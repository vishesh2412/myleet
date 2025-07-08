class Solution(object):
    def numMovesStones(self, a, b, c):
        new=sorted([a,b,c])
        if abs(new[0]-new[1])==1 and abs(new[1]-new[2])==1:
            answer1=0
        elif abs(new[0]-new[1])<=2 or abs(new[1]-new[2])<=2:
            answer1=1
        else:
            answer1=2
        
        answer2=abs(new[0]-new[1])+abs(new[1]-new[2])-2

        return [answer1,answer2]