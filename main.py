from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)

        while left < right:
            mid = (left + right) // 2
            if self.count_operations(nums, mid) <= maxOperations:
                right = mid
            else:
                left = mid + 1

        return left

    def count_operations(self, nums: List[int], max_size: int) -> int:
        operations = 0
        for num in nums:
            if num > max_size:
                operations += (num - 1) // max_size
        return operations

print(Solution().minimumSize([9], 2))  # 5