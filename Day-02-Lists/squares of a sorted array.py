class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[]
        for num in nums:
            n=num*num
            ans.append(n)
        ans=sorted(ans)
        return ans
