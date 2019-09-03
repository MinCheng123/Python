class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: 
            return 0
        deep=1
        
        ans=self.recursive(root,deep)
        return ans

    def recursive(self,root,deep):
        temp=deep

        if root.left:
            deep =self.recursive(root.left,temp+1)            
        if root.right:
            temp2=self.recursive(root.right,temp+1)
            if  deep < temp2:
                deep=temp2
                
        deep=max(deep,temp)
        return deep     4

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
A=TreeNode(1)
B=TreeNode(2)
C=TreeNode(3)
D=TreeNode(4)
E=TreeNode(5)
A.left=B
A.right=C
B.left=D
B.right=E
Ans=Solution()
answer=Ans.maxDepth(A)
print(answer)