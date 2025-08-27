class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        last=0
        sep=s.split(" ")
        for i in sep:
            if i.isdigit():
                if last>=int(i):
                    return False
                else:
                    last=int(i)
        return True