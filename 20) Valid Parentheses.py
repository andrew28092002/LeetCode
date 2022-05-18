class Solution:
    def isValid(self, s: str) -> bool:
        dct = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            if i in dct.values():
                stack.append(i)
            else:
                if stack and dct[i] == stack[-1]:
                    del stack[-1]
                else:
                    return False
        return len(stack) == 0

