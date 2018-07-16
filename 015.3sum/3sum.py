```
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #定义一个空列表，并将原列表排序
        result = []
        nums.sort()
        #原列表长度
        ly_len = len(nums)
        #遍历所有
        for i in range(ly_len-1):
            for j in range(i + 1,ly_len):
                #当前两数之和的相反数在列表切片nums[j+1:]中即可
                if -(nums[i]+nums[j]) in nums[j+1:]:
                    ly = [nums[i],nums[j],-(nums[i]+nums[j])]
                    if ly not in result:
                        result.append(ly)   
        return result
```超时！！！

```beat90
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #同上，空列表和排序
        res = []
        nums.sort()
        #固定一个数，另外两个数来匹配，凑0
        for i in range(0, len(nums)):
            #排序后可能存在相等的数连续，比如[-1,-1,0……];continue下次循环
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i] #另外两个数之和为target
            start, end = i + 1, len(nums) - 1#从后续列表切片两端向中间逼近
            while start < end:
                if nums[start] + nums[end] > target:
                    end -= 1  #如果首位之和大于目标值，尾部索引减一
                elif nums[start] + nums[end] < target:
                    start += 1#如果首位之和小于目标值，首部索引加一
                else:#等于目标值，则记录当前一组解，并寻找其他解
                    res.append((nums[i], nums[start], nums[end]))
                    end -= 1
                    start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1 #如果尾部连续两个数相等时，尾部索引减一
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1#如果首部连续两个数相等时，首部索引加一
        return res
```