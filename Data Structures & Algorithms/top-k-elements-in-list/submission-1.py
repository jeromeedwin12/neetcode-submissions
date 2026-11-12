class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            if num not in my_dict:
                my_dict[num]=1
            else:
                my_dict[num]+=1
        return [pair[0] for pair in sorted(my_dict.items(), key=lambda pair: pair[1], reverse=True)[:k]]
        