#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start

"""
O(n)复杂度
从左到右扫描，使用哈希表记录
遇到重复则开头调到重复字符的后一个
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        start = 0
        max_len = 0
        tmp = 0
        for i in range(len(s)):
            if (not s[i] in dict) or dict[s[i]]<start:
                tmp += 1
                max_len = max(max_len, tmp)
            else:
                start = dict[s[i]] + 1
                max_len = max(max_len, tmp)
                tmp = i - start + 1
            dict[s[i]] = i
        return max_len
        



        
# @lc code=end

