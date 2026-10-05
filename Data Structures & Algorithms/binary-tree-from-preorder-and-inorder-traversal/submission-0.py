# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # if `preorder` or `inorder` is empty 
        # Base case
        if not preorder or not inorder:
            return None

        # The root is always the first value of `preorder` array
        root = TreeNode(preorder[0])
        # Finding the position of `preorder[0]` which is the root (aka always the first value of the `inorder` array)
        mid = inorder.index(preorder[0])

        # Calling the function recursively 
        # The value of `mid` tells us how many nodes we want in the "left sub tree" 
        # `preorder[1 : mid + 1]` -> starting from index `1`, skipping index `0` as it is the root
        # `mid + 1` is inclusive (for example if x = [1, 2, 3, 4, 5, 6] --->>> x[1:3] is ---> [2, 3])
        # `inorder[:mid]` from the beginning up until `mid` but not including `mid` 
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])

        # We need every value after the "right sub tree" list, so we will get this ---->>> (aka `preorder[mid + 1 :]`) until the end of the list 
        # `inorder[mid + 1 :]` we want every node to the right of `mid` until the end of the array
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        # return the tree
        return root
        