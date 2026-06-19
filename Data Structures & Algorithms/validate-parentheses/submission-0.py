class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for i in range(len(s)):
            if s[i] in pairs.keys():
                if len(stack) == 0 or stack[-1] != pairs[s[i]]:
                    return False
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack) == 0