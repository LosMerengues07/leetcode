#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        startnode = ListNode()
        node = startnode
        cur_node1 = l1
        cur_node2 = l2
        addition = 0
        while(True):
            if cur_node1:
                a = cur_node1.val
            else:
                a = 0
            if cur_node2:
                b = cur_node2.val
            else:
                b = 0
            if cur_node1:
                cur_node1 = cur_node1.next
            if cur_node2:
                cur_node2 = cur_node2.next
            sum = a + b + addition   #每位和为两数对应位之和加进位
            node.val = sum%10
            addition = sum//10
            if (not cur_node1) and (not cur_node2) and addition==0:
                node.next = None
                return startnode
            node.next = ListNode()
            node = node.next
# @lc code=end

