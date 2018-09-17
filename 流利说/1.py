class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.total = sum
        def caculate(root,sum,templist):
            if not root:
                return
            if not root.left and not root.right:
                if root.val+sum == self.total:
                    self.res.append(templist+[root.val])
            if root.left:
                caculate(root.left,sum+root.val,templist+[root.val])
            if root.right:
                caculate(root.right,sum+root.val,templist+[root.val])
        1caculate(root,0,[])
        return self.res