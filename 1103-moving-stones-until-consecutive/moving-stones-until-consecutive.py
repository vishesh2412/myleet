class Solution(object):
    def numMovesStones(self, a, b, c):
        answer=[]
        new=sorted([a,b,c])
        if abs(new[0]-new[1])==1 and abs(new[1]-new[2])==1:
            answer.append(0)
        elif abs(new[0]-new[1])<=2 or abs(new[1]-new[2])<=2:
            answer.append(1)
        else:
            answer.append(2)
        
        answer.append(abs(new[0]-new[1])+abs(new[1]-new[2])-2)

        return answer