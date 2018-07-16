#关注小詹学python
#关注小詹学python
#关注小詹学python
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = 0
        diff = float("inf")
        for i in xrange(0, len(nums)):
            start, end = i + 1, len(nums) - 1
            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                if sum > target:
                    if abs(target - sum) < diff:
                        diff = abs(target - sum)
                        ans = sum
                    end -= 1
                else:
                    if abs(target - sum) < diff:
                        diff = abs(target - sum)
                        ans = sum
                    start += 1
        return ans


#beat100%
```
class Solution:
    def threeSumClosest(self, nums, target):
        # 先排好序，便于比较
        nums.sort()
        length = len(nums)
        closest = []
        #这里是采用固定第一个最小数，从后面切片中两端向中间逼近
        for i, num in enumerate(nums[0:-2]):
            l,r = i+1, length-1	 # i之后的切片：从第一个和最后一个向中逼近				
            if num+nums[r]+nums[r-1] < target:  
            #固定的数加上最大的两个数小于目标值，此时即对于固定一个数后最接近的情况
                closest.append(num+nums[r]+nums[r-1])
            elif num+nums[l]+nums[l+1] > target:
            #固定的数加上最小的两个数大于目标值，此时即对于固定一个数后最接近的情况
                closest.append(num+nums[l]+nums[l+1])
            else: 
                while l < r: # 当l<r,即第二个数小于第三个数时，继续执行
                    closest.append(num+nums[l]+nums[r])
                    if num+nums[l]+nums[r] < target:
                        l += 1 # 如果小于目标值，第二个数后移一个
                    elif num+nums[l]+nums[r] > target:
                        r -= 1 # 如果大于目标值，第三个数前移一个
                    else:
                        return target # 恰好等于，只有一个解，则直接返回
        #上边将可能的情况append进closest，现在先按差的绝对值排序后返回第一个            
        closest.sort(key=lambda x:abs(x-target))
        return closest[0]
```