import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        m = collections.defaultdict(int)
        tail, ans = 0, 0
        for i, c in enumerate(s):
            m[c] += 1
            while m[c] > 1:
                c_del = s[tail]
                if m[c_del] > 0:
                    m[c_del] -= 1
                    if m[c_del] == 0:
                        del m[c_del]
                tail += 1
            ans = max(ans, i - tail + 1)
        return ans


for s in ["abcabcbb", "bbbbb", "pwwkew"]:
    print(Solution().lengthOfLongestSubstring(s))
