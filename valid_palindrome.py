class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=""
        for ch in s:
            if ch.isalpha() or ch.isnumeric():
                ans+=ch
        ans=ans.lower()
        a=ans
        if a==ans[::-1]:
            return True
        else:
            return False
