class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0

        letter_tracker = {}
        local_max = 0
        total_max = 0
        for right in range(len(s)):
            if s[right] not in letter_tracker:
                letter_tracker[s[right]] = 1
            else:
                letter_tracker[s[right]] += 1
            
            local_max += 1
            
            while letter_tracker[s[right]] > 1:
                letter_tracker[s[left]] -= 1
                left += 1
                local_max -= 1

            total_max = max(local_max, total_max)

        
        return total_max
