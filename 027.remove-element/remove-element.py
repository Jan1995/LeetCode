#»¶Ó­¹Ø×¢Ð¡Õ²Ñ§python
```
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        length = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[length] = nums[i]
                length = length + 1
                
        return length
```