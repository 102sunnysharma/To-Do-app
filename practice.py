class Solution:
    def reverseWords(self, s: str) -> str:
        newstr = s.split()
        newstr.reverse()
        result = " ".join(newstr)
        return result

class Solution:
    def reverseWords(self, s: str) -> str:
        newstr = s.split()
        newstr.reverse()
        newstr = " ".join(newstr)
        return newstr