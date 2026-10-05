class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bla = {}
        for i, n in enumerate(nums):
            x = target - n

            #if the (outcome) in `bla`
            if x in bla:
                #return indicies
                #return [?, i]
                return [bla[x], i]
            #if we didn't find the solution, update the hashmap `bla`    
            bla[n] = i
        return     
            

