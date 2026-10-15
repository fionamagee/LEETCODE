class Solution(object):
    def maxArea(self, height):

        left = 0
        right = len(height)-1

        area = 0

        if len(height) == 2:
            return min(height[right], height[left])

        for i in range(len(height)):
            width = (right - left) 
            length = min(height[right], height[left])
            
            if width*length > area:
                area = width*length 
            
            if height[right]< height[left]:
                right -= 1
            else:
                left += 1
        


        
        return area
            




