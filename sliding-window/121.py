class Solution(object):
    def maxProfit(self, prices):
        local_min = float('inf')
        highest_diff = 0
        for right in prices:
            if right < local_min:
                local_min = right 
            
            highest_diff = max(highest_diff,right-local_min)
            
        return highest_diff


        
