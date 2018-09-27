#»¶Ó­¹Ø×¢Ð¡Õ²Ñ§python
```
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        length = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[length] = nums[i+1]
                length = length +1
        
        return length
```

