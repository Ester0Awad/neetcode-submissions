class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        bla = defaultdict(list)

        #count the strings in `str` list
        for s in strs:
            #making an empty list of 26 0s
            count = [0] * 26

            #count each char in every word (aks list of chars)
            for c in s:

                # take the Ascii value of the current char `c` and 
                # subtract it from `a` lowercase char value
                # increase the count by 1
                count[ord(c) - ord("a")] += 1

            bla[tuple(count)].append(s)

        return bla.values()


















               