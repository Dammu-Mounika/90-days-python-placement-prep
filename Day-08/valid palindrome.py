class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=""
        for ch in s:
            if ch.isalnum():
                ans+=ch
        ans=ans.lower()
        left=0
        right=len(ans)-1
        while left<right:
            if ans[left]!=ans[right]:
                return False
                break
            left+=1
            right-=1
        else:
            return True
