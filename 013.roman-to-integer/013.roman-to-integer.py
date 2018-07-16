```
class Solution(object):
    def romanToInt(self, s):
        #定义一个字典，将罗马数字的所有组合列举出来。
        map={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        #初始为0
        i,res=0,0
        while i<len(s):
            #从头到尾进行查找，s[i:i+2]表示切片，注意左闭右开！
            if i<len(s)-1 and map.get(s[i:i+2]) != None:
                i,res =i+2,res+map[s[i:i+2]]
            #当同时匹配两个罗马数字字符，在字典key中无匹配时，单独进行一个字符匹配
            else:
                if map.get(s[i])!=None:
                    i,res=i+1,res+map[s[i]]
        return res
```

```
class Solution(object):
    def romanToInt(self, s):
        #这里构建字典单字符罗马数字
        romans = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}
        #记录前一个字符代表的数字，初始为0
        prev_value = running_total = 0
        #从低位到高位，依次处理
        for i in range(len(s)-1, -1, -1):
            int_val = romans[s[i]]
            #如果当前值小于前一位（右边），表示是特殊情况，为右-左
            if int_val < prev_value:
                running_total -= int_val
            #如果当前值不小于前一位（右边），为正常加的情况
            else:
                running_total += int_val
            #记录当前值为历史值，并进行下一次循环
            prev_value = int_val
        return running_total
```