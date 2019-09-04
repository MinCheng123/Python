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
                pil = "->"
                path = ""
                answer = []
                if root is None:
                        return []
                self.recursive(root, pil, path, answer)
                return answer

        def recursive(self, root, pil, path, answer):

                if root.left:
                        self.recursive(root.left, pil, path + str(root.val) + pil, answer)

                if root.right:
                        self.recursive(root.right, pil, path + str(root.val) + pil, answer)

                path = path + str(root.val)
                if root.left is None and root.right is None:
                        answer.append(path)
