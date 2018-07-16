#encoding=utf-8

# ~ #方案一：两层循环
# ~ def twoSum( nums, target):
	# ~ length = len(nums)
	# ~ result = []
	# ~ for i in range(0,length):
		# ~ for j in range(i,length):
			# ~ tSum = nums[i] + nums[j]
			# ~ if tSum == target and i != j:
				# ~ result.append(i)
				# ~ result.append(j)
				# ~ return result
#方案二：一层循环
def twoSum(nums, target):
	result = []
	for i in range(0,len(nums)):
		oneNum = nums[i]
		twoNum  = target - oneNum
		if twoNum in nums:
			j = nums.index(twoNum)
			if i != j:
				result.append(i)
				result.append(j)
				return result


nums = [2,7,11,13]
target = 13
result = twoSum(nums,target)
print(result)

#方案三：
def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # Create a dictionary from the input with its value as the keys and indices as the value
        num_dict = {nums[i]:i for i in range(len(nums))}
        print(num_dict)
        
        # Create a regular dictionary of the complement of the input
        num_dict2 = {i:target-nums[i] for i in range(len(nums))}
        print(num_dict2)
        
        # If the complement is in num_dict return the index of it. 
        r = []
        for i in range(len(nums)):
            j = num_dict.get(num_dict2.get(i))
            if (j is not None) and (j!=i):
                r = [i,j]
                break
        return r