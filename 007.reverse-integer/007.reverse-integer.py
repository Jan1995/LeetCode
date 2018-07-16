微信公众号：小詹学python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = x < 0 and -1 or 1
        x = abs(x)
        ans = 0
        while x:
            ans = ans * 10 + x % 10
            x /= 10
        return sign * ans if ans <= 0x7fffffff else 0


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #先记录正负
        sign = [1,-1][x < 0]
        #利用正负反转后符号不变，并利用绝对值函数进行反转，添加原有符号即可
        rst = sign * int(str(abs(x))[::-1])
        #返回反转值，超出32位为0
        return rst if -(2**31)-1 < rst < 2**31 else 0


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #定义一个空字符串，思路是将数字字符化通过以下计算反转，
        #转换成字符串后反转转换成数字
        s = ''
        while x//10 != 0:
            num = x % 10
            s = s + str(num)
            x //= 10
        s = s + str(x) #针对最高位或者本身就是个位数的特殊情况  

        return int(s)