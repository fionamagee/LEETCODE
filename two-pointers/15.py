class Solution(object):
    def threeSum(self, nums):
        nums.sort()

        length = len(nums)
        output = []

        set_check = set()
        for i in range(length):
            left = i + 1
            right = length -1
            for j in range(i+1,length-1):
                sum3 = nums[i] + nums[left] + nums[right]
                sum3_tup = tuple([nums[i], nums[left], nums[right]])
                if sum3 == 0 and sum3_tup not in set_check:
                    output.append([nums[i], nums[left], nums[right]])
                    set_check.add(sum3_tup)

                if sum3 < 0:
                    left += 1
                else:
                    right -= 1
        
        return output 




        