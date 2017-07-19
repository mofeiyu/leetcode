class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        return process(s)
def process(text):
    ans = 0
    pos_dict = {}
    lpos = 0
    for i, ch in enumerate(text):
        if ch in pos_dict:
            lpos = pos_dict[ch] + 1
        pos_dict[ch] = i
        ans = max(ans, i - lpos + 1)
    return ans
