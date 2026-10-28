class Solution(object):
    def groupAnagrams(self, strs):

        letter_map = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19, 'u':20,'v':21,'w':22,'x':23, 'y':24, 'z':25}

        overall_dict = {}

        output = []
        for i in strs:
            letters = [0]*26
            for j in i:
                letters[letter_map[j]] += 1
            
            new_letters = tuple(letters)
            if new_letters not in overall_dict:
                output.append([i])
                overall_dict[new_letters] = len(output)-1 
            else:
                output[overall_dict[new_letters]].append(i)
            

        return output 
            
        



        
