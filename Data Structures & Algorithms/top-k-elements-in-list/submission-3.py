class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            if num not in my_dict:
                my_dict[num]=1
            else:
                my_dict[num]+=1
        for num, count in my_dict.items():
            buckets[count].append(num)
        
        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

# Time >> O(n)
# Space >> O(n)