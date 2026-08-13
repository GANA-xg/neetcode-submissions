class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mem=[]
        for i in range(len(nums)):
            if nums[i] not in mem:
                mem.append(nums[i])
            else:
                return True
        return False