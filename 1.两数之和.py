#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            if b in table:
                return [table[b], i]   #再往i之前的元素找，所以要反过来
            else:
                table[a] = i
        
# @lc code=end

