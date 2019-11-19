# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        result = 0
        queue = [(root, 0)]
        while len(queue) > 0:
            item = queue.pop(0)
            node = item[0]
            if node.left != None:
                queue.append((node.left, 1))
            if node.right != None:
                queue.append((node.right, 2))

            if node.left == None and node.right == None and item[1] == 1:
                result += node.val

        return result
