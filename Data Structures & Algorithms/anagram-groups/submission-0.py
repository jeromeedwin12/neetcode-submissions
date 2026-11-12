class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for value in strs:
            i="".join(sorted(value))
            my_dict.setdefault(i,[]).append(value)
        return list(my_dict.values())