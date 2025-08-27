import re
class Solution:
    def checkString(self, s: str) -> bool:
        return bool(re.fullmatch(r'a*b*',s))