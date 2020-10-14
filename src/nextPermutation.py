from typing import List

class NextPermutation:
    def nextPermutation(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        def find_pivot(nums):
            m = nums[-1]
            i = len(nums) - 1
            while i >= 0 and nums[i] >= m:
                m = nums[i]
                i -= 1
            return i

        def find_successor(nums, pivot):
            j = len(nums) - 1
            while nums[pivot] >= nums[j]:
                j -= 1
            assert j > pivot
            return j

        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        if len(nums) < 2:
            return nums
        # 找到第一个下降的索引
        i = find_pivot(nums)
        if i < 0:
            nums.sort()
        else:
            #在i后面找到第一个大于nums[i]的索引j
            j = find_successor(nums, i)
            # 把索引位置i,j上的数字交换一下
            nums[i], nums[j] = nums[j], nums[i]
            # 索引位置i之后的数组排序
            reverse(nums, i+1, len(nums)-1)
        return nums