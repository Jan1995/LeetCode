微信公众号：小詹学python
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        str_x_re = list(str_x)[::-1]
        str_x_re = "".join(str_x_re)
        
        return str_x == str_x_re
        # if str_x == str_x_re:
        #     return true
        #     # result = 'true'
        # else:
        #     # result = 'false'
        #     return false
        # # return result

#上边用字符


class Solution(object):
    # normal way
    def _isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        z = x
        y = 0
        while x > 0:
            y = y * 10 + x % 10
            x //= 10
        return z == y
    
    # faster way
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        half = 0
        while x > half:
            half = half * 10 + x % 10
            x /= 10
        return x == half or half / 10 == x