from typing import List
import collections


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        presum = [0]
        for i, num in enumerate(A):
            if num >= K:
                return 1
            presum.append(num + presum[-1])

        ans = float('inf')
        q = collections.deque()
        for i, num in enumerate(presum):
            while q and presum[q[-1]] >= num:
                q.pop()
            while q and num - presum[q[0]] >= K:
                ans = min(ans, i - q.popleft())
            q.append(i)

        return -1 if ans == float('inf') else ans


print(Solution().shortestSubarray(A=[1], K=1))
print(Solution().shortestSubarray(A=[1, 2], K=4))
print(Solution().shortestSubarray(A=[2, -1, 2], K=3))
print(Solution().shortestSubarray([17, 85, 93, -45, -21], 150))
print(Solution().shortestSubarray([84, -37, 32, 40, 95], 167))
