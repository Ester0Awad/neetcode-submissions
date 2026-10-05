class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       # Making a `hashset` to see if the number in `nums` 
       # in `hashset`, return True. 
       # Other than that, add the number into the hashmap
       # `set()` in python can not has duplicates, that is why 
       # we used it to check the duplications.  
        hashset = set()
        for i in nums:
          if i in hashset:
            return True
          hashset.add(i)

        return False             