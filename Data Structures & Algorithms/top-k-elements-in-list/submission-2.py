class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        l=[]
        for i in nums:
            if i in freq:
                freq[i]+= 1
            else:
                freq[i]=1
        ordered = sorted(freq,key = lambda x:freq[x], reverse =True )
        for k in range(0,k):
            l.append(ordered[k])
        return l