class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_stack = []
        for o in operations:
            if o == "D":
                score_stack.append(score_stack[len(score_stack) - 1] * 2)
            elif o == "C":
                score_stack.pop()
            elif o == "+":
                new_sum = score_stack[len(score_stack) - 2] + score_stack[len(score_stack) - 1]
                score_stack.append(new_sum)
            else:
                score_stack.append(int(o))
            print(score_stack)
            
        return sum(score_stack)
        
        