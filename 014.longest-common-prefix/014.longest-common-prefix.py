```python
#有没有发现小詹今天换了个编程背景？哈哈哈！
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        #这里利用正则匹配实现，利用率re库
        #初始记第一个字符串为匹配模式
        prefix = strs[0]
        for i in range(1, len(strs)):
            match = re.match(prefix, strs[i])
            while not match:
                #没有匹配到，则将模式后边依次去除一个字符
                prefix = prefix[:-1]
                match = re.match(prefix, strs[i])
        return prefix
```

```python
#有没有发现小詹今天换了个编程背景？哈哈哈！
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #考虑极端情况，当数组中有0或1个字符串时
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]

        l_strs = len(strs)
        #求取字符数组中长度最短的长度值，注释掉的是一种求取方式，
        #这里使用的是另一种min方式
        # for l in range(1,l_strs):
        #     if len(strs[l]) < j_max:
        #         j_max = len(strs[l])
        j_max = min([len(str) for str in strs])
        
        #这里是将最短字符串的字符依次与其他所有字符串对比
        #比如把所有字符串的第一个字符、第二个……进行对比
        for j in range(0,j_max):
            for i in range(1, l_strs):
                #当遇到字符不同的时候，说明这里就是最长共同字符了
                if strs[0][j] != strs[i][j]:
                    return strs[0][:j]
        #否则输出最短字符串
        return strs[0][:j_max]
```