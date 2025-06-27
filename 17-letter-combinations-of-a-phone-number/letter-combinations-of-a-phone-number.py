class Solution(object):
    def letterCombinations(self, digits):
        dict1={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        result=[]

        if not digits:
            return result

        def backtrack(index,solution):
            if index==len(digits):
                result.append(solution)
                return 
            
            letters=dict1[digits[index]]
            for i in letters:
                backtrack(index+1,solution+i)

        backtrack(0,'')
        return result