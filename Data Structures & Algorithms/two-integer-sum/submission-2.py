class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        solutions=[]
        for ind,value in enumerate(nums):
            pair = target - value
            if pair in my_dict:
                return [my_dict[pair],ind]
            my_dict[value]=ind      