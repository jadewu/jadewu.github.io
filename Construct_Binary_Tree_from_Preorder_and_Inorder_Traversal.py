# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 按照preorder的顺序来建立root，inorder用来分开root.left的部分和root.right部分
# 选取preorder的第一个为root，找到它在inorder里的位置，它左边的是left节点，右边的是right节点
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            pre = preorder.pop(0)
            ind = inorder.index(pre)
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
