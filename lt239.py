from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, res = [], []
        for i, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                del q[-1]

            q.append(i)
            if i - q[0] >= k:
                del q[0]

            if i >= k - 1:
                res.append(nums[q[0]])

        return res


print(Solution().maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
