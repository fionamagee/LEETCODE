class Solution(object):
    def isAnagram(self, s, t):
        s_letters = {}
        t_letters = {}

        count = 0

        while count < max(len(s),len(t)):
            if count < len(t):
                if t[count] in t_letters:
                    t_letters[t[count]] += 1
                else:
                    t_letters[t[count]] = 1
            
            if count < len(s):
                if s[count] in s_letters:
                    s_letters[s[count]] += 1
                else:
                    s_letters[s[count]] = 1


            count += 1
        

        return s_letters == t_letters
        
