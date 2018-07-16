微信公众号：小詹学python
```python
class Solution:
    def myAtoi(self, string):
        #正负可以用这个+-1处理，最后返回result时乘以sign即可
        sign = 1
        result = 0
        found = False
        n = len(string)
        for char in string:
            # 利用continue跳过开头的空格符
            if not found and char == " ":
                continue
            # 检测到符号-表示负数，sign记为-1
            elif not found and char == "-":
                found = True
                sign = -1
            # 检测到符号+表示正数
            elif not found and char == "+":
                found = True
            # 利用str.isdigit()方法检测字符是否为数字
            elif char.isdigit():
                found = True
                result = result * 10 + int(char)
                # 确定是否超出范围，超出则按照边界输出
                if result > 2147483647 and sign == 1:
                    return 2147483647
                if result > 2147483648 and sign == -1:
                    return -2147483648
            #其他情况，首字符是字母等。跳出，返回result=0
            else:
                break
        return sign * result
```