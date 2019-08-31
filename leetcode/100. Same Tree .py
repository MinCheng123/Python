class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
p = TreeNode(1)
pl = TreeNode(2)
pr = TreeNode(2)
q = TreeNode(1)
ql = TreeNode(2)
qr = TreeNode(3)

p.left = pl
p.right = pr

q.left = ql
q.right = qr

class Solution(object):

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        self.flag = True
        if p is None and q is None:
            return True
        while p and q:
            if p.val==q.val:

                if p.left  and q.left :
                    self.flag=self.isSameTree(p.left,q.left)
                    if self.flag is False:
                        break
                elif p.left is None and q.left is None:
                    pass
                else:
                    return False
                
                if p.right  and q.right :    
                    self.flag=self.isSameTree(p.right,q.right)
                    if self.flag is False:
                        break
                elif p.right is None and q.right is None:
                    pass
                else:
                    return False
                return True

            else:
                return False
        return False
x = Solution()
ans=x.isSameTree(p,q)
print(ans)