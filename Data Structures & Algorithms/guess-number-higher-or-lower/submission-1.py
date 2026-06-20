# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        n_range = range(1, n + 1)

        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            target = n_range[mid]
            if guess(target) == -1:
                r = mid - 1
            elif guess(target) == 1:
                l = mid + 1
            else:
                return target