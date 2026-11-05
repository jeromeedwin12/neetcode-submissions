class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique=set()
        for val in nums:
            if val in unique:
                return True
            unique.add(val)
        return False
        