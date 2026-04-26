class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we want every key has a list as value
        groups = defaultdict(list)
        for s in strs:
            # for every word we create a letter counter
            count = [0] * 26

            for char in s:
                # by using ASCII order with ord() we find count per letter
                count[ord(char) - ord('a')] += 1
            
            #lists cannot be a key 
            groups[tuple(count)].append(s)

        return list(groups.values())

