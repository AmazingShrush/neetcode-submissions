# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr=[]
        def preOrderTraversal(node):
            if node is None:
                arr.append(None)
                return
            arr.append(node.val)
            preOrderTraversal(node.left)
            preOrderTraversal(node.right)

            return arr
        
        p_arr = preOrderTraversal(p)
        arr=[]
        q_arr = preOrderTraversal(q)

        return p_arr == q_arr