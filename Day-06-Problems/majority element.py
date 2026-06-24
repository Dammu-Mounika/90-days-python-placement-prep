class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans={}
        for num in nums:
            ans[num]=ans.get(num,0)+1
        majority=max(ans.values())
        for num in ans:
            if ans[num]==majority:
                return num
