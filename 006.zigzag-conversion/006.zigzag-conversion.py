微信公众号：小詹学python
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = numRows
        #开始小詹是利用列表保存，然后得到结果
        #再将其转换为字符串的，这里定义空的列表
        res_list = []
        l = len(s)
        #考虑到极端情况，其实这里小詹还是没有考虑全
        #除了一行，还应该考虑到单字符串或者空字符串
        if n == 1:
            return s
        #遍历0到n-1行
        for i  in range(n):
            #遍历所有字符，j表示索引
            for j in range(l):
                #这是就是小詹介绍的取模判断是否在第i行输出
                if j%(2*n-2) == i or j%(2*n-2) == 2*n-2-i:
                    res_list.append(s[j])
        #这里就是利用join将列表转换为字符串
        res = "".join(res_list)
        
        return res
#上边超出时间限制


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        n = len(s)
        ans = []
        step = 2 * numRows - 2
        for i in range(numRows):
            one = i
            two = -i
            while one < n or two < n:
                if 0 <= two < n and one != two and i != numRows - 1:
                    ans.append(s[two])
                if one < n:
                    ans.append(s[one])
                one += step
                two += step
        return "".join(ans)

#
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        str_length = len(s)
        node_length = 2*numRows - 2  # 两列之间的差
        result = ""

        if str_length == 0 or numRows == 0 or numRows == 1:
            return s

        for i in range(numRows):  # 从第一行遍历到最后一行
            for j in range(i, str_length, node_length):
                result += s[j]  # 第一行和最后一行  还有普通行的整列数字
                if i != 0 and i != numRows-1 and j - 2*i + node_length < str_length:
                    result += s[j-2*i+node_length]  # 单列行的数字
        return result