# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        l=[]
        if not root:
            return []
        frontier=[root]
        parent={}
        level={}
        i=1
        while frontier:
            r=[]
            for z in frontier:
                if z:
                    r.append(z.val)
            l.append(r)
            next=[]
            for u in frontier:
                if u.left:
                    next.append(u.left)
                if u.right:
                    next.append(u.right)
            i=i+1
            frontier=next
        return l[::-1]