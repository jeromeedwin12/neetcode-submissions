class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_lookup = set(nums)
        best = 0
        for num in nums_lookup:
            if num-1 not in nums_lookup:
                count = 1
                current = num

                while(current+1 in nums_lookup):
                    current +=1
                    count +=1
                    
                best = max(best,count)
        return best      

# Time: O(n) - each number is visited at most once across all while loops
# Space: O(n) - set of all numbers