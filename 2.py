from typing import List


class Solution:
    def canPartition1(self, nums: List[int]) -> bool:
        if not nums:
            return False

        target, n = sum(nums), len(nums)
        if target % 2 != 0:
            return False
        target = target // 2

        dp = [[False for _ in range(target + 1)] for _ in range(n)]
        if nums[0] < target:
            dp[0][nums[0]] = True

        for i in range(n):
            for j in range(1, target + 1):
                if nums[i] == j:
                    dp[i][j] = True
                elif nums[i] < j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]

        return dp[n - 1][target]

    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False

        target, n = sum(nums), len(nums)
        if target % 2 != 0:
            return False
        target = target // 2

        dp = [False for _ in range(target + 1)]
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(target, 0, -1):
                if nums[i - 1] > j:
                    continue
                dp[j] = dp[j] or dp[j - nums[i - 1]]

        return dp[target]


print(Solution().canPartition([1, 5, 11, 5]))
print(Solution().canPartition([1, 2, 3, 5]))
