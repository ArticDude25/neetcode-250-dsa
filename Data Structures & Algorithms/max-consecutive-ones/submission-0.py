class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currcount=0
        prevcount=0
        for i in nums:
            if(i==1):
                currcount=currcount+1
                
            else:
                prevcount=max(currcount,prevcount)
                currcount=0
                
                
               
        return max(currcount,prevcount)            
        