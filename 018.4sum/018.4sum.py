#关注小詹学python
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        n_len = len(nums)
        for i in range(n_len-3):
            for j in range(i+1,n_len-2):
                left,right = j+1,n_len-1
                while left < right:
                    if nums[i]+nums[j]+nums[left]+nums[right] < target:
                        left += 1
                    elif nums[i]+nums[j]+nums[left]+nums[right] > target:
                        right -= 1
                    elif nums[i]+nums[j]+nums[left]+nums[right] == target:
                        if [nums[i],nums[j],nums[left],nums[right]] not in res:                      
                            res.append([nums[i],nums[j],nums[left],nums[right]])
                        left,right = left+1,right-1
        return res

#思路二
class Solution:
    def fourSum(self, nums, target):
        def nSum(nums, target, n, result, results):
            if len(nums) < n or n < 2 or n * nums[0] > target or n * nums[-1] < target:
                return []
            if n == 2:
                begin, end = 0, len(nums) - 1
                while begin < end:
                    sums = nums[begin] + nums[end]
                    if sums < target:
                        begin += 1
                    elif sums > target:
                        end -= 1
                    else:
                        plet = [nums[begin], nums[end]]
                        results.append(result + plet)
                        while begin < end and nums[begin] == plet[0]: begin += 1
                        while begin < end and nums[end] == plet[1]: end -= 1
            else:
                for i in range(len(nums) - n + 1):
                    if (i > 0 and nums[i] == nums[i - 1]) or (nums[i] + (n - 1) * nums[len(nums) - 1] < target):
                        continue
                    if n * nums[i] > target:
                        break
                    if n * nums[i] == target and i + n -1 < len(nums) and nums[i + n - 1] == nums[i]:
                        plet = [nums[i]] * n
                        results.append(result + plet)
                        break
                    nSum(nums[i + 1:], target - nums[i], n - 1, result + [nums[i]], results)

        results = []
        nums.sort()
        nSum(nums, target, 4, [], results)
        return results