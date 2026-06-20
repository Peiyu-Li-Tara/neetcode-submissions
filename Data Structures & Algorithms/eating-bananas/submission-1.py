class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower_k, upper_k = 1, max(piles)

        while lower_k < upper_k:
            mid_k = (lower_k + upper_k) // 2
            print("mid_k", mid_k)
            if canEatAll(piles, mid_k, h):
                upper_k = mid_k
            else:
                lower_k = mid_k + 1
        
        return lower_k
            
        
def canEatAll(piles, k, h) -> bool:
    t = 0
    for i in piles:
        round_up = 0 if i % k == 0 else 1
        t += i // k + round_up
        print(i // k + round_up)
    if t <= h:
        return True
    else:
        return False