class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        seen.append(n)
        # print(seen)

        while True:
            next_n = 0
            n_str = str(n)
            for i in range(len(n_str)):
                next_n += int(n_str[i]) ** 2
            
            # print(seen)
            # print(next_n)
            
            if next_n == 1:
                return True
            
            if next_n in seen:
                return False
            
            n = next_n
            seen.append(n)