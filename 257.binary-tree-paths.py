#
# @lc app=leetcode id=257 lang=python
#
# [257] Binary Tree Paths
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root:
            cur_str = str(root.val)
            res = [cur_str]
            stack = [root]
            while stack:
                cur = stack.pop()
                #cur_str += "->%i" %cur.val
                cur_str = res.pop()
                if cur.left:
                    stack.append(cur.left)
                    res.append(cur_str + "->%i" %cur.left.val)
                if cur.right:
                    stack.append(cur.right)
                    res.append(cur_str + "->%i" %cur.right.val)
                if (not cur.left) and (not cur.right):
                    res.insert(0, cur_str)
            return res
        return []
