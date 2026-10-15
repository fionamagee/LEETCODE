class Solution(object):
    def characterReplacement(self, s, k):
        substring = {}
        left = 0

        max_curr = 0
        output = 0
        total = 0

        for char in s:
            if char not in substring:
                substring[char] = 1
            else:
                substring[char] += 1
            
            if substring[char] > max_curr:
                max_curr = substring[char]
            
            total += 1

            while total-max_curr> k:
                total -=1 
                substring[s[left]] -=1
                left+= 1
            output = max(output, total)
        
        return output

        