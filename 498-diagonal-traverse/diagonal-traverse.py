class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        i = j = 0
        result = []

        for _ in range(m * n):
            result.append(mat[i][j])

            if (i + j) % 2 == 0:  # moving up-right
                if j == n - 1:
                    i += 1
                elif i == 0:
                    j += 1
                else:
                    i -= 1
                    j += 1
            else:  # moving down-left
                if i == m - 1:
                    j += 1
                elif j == 0:
                    i += 1
                else:
                    i += 1
                    j -= 1

        return result
