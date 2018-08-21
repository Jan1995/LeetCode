#欢迎关注小詹学python
```
class Solution(object):
    def generateParenthesis(self, n):
        #子函数 ，生成括号序列 ，递归思路哦
        def generate(A = []):
            if len(A) == 2*n: #如果生成的括号序列长度为2n，就判断是否有效
                if valid(A):
                    ans.append("".join(A)) #有效括号序列添加进ans
            else: 
            #不够长度则通过递归调用generate生成，如果是无效则将上一个括号字符pop出，并继续generate
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()
        #判断生成的长度为2n括号序列是否有效
        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0
        #定义空列表ans存储，通过调用generate执行直到所有结果都判断了一遍结束
        ans = []
        generate()
        return ans
```

```
class Solution(object):
    def generateParenthesis(self, N):
        #依旧是递归 ，只不过不是暴力列出所有的括号字符串
        #而是当当前括号字符串序列仍然保持有效时才添加
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            #这里比较关键，需要好好理解下！看推文中的讲解。
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)
        ans = []
        backtrack()
        return ans
```