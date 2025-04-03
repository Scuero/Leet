# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def es_simetrico(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (p.val==q.val and self.es_simetrico(p.right,q.left) and self.es_simetrico(p.left,q.right))

    def isSymmetric(self, root):
        if not root:
            return True
        return self.es_simetrico((root.left), (root.right))
        