"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        queue = [] if root == None else [(root, 0)]
        result = []
        while len(queue) > 0:
            node, level = queue.pop(0)
            if level >= len(result):
                result.append([])
            result[level].append(node.val)

            if node.children != None:
                for child in node.children:
                    queue.append((child, level + 1))
        return result


    def levelOrder1(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        queue = [] if root == None else [root]
        result = []
        while len(queue) > 0:
            l = queue
            queue = []
            for item in l:
                for child in item.children:
                    queue.append(child)
            result.append([i.val for i in l])

        return result
