微信公众号：小詹学python
class Solution:
    def isMatch(self, s, p):
        dp = [[False] * (len(p)+1) for _ in range(len(s) + 1)]
        #dp[i][j]=true 表示长度为i的s和j的p匹配
        
        dp[0][0] = True
        dp[0][1] = False
        # if len(s) == 0 or len(s) ==1 or len(p) == 0 or len(p) ==1:
        #     return dp[len(s)][len(p)]
        for i in range(1,len(s) + 1):
            dp[i][0] = False
        for j in range(2,len(p) + 1):
            dp[0][j] = dp[0][j-2] and p[j-1] == '*'
        
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (p[j-1] == '.' or p[j-1] == s[i-1])
                else:
                    dp[i][j] = dp[i][j-2] or \
                    (dp[i-1][j-2] and (p[j-2] == '.' or p[j-2] == s[j-1])) or\
                    (dp[i-1][j] and (p[j-2] == '.' or p[j-2] == s[j-1]))
                
        return dp[-1][-1]
                    
                


# class Solution:
#     def isMatch(self, s, p):
#         return s in re.findall(p, s)

# class Solution:
#     def isMatch(self, s, p):
#         return bool(re.match(p, s)) and re.match(p, s).group(0) == s 

```python
class Solution:
    def isMatch(self, s, p):
        #dp[i][j]=true 表示长度为i的s和j的p匹配
        dp = [[False] * (len(p)+1) for _ in range(len(s) + 1)]
        #i = j = 0时
        dp[0][0] = True
        #j = 0,i >= 1时，默认为false。其实可以忽略，小詹写出来方便读者理解
        for i in range(1,len(s) + 1):
            dp[i][0] = False
        #i = 0,j >= 2时    
        for j in range(2,len(p) + 1):
            dp[0][j] = dp[0][j-2] and p[j-1] == '*'
        #i >= 1,j >= 1时
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                #对应第五类情况p[j-1]不为‘*’的一类，下else相反
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (p[j-1] == '.' or p[j-1] == s[i-1])
                else:
                    dp[i][j] = dp[i][j-2] or \
                    (dp[i-1][j] and (p[j-2] == '.' or p[j-2] == s[i-1]))
                
        return dp[-1][-1]

```