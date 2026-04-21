class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters_s = set(s)
        letters_t = set(t)
        if letters_s != letters_t:
            return False

        else:
            s_counts = []
            for i in letters_s:
                s_counts.append(s.count(i))

            t_counts = []
            for i in letters_t:
                t_counts.append(t.count(i))

            s_dic = dict(zip([i for i in letters_s], s_counts))
            t_dic = dict(zip([i for i in letters_t], t_counts))

            return s_dic == t_dic
        
        """
        if len(s) != len(t):
            return False
        
        s_dic, t_dic = {}, {}

        for i in range(len(s)):
            s_dic[s[i]] = s_dic.get(s[i], 0) + 1 
            t_dic[t[i]] = t_dic.get(t[i], 0) + 1
        
        return s_dic == t_dic 
        """
                
