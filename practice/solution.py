from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = None
        return ret

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if target < nums[0]:
            return 0
        if target > nums[n - 1]:
            return n
        for i in range(n):
            if nums[i] == target:
                return i
            if i < n - 1 and nums[i] < target < nums[i + 1]:
                return i + 1

    def searchInsert2(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n
        while left < right:
            middle = (left + right) // 2
            if target > nums[middle]:
                left = middle + 1
            else:
                right = middle
        return left

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

    def setzeros(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        markx = []
        marky = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    markx.append(i)
                    marky.append(j)
        for i in range(m):
            for j in range(n):
                if i in markx or j in marky:
                    matrix[i][j] = 0

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root: TreeNode):
            if not root:
                return
            preorder(root.left)
            res.append(root.val)
            preorder(root.right)

        res = list()
        preorder(root)
        return res

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        # 跟结点入queue
        queue = [root]
        res = []
        while queue:
            res.append([node.val for node in queue])
            # 存储当前层的孩子节点列表
            ll = []
            # 对当前层的每个节点遍历
            for node in queue:
                # 如果左子节点存在，入队列
                if node.left:
                    ll.append(node.left)
                # 如果右子节点存在，入队列
                if node.right:
                    ll.append(node.right)
            # 后把queue更新成下一层的结点，继续遍历下一层
            queue = ll
        return res


if __name__ == '__main__':
    example = Solution()
    # example.fourSum([],3)
    example.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
