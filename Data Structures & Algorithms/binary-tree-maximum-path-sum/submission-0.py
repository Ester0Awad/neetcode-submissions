# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # Global varaibel, a list so I can modify it within the recursive function
        result = [root.val]

        # return max path sum WITHOUT SPILIT
        def dfs(root):
            # Base Case
            if not root:
                return 0


            # To get the `max path sum`, it will return `0` if it is null 
            leftMax = dfs(root.left)  
            rightMax = dfs(root.right) 
            # The above variable could be negative so I will update them (example `max(-4, -5, 0)`) 
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            # Updating the result 
            # compute the max path sum WITH SPILIT here -> `root.val + leftMax + rightMax`
            # max of itself or the value that we just computed  here -> `max(res[0]`
            result[0] = max(result[0], root.val + leftMax + rightMax)

            # compute max path WITH SPILIT
            # We can't chose both here `max(leftMax, rightMax)`. Either the left max or the right max
            # The return value is what we compute WITHOUT SPLITING 
            return root.val + max(leftMax, rightMax)
        # update the global variable 
        dfs(root)
        return result[0]

        