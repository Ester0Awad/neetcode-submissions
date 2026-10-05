class Solution:

    def encode(self, strs: List[str]) -> str:
        # Handle edge case where the input string is empty
        if not strs:
            return ""

        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s
        return result    


    def decode(self, s: str) -> List[str]:
        # Handle edge case where the input string is empty
        if not s:  # If s is empty or None
           return []

        # i is a poniter
        # a list `result`
        result, i = [], 0

        # each iteration will read 1 entire word
        while i < len(s):
            j = i

            # still in the integer character aka `5` in `5#co#de`
            while s[j] != "#":
                j += 1

            # tells us how many following characters we have to read
            length = int(s[i:j])  

            # `j + 1 ` is the first character (aka the begining of the string
            # at the delimiter character `#` and 
            # `j + 1 + length` end of the string
            result.append(s[j + 1 : j + 1 + length])  

            # `j + 1 + length` begining of the next string 
            # or the end of the entire string 
            i = j + 1 + length

        return result    

