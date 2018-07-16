微信公众号：小詹学python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = right = 0
        n = len(s)
        for i in range(n - 1):
            if 2 * (n - i) + 1 < right - left + 1:
                break
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 2 > right - left:
                left = l + 1
                right = r - 1
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 2 > right - left:
                left = l + 1
                right = r - 1
        return s[left:right + 1]

#
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        self.res = ""
        for i in range(len(s)):
            self.helper(s, i, i)
            self.helper(s, i, i+1)
        return self.res
        
    def helper(self,s, left, right):
        while left>=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if right -left -1 > len(self.res):
            self.res = s[left+1:right]