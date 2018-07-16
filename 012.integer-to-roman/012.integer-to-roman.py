
```
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #定义空字符串输出
        ans = ""
        #构建一个字典和一个列表；数字的匹配对应，列表用于输出添加到空字符串中输出
        values = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        literals = ["M", "D", "C", "L", "X", "V", "I"]
        #依次除以1000；100；10；1，进行处理
        for idx in [0, 2, 4]:
            #k表示整除得到的商，这里实际上只有在除以1000时会用的上（可以代个数试试）
            k = num // values[literals[idx]]
            #re表示取模后再除以低一个数量级得到的商
            re = (num % values[literals[idx]]) // values[literals[idx + 2]]
            #小詹提醒：输入在1-3999范围内，所以除以1000最大商为3
            ans += k * literals[idx]
            #这里针对不同的特殊情况分类处理
            #取模为9时
            if re >= 9:
                ans += literals[idx + 2] + literals[idx] 
            #取模为5；6；7；8时
            elif re >= 5:
                ans += literals[idx + 1] + (re - 5) * literals[idx + 2]
            #取模为4时
            elif re == 4:
                ans += literals[idx + 2] + literals[idx + 1]
            #取模为0；1；2；3时
            else:
                ans += re * literals[idx + 2]
            #取模后进行下一次循环
            num %= values[literals[idx + 2]]
        return ans
        
```