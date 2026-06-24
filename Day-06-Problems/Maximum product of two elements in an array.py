class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        max1=nums[0]
        max2=nums[1]
        return (max1-1)*(max2-1)
