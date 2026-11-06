class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict={}
        if len(s)!= len(t):
            return False
        for ind in range(len(s)):
            if s[ind] in my_dict:
                my_dict[s[ind]]+=1
            else:
                my_dict[s[ind]]=1

            if t[ind] in my_dict:
                my_dict[t[ind]]-=1
            else:
                my_dict[t[ind]]=-1
        
        if(all(x==0 for x in my_dict.values())):
            return True
        else:
            return False