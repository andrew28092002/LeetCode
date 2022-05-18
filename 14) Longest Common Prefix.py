class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        low,high=0,min([len(s) for s in strs])
        while low <= high:
            mid = (low+high)//2
            for s in strs[1:]:
                if strs[0][0:mid] != s[0:mid]:
                    high = mid-1
                    break
            else:
                low = mid+1
        return strs[0][0:low-1] if low > 0 else ''