```
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #初始记为最大面积为0（用面积衡量容量噢）
        max_area = 0
        n = len(height)
        #这里有点没技术含量，遍历所有情况，小詹在之前很多题都写过详细注释，不再赘述
        for i in range(n):
            for j in range(i,n):
                area = (j - i)*min(height[i],height[j])
                if area >= max_area:
                    max_area = area
        return max_area
```

```
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #定义初始面积为0，并用索引模拟指针指向两头
        max_area = left = 0
        right = len(height) - 1
        #循环执行条件
        while left < right:
            #最大面积
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            #向大佬低头哈哈哈
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area
```