#关注小詹学python
#关注小詹学python
#关注小詹学python
beat 97
```
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return [] # 数字字符为空时
        #建立一个字典，键值对形式存放电话按键上数字字符对应关系
        table = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}
        
        result = [''] # 建立空列表，用于存放结果
        for digit in digits: # 从输入digits中依次对每个数字字符处理
            str_list = [] # 设定一个中间过程存放列表
            for char in table[digit]: # result为存放处理过的前边数字字符
                #这里将新数字对应的字符拼接到前边已有的result中
                str_list += [x + char for x in result] 
            result = str_list #将处理好的前边数字结果存放于result，并继续处理后位
        return result
```

#网上代码，同种思路，更简洁！
```
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict = {'2': [i for i in "abc"], '3': [i for i in "def"], \
                '4': [i for i in "ghi"], '5': [i for i in "jkl"], \
                '6': [i for i in "mno"], '7': [i for i in "pqrs"],\
                '8': [i for i in "tuv"], '9': [i for i in "wxyz"]}
								
        def helper(digits, comb = ""):
            if len(digits) > 0:
                for i in dict[digits[0]]:
                    yield from helper(digits[1:], comb + i)
            else:
                yield comb
        return list(helper(digits)) if digits != "" else []
```