class Solution(object):
    def minElement(self, nums):
        def digitSum(num):
            tot=0
            while num>0:
                tot+=num%10
                num//=10
            return tot
        ans = float('inf')
        for num in nums:
            ans=min(ans,digitSum(num))
        return ans