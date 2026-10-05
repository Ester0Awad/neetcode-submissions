class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s) - 1
        
        # To make the charcters lowercase  
        s = s.lower()

        
        while left_pointer < right_pointer:

            # If the character is non-alphanumeric, then run the skipping code.
            # pointer is simply a variable that holds an integer index.
            # The purpose of the skipper loop is to wait until an invalid character is encountered and then run the code to move the pointer.

            while not s[left_pointer].isalnum() and left_pointer < right_pointer:
                left_pointer += 1
            while not s[right_pointer].isalnum() and left_pointer < right_pointer:
                right_pointer -= 1

            # `break` if the pointers might has crossed
            if left_pointer >= right_pointer:
                break #exist the main while loop


            # Now, both charcters are valid and lowercase
            if s[left_pointer].lower() != s[right_pointer].lower():
                return False

            # If they DO match, we move both pointers inward to check the next pair.
            else:
                left_pointer += 1
                right_pointer -= 1

        return True

                
                    


