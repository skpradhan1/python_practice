import itertools

class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) ==0 :
            return 0
        start, max_p = 0,0
        for end in range(len(s)):
            righ_char = s[end]
            left_char = s[start]
            if righ_char == left_char:
                max_p = max(max_p, end-start+1)
            else:
                start = end
        return  max_p

    def maxPower1(self, s):
        for k, v in itertools.groupby(s):
            print("k", k)
            print("v", list(v))


s = Solution()
print(s.maxPower("leetcode"))
print(s.maxPower("abbcccddddeeeeedcba"))
print(s.maxPower1("ccbccbb"))