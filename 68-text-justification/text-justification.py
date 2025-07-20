class Solution(object):
    def fullJustify(self, words, maxWidth):
        reach=0
        string=[]
        answer=[]
        for i in words:
            if reach+len(i)+len(string)>maxWidth:
                extra=maxWidth-reach
                count=len(string)-1
                if count==0:
                    adding=string[0]+' '*extra
                else:
                    spaces=extra//count
                    left=extra%count
                    new_line=''
                    for j,word in enumerate(string[:-1]):
                        space_now=spaces+(1 if j<left else 0)
                        new_line+=(word+' '*space_now)
                    new_line+=string[-1]
                    adding=new_line
                answer.append(adding)
                reach=len(i)
                string=[i]
            else:
                string.append(i)
                reach+=len(i)
        last=' '.join(string)
        answer.append(last+' '*(maxWidth-len(last)))
        return answer