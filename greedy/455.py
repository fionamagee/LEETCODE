class Solution(object):
    def findContentChildren(self, g, s):
        #sort by smallest 
        g.sort(reverse=True)
        s.sort(reverse=True)

        #check if it can be eaten if it can count +=1 
        count = 0
        i = len(g)-1
        while s and i >= 0:
            if s[-1] >= g[i]:
                count += 1
                i -= 1
            
            s.pop()
        return count 
