class Solution(object):
    def topKFrequent(self, nums, k):

        count = {}
        
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        

        boxes = []
        for box in range(len(nums)+1):
            boxes.append([])

        for key,value in count.items():
            boxes[value].append(key)
        

        output = []

        i = len(boxes) -1

        while i >= 0 and k > 0:

            for j in range(len(boxes[i])):
                output.append(boxes[i][j])
                k-= 1
            
            i -= 1




        return output


        
