# Definition for a binary tree node.  英文是資料結構的介紹
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val 值
#         self.left = left 左邊的小孩
#         self.right = right 右邊的小孩
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root == None: return root #沒有東西 就提早結束
        left = self.removeLeafNodes(root.left,target) #先用同一函示 處理左半邊
        right = self.removeLeafNodes(root.right,target) #用同一個函式 處理右半邊
        if left==None and right==None and root.val==target:
            return None #甚麼都沒有 交給當初呼叫我的人

        root.left = left
        root.right = right
        return root