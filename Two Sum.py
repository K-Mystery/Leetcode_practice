"""
Given an array of integers num and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Solution 1 O(n**2) 暴力枚举
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums [j] == target and i!=j:
                    out.append(i)
                    out.append(j)
                    return out

# 2 hash table, python中的字典是哈希表 O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()
        for i,num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target-num],i]
            hash_table[num] = i
        return []

