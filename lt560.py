import collections
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = collections.defaultdict(int)
        m[0] = 1

        ans, s = 0, 0
        for num in nums:
            s += num
            if s - k in m:
                ans += m[s - k]
            m[s] += 1

        return ans


print(Solution().subarraySum(nums=[1, 1, 1], k=2))
