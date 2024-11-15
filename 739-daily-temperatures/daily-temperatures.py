class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stk_temp, stk_inx = stack.pop()
                answer[stk_inx] = i - stk_inx
            stack.append((t,i))
        return answer
