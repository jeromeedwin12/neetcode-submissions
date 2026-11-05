class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        solutions=[]
        for ind,value in enumerate(nums):
            pair = target - value
            if pair in my_dict:
                solutions.append(my_dict[pair])
                solutions.append(ind)
            else:
                my_dict[value]=ind
        return solutions        