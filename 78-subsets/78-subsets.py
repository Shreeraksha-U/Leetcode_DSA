class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[]
        n=len(nums)
        def solve(i,sequence):
            if i==n:
                res.append(sequence[:])
                return 0
            sequence.append(nums[i])
            take=solve(i+1,sequence)
            sequence.pop()
            skip=solve(i+1,sequence)
        solve(0,[])
        return res