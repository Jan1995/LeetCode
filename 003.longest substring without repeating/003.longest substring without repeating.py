# liangduansuojin
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         sLen = len(s)
#         if sLen == 0 or sLen == 1:
#             return sLen
#
#         letters = list(s)
#
#         hashSet = {}
#         hashSet[letters[0]] = 1
#
#         start = 0
#         end = 1
#
#         maxLen = 1
#
#         while end != sLen:
#             letter = letters[end]
#
#             if hashSet.has_key(letter) and hashSet[letter] > 0:
#                 hashSet[letters[start]] -= 1
#                 start += 1
#                 continue
#
#             hashSet[letter] = 1
#             end += 1
#             if end - start > maxLen:
#                 maxLen = end - start
#
#         return maxLen

s = 'pwwkew'
# sLen = len(s)
# if sLen == 0 or sLen == 1:
#     print(sLen)
#
# letters = list(s)
# print(letters)
# hashSet = {}
# hashSet[letters[0]] = 1
#
# start = 0
# end = 1
#
# maxLen = 1
#
# while end != sLen:
#     letter = letters[end]
#
#     if hashSet.has_key(letter) and hashSet[letter] > 0:
#         hashSet[letters[start]] -= 1
#         start += 1
#         continue
#
#     hashSet[letter] = 1
#     end += 1
#     if end - start > maxLen:
#         maxLen = end - start
#
# print(maxLen)


# max_len = 0
# if (len(s) == 1 or len(s) == 0):
#     max_len = len(s)
# for i in range(0,len(s)-1):
#     for j in range(i+1, len(s)):
#         if s[j] in s[i:j]:
#             if j-i > max_len:
#                 right = j
#                 left = i
#                 max_len = right-left
#             break
#         elif j == len(s) - 1:
#             if max_len < j - i +1:
#                 max_len = j - i + 1
# print(max_len)
# print(right,left)

# indexDict = {}
# maxLength = currMax = 0
# for i in range(len(s)):
#     if s[i] in indexDict and i - indexDict[s[i]] - 1 <= currMax:
#         if maxLength < currMax:
#             maxLength = currMax
#         currMax = i - indexDict[s[i]] - 1
#     currMax = currMax + 1
#     indexDict[s[i]] = i
# # if currMax > maxLength:
# #     maxLength = currMax
# # print(maxLength)
# print(maxLength if currMax < maxLength else currMax)