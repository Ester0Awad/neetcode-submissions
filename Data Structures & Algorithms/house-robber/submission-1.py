class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ....]
        for i in nums:

            # `temp` calculates the better option at the current house
            # calculate max moeny if we rob this house or skip it 
            # temporary variable to calcualted the new max money at the current house without overwriting `rob1` or `rob2`
            temp = max(i + rob1, rob2)
            # once `temp` is calculated, you shift the window of previous states

            # Move `rob2` (the last max) into `rob1` 
            # Move `temp` (the new max) into `rob2`

            rob1 = rob2
            rob2 = temp

        return rob2 


        # Explanation 
        # nums = [2, 7, 9, 3, 1]
        
        # House 1 (n = 2):

        #- temp = max(2 + rob1, rob2) = max(2 + 0, 0) = 2.
        #- Update: rob1 = rob2 = 0, rob2 = temp = 2.

        # /////////////////# 
        # House 2 (n = 7):

        #- temp = max(7 + rob1, rob2) = max(7 + 0, 2) = 7.
        #- Update: rob1 = rob2 = 2, rob2 = temp = 7.  

        #/////////////////////#
        # House 3 (n = 9):

        #- temp = max(9 + rob1, rob2) = max(9 + 2, 7) = 11.
        #- Update: rob1 = rob2 = 7, rob2 = temp = 11.
        #////////////////

        # House 4 (n = 3):

        #- temp = max(3 + rob1, rob2) = max(3 + 7, 11) = 11.
        #- Update: rob1 = rob2 = 11, rob2 = temp = 11.
        # ////////////////
        # House 5 (n = 1):

        # temp = max(1 + rob1, rob2) = max(1 + 11, 11) = 12.
        # Update: rob1 = rob2 = 11, rob2 = temp = 12.

        # ////////////

        # Final result 
            ## After processing all houses, rob2 = 12. 
